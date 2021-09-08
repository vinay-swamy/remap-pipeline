import argparse


parser = argparse.ArgumentParser()



parser.add_argument('-b', '--bed', action='store', help='Path to the bed file')




args = parser.parse_args()

Error_input = argparse.ArgumentTypeError('input file necessary')



if args.bed is None:

    bed = "remap2022_nr-ecotype_macs2_TAIR10_v1_0.bed"

else:

    bed = args.bed


dict_biotype = {}
with open(bed, 'r') as f:

    for line in f:
        list_biotype = line.rstrip().split('\t')[3].split(':')[1].split(',')
        for biotype in list_biotype:
            if biotype in dict_biotype.keys():
                dict_biotype[biotype].write(line.rstrip() + '\n')
            else:
                dict_biotype[biotype] = open('9.bed/ECOTYPE_BIOTYPE/' +biotype+'/remap2022_'+ biotype+'_nr_macs2_TAIR10_v1_0.bed', 'w')
                dict_biotype[biotype].write(line.rstrip() + '\n')

