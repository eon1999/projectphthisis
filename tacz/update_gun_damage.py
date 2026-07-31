#!/usr/bin/env python3
"""
Script to update gun damage values in TACZ gun data files based on gun_index_tiered.csv
"""
import csv
import json
import os
import sys
from pathlib import Path

# Pack configuration: maps CSV pack name to (directory_path, namespace)
PACK_CONFIG = {
    "Apocalypse (bf1)": ("Apocalypse_v1.1.7_G", "bf1"),
    "ChocolateMan (qkl)": ("ChocolateMan V1.2.6a1-Public Edition", "qkl"),
    "EMX Arms": ("[Tacz1.1.5+]EMX-Arms GunsPack ver1.1.5.zip", "emxarms"),
    "MS-Mobius": ("[Tacz1.1.8+]MS-Mobius Gunspack v1.5.8", "sfms"),  # Also has erode namespace
    "Suffuse": ("Suffuse-GunSmoke-Pack1.0.7--hotfix", "suffuse"),
    "TRIS Dyna": ("[Tacz1.1.5+]TRIS-dyna GunsPack ver1.1.5.zip", "trisdyna"),
    "TaCZ Expanded Arsenal": ("TaCZ_-Expanded-Arsenal-v2.9", "tacz"),
    "daffas": ("daffas", "daffas_arsenal"),
    "tacz (vanilla)": ("tacz_default_gun", "tacz"),
}

# For MS-Mobius, we need to handle both sfms and erode namespaces
MS_MOBIUS_NAMESPACES = ["sfms", "erode"]

def load_csv(csv_path):
    """Load the CSV and return a dict mapping gun_id to damage info."""
    gun_data = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            gun_id = row['gun_id']
            gun_data[gun_id] = {
                'tier': row['tier'],
                'pack': row['pack'],
                'type': row['type'],
                'ammo': row['ammo'],
                'note': row['note'],
                'bullet_damage': float(row['bullet_damage']) if row['bullet_damage'] else None,
                'bullet_amount': int(row['bullet_amount']) if row['bullet_amount'] else None,
                'explosion_damage': float(row['explosion_damage']) if row['explosion_damage'] else None,
            }
    return gun_data

def update_gun_data_file(file_path, csv_info):
    """Update a single gun data file with CSV values."""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed = False

    # Update bullet damage
    if 'bullet' in data and csv_info['bullet_damage'] is not None:
        old_damage = data['bullet'].get('damage')
        new_damage = csv_info['bullet_damage']
        if old_damage != new_damage:
            # Scale damage_adjust proportionally
            if 'damage_adjust' in data['bullet'] and old_damage and old_damage > 0:
                scale = new_damage / old_damage
                for entry in data['bullet']['damage_adjust']:
                    if 'damage' in entry:
                        entry['damage'] = round(entry['damage'] * scale, 1)
            data['bullet']['damage'] = new_damage
            changed = True
            print(f"  Updated bullet.damage: {old_damage} -> {new_damage}")

    # Update bullet amount
    if 'bullet' in data and csv_info['bullet_amount'] is not None:
        old_amount = data['bullet'].get('bullet_amount')
        new_amount = csv_info['bullet_amount']
        if old_amount != new_amount:
            data['bullet']['bullet_amount'] = new_amount
            changed = True
            print(f"  Updated bullet.bullet_amount: {old_amount} -> {new_amount}")

    # Update explosion damage
    if 'bullet' in data and 'explosion' in data['bullet'] and csv_info['explosion_damage'] is not None:
        old_explosion = data['bullet']['explosion'].get('damage')
        new_explosion = csv_info['explosion_damage']
        if old_explosion != new_explosion:
            data['bullet']['explosion']['damage'] = new_explosion
            changed = True
            print(f"  Updated bullet.explosion.damage: {old_explosion} -> {new_explosion}")

    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return True
    return False

def process_pack(base_dir, pack_name, namespace, csv_data):
    """Process all guns for a specific pack."""
    pack_dir = Path(base_dir) / PACK_CONFIG[pack_name][0]
    data_dir = pack_dir / "data" / namespace / "data" / "guns"

    if not data_dir.exists():
        print(f"Data directory not found: {data_dir}")
        return 0, 0

    # Filter CSV data for this pack
    pack_guns = {k: v for k, v in csv_data.items() if v['pack'] == pack_name}

    updated = 0
    skipped = 0

    for gun_id, info in pack_guns.items():
        # Extract gun name from gun_id (e.g., "bf1:martini" -> "martini")
        if ':' in gun_id:
            gun_name = gun_id.split(':', 1)[1]
        else:
            gun_name = gun_id

        data_file = data_dir / f"{gun_name}_data.json"

        if data_file.exists():
            print(f"Processing {gun_id}...")
            if update_gun_data_file(data_file, info):
                updated += 1
            else:
                skipped += 1
        else:
            print(f"  WARNING: Data file not found: {data_file}")
            skipped += 1

    return updated, skipped

def main():
    base_dir = Path(r"C:\Users\Viet-Anh\curseforge\minecraft\Instances\Project Phthisis\tacz")
    csv_path = base_dir / "gun_index_tiered.csv"

    if len(sys.argv) < 2:
        print("Usage: python update_gun_damage.py <pack_name>")
        print("Available packs:")
        for pack in PACK_CONFIG.keys():
            print(f"  {pack}")
        sys.exit(1)

    pack_name = sys.argv[1]

    if pack_name not in PACK_CONFIG:
        print(f"Unknown pack: {pack_name}")
        sys.exit(1)

    print(f"Loading CSV data from {csv_path}...")
    csv_data = load_csv(csv_path)
    print(f"Loaded {len(csv_data)} gun entries from CSV")

    if pack_name == "MS-Mobius":
        # Handle both namespaces for MS-Mobius
        total_updated = 0
        total_skipped = 0
        for ns in MS_MOBIUS_NAMESPACES:
            print(f"\n=== Processing MS-Mobius namespace: {ns} ===")
            # Temporarily modify config for this namespace
            updated, skipped = process_pack(base_dir, pack_name, ns, csv_data)
            total_updated += updated
            total_skipped += skipped
        print(f"\n=== MS-Mobius Total: {total_updated} updated, {total_skipped} skipped ===")
    else:
        namespace = PACK_CONFIG[pack_name][1]
        print(f"\n=== Processing {pack_name} (namespace: {namespace}) ===")
        updated, skipped = process_pack(base_dir, pack_name, namespace, csv_data)
        print(f"\n=== {pack_name} Total: {updated} updated, {skipped} skipped ===")

if __name__ == "__main__":
    main()