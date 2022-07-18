# Snakemake workflow: PacBio Iso-Seq processing pipeline

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/<owner>/<repo>/workflows/Tests/badge.svg?branch=main)](https://github.com/<owner>/<repo>/actions?query=branch%3Amain+workflow%3ATests)


# Introduction 

A Snakemake workflow for processing PacBio raw `subreads.bam` into polished mRNA isoforms in FASTA format.  
Optionnally, long assembled mRNAs can be aligned against a genomic reference to generate a genomic annotation in the GFF3 format. 

## Steps
The workflow follows Iso-Seq standard analysis that consists of the following steps:  
1. Get **Circular Consensus Sequence (CCS) reads**.  
2. Get **Full Length (FL) reads**.   
3. Get **refined Full-Length, Non-Concatemer (FLNC) reads**.  
4. Get **transcript isoforms from (refined and clustered) FLNC reads**.    
5. Optionally, align these transcript isoforms to a genome reference and create a GFF3 annotation file.

## PacBio Iso-Seq terminology

| name                           | abbreviation 	| explanation  | |-----------------------------------	|--------------	|------------------------------------------------------------------------------------------------	|
| Full-Length Reads                 	| FL reads     	| CCS reads with 5’ and 3’ cDNA primers removed.  |
| Full-Length, Non-Concatemer Reads 	| FLNC reads   	| Reads FLNC Reads CCS reads with 5’ and 3’ cDNA primers, polyA tail, and concatemers removed. 	|
| High-Quality Isoforms             	| HQ isoforms  	| Polished transcript sequences with predicted accuracy ≥99% & ≥2 FLNC                  |
| Low-Quality Isoforms              	| LQ isoforms  	| Polished transcript sequences with predicted accuracy <99% & ≥2   FLNC                  |


# Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog?usage=SilkeAllmannLab/pacbio_snakemake) and also here. 

If you use this workflow in a paper, don't forget to give credits to the authors by citing the URL of this (original) repository and its DOI (see above).

## Install conda and mamba

For each rule, a dedicated Conda/Mamba environment 
On the crunchomics cluster, 

To install the 'conda' package manager from the lightweight miniconda distribution, follow instructions [here](https://docs.conda.io/en/latest/miniconda.html).   

To install the `mamba` package manager, follow the instructions [here](https://mamba.readthedocs.io/en/latest/installation.html).

## Create a ''snakemake' environment

This will be your starting environment with:
- [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html) version 7.0.1
- [Pandas](https://pandas.pydata.org/) version 1.4.3.
- [Biopython](https://biopython.org/) version 1.79.

To create it, run `mamba env create -f config/environment.yaml` to install these three Python dependencies. 

## Run Snakemake with conda

Snakemake will use the rule conda environments defined in `envs/` for each given rule. It will install the conda environment using `mamba` so be sure `mamba` is available by running either `which mamba`. 

If using Snakemake interactively execute: `snakemake --use-conda -j X` where X is your number of cores.   
Otherwise submit your jobs using SLURM job manager: `sbatch pacbio_snakemake_sbatch.sh`.

# Pipeline maintainers

- Tijs Bliek, technician, Plant Development and Epigenetics, SILS, University of Amsterdam.    
- Marc Galland, support data scientist, Plant Physiology, SILS, University of Amsterdam.  

# References 

## PacBio conda tools

[https://github.com/PacificBiosciences/pbbioconda](https://github.com/PacificBiosciences/pbbioconda)

## PacBio Iso-Seq workflow

- [A nice Iso-Seq tutorial to follow](https://databeauty.com/blog/tutorial/2020/12/08/PacBio-Iso-Seq-Data-Analysis.html)
- [UC Davis Bioinformatics Core Iso-Seq workflow](https://ucdavis-bioinformatics-training.github.io/2020-september-isoseq/liz/bioconda/2-bioconda)

# TODO

* Replace `<owner>` and `<repo>` everywhere in the template (also under .github/workflows) with the correct `<repo>` name and owning user or organization.
* Replace `<name>` with the workflow name (can be the same as `<repo>`).
* Replace `<description>` with a description of what the workflow does.
* The workflow will occur in the snakemake-workflow-catalog once it has been made public. Then the link under "Usage" will point to the usage instructions if `<owner>` and `<repo>` were correctly set.