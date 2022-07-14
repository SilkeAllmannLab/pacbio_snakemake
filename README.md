# Snakemake workflow: PacBio Iso-Seq processing pipeline

[![Snakemake](https://img.shields.io/badge/snakemake-≥6.3.0-brightgreen.svg)](https://snakemake.github.io)
[![GitHub actions status](https://github.com/<owner>/<repo>/workflows/Tests/badge.svg?branch=main)](https://github.com/<owner>/<repo>/actions?query=branch%3Amain+workflow%3ATests)


A Snakemake workflow for processing PacBio raw `subreads.bam` into polished mRNA isoforms in FASTA format.  
Optionnally, long assembled mRNAs can be aligned against a genomic reference to generate a genomic annotation in the GFF3 format. 

## Steps
The workflow follows Iso-Seq standard analysis that consists of the following steps:  
1. **Circular Consensus Sequence (CCS) reads** call: aligning subreads to each other from a single Zero-mode Waveguide (ZMW).     
2. **Full Length Non Chimeric (FLNC) reads** call: identify flnc CSS reads with a polyA tail and 5'/3' primers. Removes polyA tail and primers.   
3. **Refine FLNC reads**: 
4. **Cluster FLNC reads**


# Usage

The usage of this workflow is described in the [Snakemake Workflow Catalog](https://snakemake.github.io/snakemake-workflow-catalog?usage=SilkeAllmannLab/pacbio_snakemake).  

If you use this workflow in a paper, don't forget to give credits to the authors by citing the URL of this (original) repository and its DOI (see above).

## Install conda and mamba

For each rule, a dedicated Conda/Mamba environment 
On the crunchomics cluster, 

To install the 'conda' package manager from the lightweight miniconda distribution, follow instructions [here](https://docs.conda.io/en/latest/miniconda.html). 
To install the `mamba` package manager, follow the instructions [here](https://mamba.readthedocs.io/en/latest/installation.html).

## Run Snakemake with conda

Using 

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