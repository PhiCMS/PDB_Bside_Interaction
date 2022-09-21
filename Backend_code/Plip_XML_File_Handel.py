from PLIP_XML_Functions import *
from file_handles import *

# sampel files
plip_file = sample_plip_file
plip_docking_file = sample_docking_plip_file

# input plip xml to the Plip functions object
plipxml = PlipXML(plip_file)

bsides = dict()

# Keys = interactions as Lig:Chain:Pos
# valies --> Sorted list of tuples
active_side = dict()

for side in plipxml.bsites:

    # search for current interaction only once in loop
    current_interaction = plipxml.bsites[side].bs_res
    # save to collect (maybe not useful)
    bsides[side] = current_interaction

    buffer = list()
    for res in current_interaction:
        active_side[side] = list()
        buffer.append((res['resnr'], res['aa']))
    buffer.sort()
    active_side[side] = buffer
