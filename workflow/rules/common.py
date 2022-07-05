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

def get_subread_file(wildcards):
    subread_bam_file = sample_df.loc[(wildcards.sample), "pacbio"]
    return subread_bam_file