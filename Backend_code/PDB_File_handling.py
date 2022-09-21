from file_handles import *
from Bio import SeqIO

aas = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLU', 'GLN', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE',
       'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL']

aa_map_3_1 = {'ALA':'A', 'ARG':'R', 'ASN':'N', 'ASP':'D', 'CYS':'C', 'GLU':'E', 'GLN':'Q', 'GLY':'G', 'HIS':'H',
          'ILE':'I', 'LEU':'L', 'LYS':'K', 'MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S', 'THR':'T',
          'TRP':'W', 'TYR':'Y', 'VAL':'V'}

aa_map_1_3 = {'A': 'ALA', 'R': 'ARG', 'N': 'ASN', 'D': 'ASP', 'C': 'CYS', 'E': 'GLU', 'Q': 'GLN', 'G': 'GLY',
              'H': 'HIS', 'I': 'ILE', 'L': 'LEU', 'K': 'LYS', 'M': 'MET', 'F': 'PHE', 'P': 'PRO', 'S': 'SER',
              'T': 'THR', 'W': 'TRP', 'Y': 'TYR', 'V': 'VAL'}


sequence = dict()

for record in SeqIO.parse(sample_pdb_file, "pdb-seqres"):
    buffer = list()
    for aa in record.seq:
        buffer.append(aa_map_1_3[aa])

    sequence[record.id] = buffer