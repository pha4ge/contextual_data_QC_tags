# The PHA4GE QC Contextual Data Tags Specification
How to tag and share public health sequence datasets with known quality issues for testing and training purposes

## Motivation

As public health laboratories expand their sequencing and bioinformatics capacity for the surveillance of different pathogens, labs must carry out robust optimization of wet and dry lab procedures. High quality as well as lower quality datasets are highly useful for testing and optimizing the performance of algorithms, pipelines and instruments, as well as training new personnel. Sharing of sub-optimal data is useful for the community, especially when the data is carefully annotated with known issues so that it is not mistaken for better quality information, and so that such datasets can be easily identified in repositories. 

(PHA4GE)[https://pha4ge.org/] has developed a set of standardized contextual data tags (fields and terms) that can be included in public repository submissions as a means of flagging pathogen sequence data with known quality issues to increase their discoverability. The standardized tags are organism-agnostic and sequencing technique-agnostic and can be applied to data generated from any pathogen using an array of sequencing techniques.

## PHA4GE overview

The Public Health Alliance for Genomic Epidemiology ([PHA4GE](https://pha4ge.org)) is a global coalition that is actively working to establish consensus standards, document and share best practices, improve the availability of critical bioinformatic tools and resources, and advocate for greater openness, interoperability, accessibility and reproducibility in public health microbial bioinformatics.

## Content description

### QC Contextual Data Tags Specification

Quality control metrics and thresholds often differ across laboratories and surveillance networks. While public health laboratories generate a vast number of high quality sequences, there will often be a proportion of datasets that may just fall just short of a set of prescribed baseline quality control metrics that are excluded from many types of public health analyses. In these cases, the issues associated with these borderline or lower quality datasets have been identified.

The set of fields include “quality_control_method_name”, “quality_control_method_version”, “quality_control_determination”, “quality_control_determination”, “quality_control_issues”, “quality_control_details”. Definitions, ontology IDs, and examples of use are provided as a JSON representation. The contextual data tags were developed through consultations with the community including input from the International Nucleotide Sequence Data Collaboration (INSDC), and standardized using community-based resources known as ontologies.

## Contacts

For more information and/or assistance, contact `datastructures@pha4ge.org` or the issue page of this repository.

## License

[MIT License](https://github.com/pha4ge/contextual_data_QC_tags/blob/main/license)
