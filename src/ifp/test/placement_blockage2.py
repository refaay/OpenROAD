import openroad as ord
import odb
from openroad import Tech, Design
import helpers

tech = Tech()
tech.readLef("Nangate45/Nangate45.lef")
tech.readLiberty("Nangate45/Nangate45_typ.lib")

design = Design(tech)
design.readVerilog("reg1.v")
design.link("top")

odb.dbBlockage_create(ord.get_db_block(), 0, 0, 2000000, 208400)

floorplan = design.getFloorplan()
floorplan.initFloorplan(helpers.make_rect(design, 0, 0, 1000, 1000),
                        helpers.make_rect(design, 100, 100, 900, 900))

def_file = helpers.make_result_file("placement_blockage2.def")
design.writeDef(def_file)
helpers.diff_files('placement_blockage2.defok', def_file)
