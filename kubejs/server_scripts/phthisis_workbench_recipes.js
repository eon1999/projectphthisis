// ===================================================================
// Project Phthisis - Tier 3 Gun Smith Table override
// ===================================================================
// tacz:gun_smith_table is the ONE real functional gun-crafting UI in
// the pack, and its default recipe is baked into the base tacz mod
// jar itself (data/tacz/recipes/gun_smith_table.json), not into any
// gunpack folder. That means it can't be edited in place like the
// other tier workbenches - it has to be removed and re-added here.
//
// Every other tier's workbench (Field Radio, Weapon Cases, Suffuse's
// table, MSETA, EMX-Arms/Skyline, TRIS) is a reskin the gunpacks
// already ship (tacz:workbench_a/b/c + a BlockId NBT tag), so those
// recipes live as native JSON files inside each gunpack's own
// data/<namespace>/recipes/block/ folder, right next to the gunpack's
// other content - not here.
// ===================================================================

ServerEvents.recipes(event => {

  // TIER 3 - TaCZ Gun Smith Table (Tac Default)
  // Gate: HV/Elite-tier precision machining - IE Steel Plates +
  // Graphite Electrode + Mekanism Elite Control Circuit + Refined
  // Obsidian.
  event.remove({ output: 'tacz:gun_smith_table' })

  event.shaped(
    'tacz:gun_smith_table',
    [
      'PPP',
      'GEG',
      'PRP'
    ],
    {
      P: 'immersiveengineering:plate_steel',
      G: 'immersiveengineering:graphite_electrode',
      E: 'mekanism:elite_control_circuit',
      R: 'mekanism:ingot_refined_obsidian'
    }
  )

})
