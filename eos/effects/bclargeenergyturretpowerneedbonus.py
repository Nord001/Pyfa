# Used by:
# Ship: Oracle
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                     "power", ship.getModifiedItemAttr("bcLargeTurretPower"))
