import os

# project root
ROOT_DIR = '/'.join(os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').split('/')[0:-1])

sample_data = ROOT_DIR + '/Sample_data'
sample_pdb_file = sample_data + '/6c7r.pdb'
sample_plip_file = sample_data + '/Plip_6C7R_report.xml'
sample_docking_file = sample_data + '/CHD_Docked_6C7R.pdb'
sample_docking_plip_file = sample_data + '/Plip_CHD_Docked_6C7R_Report.xml'

