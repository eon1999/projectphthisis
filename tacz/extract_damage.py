import json
import os
import csv

base_path = r"C:\Users\Viet-Anh\curseforge\minecraft\Instances\Project Phthisis\tacz"

# Find all gun data files
gun_data_files = []
for root, dirs, files in os.walk(base_path):
    for f in files:
        if f.endswith("_data.json") and "data" in root and "guns" in root:
            gun_data_files.append(os.path.join(root, f))

# Build mapping from gun_id to damage
gun_damage_map = {}

for file_path in gun_data_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if 'bullet' in data and 'damage' in data['bullet']:
            damage = data['bullet']['damage']
            bullet_amount = data['bullet'].get('bullet_amount', 1)

            # Extract namespace and gun name from path
            rel_path = os.path.relpath(file_path, base_path)
            parts = rel_path.split(os.sep)
            namespace = parts[0]
            gun_name = parts[5].replace('_data.json', '')

            # Map namespace to gun pack prefix
            if namespace == "tacz_default_gun":
                gun_id = "tacz:" + gun_name
            elif namespace == "TaCZ_-Expanded-Arsenal-v2.9":
                gun_id = "tacz:" + gun_name
            elif namespace == "Apocalypse_v1.1.7_G":
                gun_id = "bf1:" + gun_name
            elif namespace == "ChocolateMan V1.2.6a1-Public Edition":
                gun_id = "qkl:" + gun_name
            elif namespace == "Suffuse-GunSmoke-Pack1.0.7--hotfix":
                gun_id = "suffuse:" + gun_name
            elif namespace == "daffas":
                gun_id = "daffas_arsenal:" + gun_name
            elif namespace == "[Tacz1.1.8+]MS-Mobius Gunspack v1.5.8":
                inner_ns = parts[1]
                if inner_ns in ["msapl", "msskin", "sfms"]:
                    gun_id = "msapl:" + gun_name
                elif inner_ns == "erode":
                    gun_id = "erode:" + gun_name
                else:
                    gun_id = inner_ns + ":" + gun_name
            elif namespace == "[Tacz1.1.5+]EMX-Arms GunsPack ver1.1.5.zip":
                gun_id = "emxarms:" + gun_name
            elif namespace == "[Tacz1.1.5+]TRIS-dyna GunsPack ver1.1.5.zip":
                gun_id = "trisdyna:" + gun_name
            else:
                gun_id = namespace + ":" + gun_name

            gun_damage_map[gun_id] = {"damage": damage, "bullet_amount": bullet_amount}
    except Exception as e:
        print(f"Failed to parse {file_path}: {e}")

# Read CSV and add damage column
csv_path = os.path.join(base_path, "gun_index_tiered.csv")
rows = []

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

# Add new columns to header
header = rows[0] + ["bullet_damage", "bullet_amount"]
output_rows = [header]

# Process data rows
matched = 0
unmatched = 0
for row in rows[1:]:
    if not row or not row[0].strip():
        continue

    gun_id = row[2]  # gun_id is 3rd column (index 2)

    damage = ""
    amount = ""

    if gun_id in gun_damage_map:
        damage = gun_damage_map[gun_id]["damage"]
        amount = gun_damage_map[gun_id]["bullet_amount"]
        matched += 1
    else:
        # Try alternative mappings
        alt_ids = [gun_id]
        if gun_id.startswith("tacz:"):
            alt_ids.append(gun_id.replace("tacz:", "tacz_default_gun:"))
            alt_ids.append(gun_id.replace("tacz:", "TaCZ_-Expanded-Arsenal-v2.9:"))

        for alt_id in alt_ids:
            if alt_id in gun_damage_map:
                damage = gun_damage_map[alt_id]["damage"]
                amount = gun_damage_map[alt_id]["bullet_amount"]
                matched += 1
                break
        else:
            unmatched += 1

    output_rows.append(row + [str(damage), str(amount)])

# Write back
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_rows)

print(f"Done! Matched: {matched}, Unmatched: {unmatched}, Total processed: {len(output_rows) - 1}")