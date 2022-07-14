#!/usr/bin/env python3

import os
import pandas as pd

def sample_csv_to_pandas_df(path_to_sample_csv_file):
    '''
    Converts the .csv sample file (samples, PacBio subread bam files) to a Pandas dataframe
    
    Returns a Pandas dataframe with samples
    '''

    # Can csv file be imported as a Pandas df?
    try:
        sample_df = pd.read_csv(
            path_to_sample_csv_file, 
            index_col=0,
            sep=",",
            header=0
            ) 
    except FileNotFoundError:
        print(FileNotFoundError, "The ", path_to_sample_csv_file, "file does not exists. Please verify your sample file and its path")
    
    return sample_df

def verify_primer_names(barcode_fasta_file="config/barcodes.fasta"):
    '''
    Takes a FASTA file with two primer names and sequences (isoseq_5p and isoseq_3p)
    Returns TRUE if 
    '''
    # get primer sequences
    # Verify that it only contains two sequences
    with open(barcode_fasta_file) as filin:
        recs = [rec for rec in SeqIO.parse(filin, "fasta")]
    if len(recs) == 2:
        pass
    else:
        raise IndexError("Your FASTA file with barcode sequences should only contain two primers (5' and 3'). No more, no less") 
    
    # convert to a dictonary with id/sequence
    # verify primer names
    recs_dict = {rec.id: rec.seq for rec in recs}
    if "isoseq_5p" not in recs_dict.keys():
        raise KeyError("One primer has to be named exactly 'isoseq_5p")
    elif "isoseq_3p" not in recs_dict.keys():
        raise KeyError("One primer has to be named exactly 'isoseq_3p")
    else:
        pass