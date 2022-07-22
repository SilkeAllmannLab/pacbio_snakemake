# Pipeline configuration 

## General settings: `config.yaml` 

Set the desired parameters in the `config.yaml` file. 
- Directories,    
- CSV file used to link samples to PacBio subreads bam files,  
- Parameters for softwares of the PacBio Bioconda suite,
- Optionally, whether the assembled mRNA reads should be aligned to a genomic reference using Minimap2. Provides opportunity to modify default genome alignment parameters. 

For additional help on PacBio Bioconda tools, please visit the [dedicated website](https://github.com/PacificBiosciences/pbbioconda). 

## Sample spreadsheet

Add samples to `config/samples.csv`.   
For each sample, the columns `sample` and the `pacbio` have to be defined. 
The `sample` column should contain short simple sample names such as `Desiree` or `S81` for instance.   
The `pacbio` column should point to the path of the PacBio Iso-Seq for instance `subreads/mysample.subreads.bam`. Here the raw data for "mysample" is located in a folder called "subreads/".  

Missing values can be specified by empty columns or by writing `NA`.

## Primers used for library construction

After Circular Consensus Sequence (CSS) calling, full-length reads have to be detected. For this, the presence of a polyA tail  together with 5' and 3' primers have to be detected in the CSS read.  

The sequences of the 5' and 3' primers in FASTA format has to be available in `config/barcodes.fasta`.

⚠️ Primers have to be named `isoseq_5p` and `isoseq_3p` ⚠️  
Below is an example of the expected `barcodes.fasta` file.  
```
>isoseq_5p
GGCAATGAAGTCGCAGGGTTG
>isoseq_3p
GAAGCAGTGGTATCAACGCAGAG
```

## Genomic refs: `refs/`

An option is available to align the assembled mRNA isoforms to a genomic reference.   
To turn this option "on", verify that the value of the `map_to_genome:` option is set to `TRUE` in the `config.yaml` file.   
If genome mapping is turned "on", a genome reference assembly in FASTA format has to be present in `config/refs/`.  





