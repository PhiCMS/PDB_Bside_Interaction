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


# test for extracting continuous sequence sections
# here only the first interaction is checked for test reasons

single_as = active_side[list(active_side.keys())[0]]
test_out = dict()
counter = 1
buffer = list()

for i in range(len(single_as)):
    if i == 0:
        buffer.append(single_as[i][1])
        continue

    if single_as[i-1][0] + 1 == single_as[i][0]:
        buffer.append(single_as[i][1])

        if i == len(single_as)-1:
            test_out[counter+1] = buffer

    else:
        test_out[counter] = buffer
        counter += 1
        buffer = list()
        buffer.append(single_as[i][1])

