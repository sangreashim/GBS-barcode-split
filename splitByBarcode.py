#!/usr/bin/python

import sys
import os

fastq_file      = sys.argv[1]
barcode_file    = sys.argv[2]
prefix  = sys.argv[3]
unmatched       = sys.argv[4]
path_to_TrimingReads    = sys.argv[5]
barcode_length_dict     = {x.strip().split()[0]:str(len(x.strip().split()[1])) for x in open(barcode_file).readlines()}

os.system('zcat '+fastq_file+ ' | fastx_barcode_splitter.pl --bcfile '+barcode_file+' --suffix ".fq" --prefix '+prefix+'. --bol --exact')

for i in barcode_length_dict.keys():
        os.system(path_to_TrimingReads+'/TrimmingReads.pl -l '+ barcode_length_dict[i] +' -i '+prefix+'.'+i+'.fq')
