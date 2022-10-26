import argparse
import os
from configparser import ConfigParser

def args():

    ########## Parsing arguments ###########
    desc=''''''
    parser=argparse.ArgumentParser(description=desc)
    parser.add_argument('-lite',help='Run Lite mode.',action='store_true')
    parser.add_argument('-standalone',help='Run standalone mode.',action='store_true')
    parser.add_argument('-i',metavar='Input_File',help='Input your file here',dest='infile',required=True)
    parser.add_argument('-o',metavar='Output_File',help='Output file name',dest='outfile',required=True)
    parser.add_argument('-dh',help='Keep duplicate headers in FASTA file.',action='store_true')
    parser.add_argument('-tax',help='Search for taxonomy information for each sequence.',action='store_true')
    parser.add_argument('-name',help='Search for protein name for each sequence.',action='store_true')
    parser.add_argument('-dom',help='Search for domain information for each sequence in Entrenz database (no evalue and bit score).', action='store_true')
    parser.add_argument('-pfam',help='Run Pfamsacn (domain prediction) for each sequence.',action='store_true')
    parser.add_argument('-pev',metavar='PfamScan E-value',help='Spicify a e-value of Pfamscan search.',type=str)
    parser.add_argument('-pas',help='Enable active sites prediction in Pfamscan.',action='store_true')
    parser.add_argument('-em',metavar='Email address',help='Email address that you want receive potential information from web tools.',dest='email')
    parser.add_argument('-muscle',help='Run MUSCLE (multiple alignment).',action='store_true')
    parser.add_argument('-mafft',help='Run MAFFT (multiple alignment).',action='store_true')
    parser.add_argument('-matrix',metavar='MAFFT matrix type',help='Spicify a matrix type of MAFFT alignment.',type=str)
    parser.add_argument('-op',metavar='MAFFT opening score',help='Spicify a gap oppening penalty of MAFFT alignment.',type=float)
    parser.add_argument('-ep',metavar='MAFFT extension score',help='Spicify a gap extension penalty of MAFFT alignment.',type=float)
    parser.add_argument('-retree',metavar='MAFFT tree rebuilding number',help='Tree rebuilding number of MAFFT.',type=int)
    parser.add_argument('-maxiterate',metavar='MAFFT max iterate number',help='Max iterate number of MAFFT.',type=int)
    parser.add_argument('-ffts',metavar='MAFFT fast fourier transform algorithm',help='Mode of fast fourier transform.',type=str)
    parser.add_argument('-trimal',help='Run trimAl (multiple alignment trim).',action='store_true')
    parser.add_argument('-tmod',metavar='trimAl run mode',help='Run mode of trimAl.',type=str)
    parser.add_argument('-rmss',metavar='trimAl Residue overlap/Sequence overlap',help='Remove spurious sequences (residue overlap/sequence overlap). Overlap score between 0 to 1.',type=str)
    parser.add_argument('-iqtree',help='Run IQ-tree (tree building).',action='store_true')
    parser.add_argument('-iqmod',metavar='IQ-tree test mod',help='Test mod of IQ-tree.')
    # parser.add_argument('-alrt',metavar='IQ-tree SH-like test replicates (>=1000)',help='Number of replicates (>=1000) to perform SH-like approximate likelihood ratio test.',type=int)
    parser.add_argument('-boots',metavar='IQ-tree Bootstrap number',help='Bootstrap number of IQtree (must >= 1000).',type=int)
    parser.add_argument('-rcluster',metavar='Rcluster percentage',help='Rcluster percentage(0 to 100).',type=int)
    parser.add_argument('-mtree',help='Turn on full tree search for model testing of IQ-tree.',action='store_true')
    parser.add_argument('-bnni',help='Turn on additional optimize of IQ-tree.',action='store_true')
    parser.add_argument('-xzoom',metavar='Branch length scale',help='Value of X zoom(default=1, decimal possible).',type=float)
    parser.add_argument('-yzoom',metavar='Branch vertical margin',help='Value of Y zoom(default=1, decimal possible).',type=float)
    parser.add_argument('-bs',help='Show branch support in tree drawing.',action='store_true')
    parser.add_argument('-bl',help='Show branch length in tree drawing.',action='store_true')
    parser.add_argument('-bif',help='Show bifurcation number in tree drawing.',action='store_true')
    parser.add_argument('-leg',help='Generate domain legend.',action='store_true')
    parser.add_argument('-reroot',metavar='Reroot the tree',help='Reroot the tree according to bifurcation number.',type=int)
    parser.add_argument('-redo',help='Redo all processing',action='store_true')
    parser.add_argument('-format',metavar='Tree image format',help='Format of ETE3 output image.')
    args=parser.parse_args()
    ########################################

    # config file check
    if os.path.isdir(args.infile):
        cfg_path = args.infile + 'Congfig.ini'
    elif os.path.isfile(args.infile):
        cfg_path = '/'.join(args.infile.split('/')[:-1]) + '/Congfig.ini'

    if os.path.isfile(cfg_path):
        pass
    else:
        cfg_file = open('Config.ini','r') # ./standalone/
        cfg_content = cfg_file.read()
        new_cfg_file = open(cfg_path,'w')
        new_cfg_file.write(cfg_content)

    # output config log
    if not os.path.exists(args.outfile):
        os.makedirs(args.outfile)
    cfg_file = open(cfg_path,'r')
    cfg_content = cfg_file.read()
    new_path = args.outfile + 'Config.log'
    new_cfg_file = open(new_path,'w')
    new_cfg_file.write(cfg_content)

    # load config file
    cfg = ConfigParser()
    cfg.read(cfg_path)

    if not args.lite:
        args.lite = cfg.getboolean('General','run_mode_lite')
    if not args.standalone:
        args.standalone = cfg.getboolean('General','run_mode_standalone')
    if not args.dh:
        args.dh = cfg.getboolean('FASTA parser','keep_duplicate_headers')
    if not args.tax:
        args.ta = cfg.getboolean('FASTA parser','organism_lineage')
    if not args.name:
        args.name = cfg.getboolean('FASTA parser','protein_name_from_database')
    if not args.dom:
        args.dom = cfg.getboolean('FASTA parser','domain_from_database')
    if not args.pfam:
        args.pfam = cfg.getboolean('FASTA parser','pfamscan_search')
    if not args.pev:
        args.pev = cfg['FASTA parser']['E-value']
    if not args.pas:
        args.pas = cfg.getboolean('FASTA parser','active_sites')
    if not args.email:
        args.email = cfg['FASTA parser']['email'].replace('\'','')
    if not args.muscle:
        args.muscle = cfg.getboolean('Multiple Alignment','run_MUSCLE')
    if not args.mafft:
        args.mafft = cfg.getboolean('Multiple Alignment','run_MAFFT')
    if not args.matrix:
        args.matrix = cfg['Multiple Alignment']['MAFFT_matrix'].replace('\'','')
    if not args.op:
        args.op = cfg.getfloat('Multiple Alignment','MAFFT_gapopen')
    if not args.ep:
        args.ep = cfg.getfloat('Multiple Alignment','MAFFT_gapext')
    if not args.retree:
        args.retree = cfg.getint('Multiple Alignment','tree_rebuilding')
    if not args.maxiterate:
        args.maxiterate = cfg.getint('Multiple Alignment','max_iterate')
    if not args.ffts:
        args.ffts = cfg['Multiple Alignment']['perfrom_ffts'].replace('\'','')
    if not args.trimal:
        args.trimal = cfg.getboolean('Multiple Alignment','run_trimAl')
    if not args.tmod:
        args.tmod = cfg['Multiple Alignment']['auto_mode'].replace('\'','')
    if not args.rmss:
        args.rmss = cfg['Multiple Alignment']['remove_specious'].replace('\'','')
    if not args.iqtree:
        args.iqtree = cfg.getboolean('Tree Building','run_iqtree')
    if not args.iqmod:
        args.iqmod = cfg['Tree Building']['test_mod'].replace('\'','')
    # if not args.alrt:
    #     args.alrt = cfg.getint('Tree Building','SH_like_Test')
    if not args.boots:
        args.boots = cfg.getint('Tree Building','bootstrap_number')
    if not args.rcluster:
        args.rcluster = cfg.getint('Tree Building','rcluster')
    if not args.mtree:
        args.mtree = cfg.getboolean('Tree Building','full_tree_search')
    if not args.bnni:
        args.bnni = cfg.getboolean('Tree Building','additional_optimize')
    if not args.xzoom:
        args.xzoom = cfg.getint('Tree Visualizing','branch_length_scale')
    if not args.yzoom:
        args.yzoom = cfg.getint('Tree Visualizing','branch_separation_scale')
    if not args.bs:
        args.bs = cfg.getboolean('Tree Visualizing','show_branch_support')
    if not args.bl:
        args.bl = cfg.getboolean('Tree Visualizing','show_branch_length')
    if not args.bif:
        args.bif = cfg.getboolean('Tree Visualizing','show_bifurcation_number')
    if not args.leg:
        args.leg = cfg.getboolean('Tree Visualizing','motif_legend')
    if not args.format:
        args.format = cfg['Tree Visualizing']['format'].replace('\'','')

    args.color_list = eval(cfg['Tree Visualizing']['color_list'])

    return args

# args()