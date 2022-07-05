# Pipeline configuration 

## Pipeline parameters: `config.yaml` 

Set the desired parameters in this file. 
- Directories,    
- CSV file used to link samples to PacBio subreads bam files,  
- Parameters for softwares of the PacBio Bioconda suite,
- Optionally, whether the assembled mRNA reads should be aligned to a genomic reference using Minimap2. Provides opportunity to modify default genome alignment parameters. 

## Primers used for library construction

After Circular Consensus Sequence (CSS) calling, full-length reads have to be detected. For this, the presence of a polyA tail  5' and 3' primers used to build the library for Iso-Seq sequencing. 

The sequences of the 5' and 3' primers in FASTA format has to be available in `config/primers.fasta`.

## Genomic refs: `refs/`

An option is available to align the assembled mRNA isoforms to a genomic reference. If that option is turned "on" (in the `config.yaml` file), a genome reference assembly in FASTA format has to be present in `config/refs/`.  





