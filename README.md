# The PHA4GE QC Contextual Data Tags Specification

Standardized annotations for sharing public health sequence datasets with known quality issues to facilitate testing and training 

## Motivation

Public health pathogen genomic surveillance requires robust validation, training, and optimization of wet- and dry-lab procedures. In order to perform these processes, both high quality as well as lower-quality datasets are needed for comparisons. However, sharing of sub-optimal data requires its careful annotation with known issues to enable appropriate use, avoid its being mistaken for better quality information, and for it to be easily identifiable in repositories. 

![overview](https://i.imgur.com/t4lHvjw.png)
>Figure 1: Both high quality and lower quality datasets have many uses in public health activities such as personnel training and lab procedure/software optimization and validation in ideal and real-world scenarios. 

Unfortunately, there are currently no standardized attributes for tagging poor-quality datasets to maximize their utility, searchability, and accessibility. To address the challenges of annotating and identifying lower quality datasets, [PHA4GE](https://pha4ge.org) has developed a set of standardized contextual data tags (fields and terms) that can be included in public repository submissions as a means of identifying pathogen sequence data with known quality issues. Implementation of the tags in sequence records helps improve communication between submitters and data users, and increases the discoverability of lower quality datasets. 

Developed through consultations with the community including input from the International Nucleotide Sequence Data Collaboration (INSDC), the contextual data tags have been standardized using community-based resources known as ontologies. The standardized tags are organism-agnostic and sequencing technique-agnostic and can be applied to data generated from any pathogen using an array of sequencing techniques. Definitions, ontology IDs, and examples of use are provided, as well as a JSON representation. Suggestions for additional tags can be submitted to PHA4GE via the New Term Request Form. By providing a mechanism for feedback and suggestions, we also expect that the tags will evolve with the needs of the community.

## Content description

### QC Contextual Data Tags Specification

The [PHA4GE](https://pha4ge.org) Contextual Data QC Tag Specification provides a set of five fields which can be included as user-defined contextual data in public repository raw read sequence submissions. Two of the fields (“quality control determination” and “quality control issues”) have sets of prescribed values (Table 1).

> Table 1: Standardized fields and values for annotating quality control information in shared pathogen genomics datasets

| Field | Definition | Ontology ID | Data Type | Values | Example |
|---|---|---|---|---|---|
| quality control method name | The name of the method used to assess whether a sequence passed a predetermined quality control threshold. | GENEPIO:0100557 | String | No prescribed values | ncov-tools |
| quality control method version | The version number of the method used to assess whether a sequence passed a predetermined quality control threshold. | GENEPIO:0100558 | String | No prescribed values | 1.2.3 |
| quality control determination | The determination of a quality control assessment. | GENEPIO:0100559 | Enums | no quality control issues identified [GENEPIO:0100562]; sequence passed quality control [GENEPIO:0100563]; sequence failed quality control [GENEPIO:0100564]; minor quality control issues identified [GENEPIO:0100565]; sequence flagged for potential quality control issues [GENEPIO:0100566]; quality control not performed [GENEPIO:0100567] | sequence failed quality control [GENEPIO:0100564] |
| quality control issues | The reason contributing to, or causing, a low quality determination in a quality control assessment. | GENEPIO:0100560 | Enums | low quality sequence [GENEPIO:0100568]; sequenced contaminated [GENEPIO:0100569]; low average genome coverage [GENEPIO:0100570]; low percent genome captured [GENEPIO:0100571]; read lengths shorter than expected [GENEPIO:0100572]; sequence amplification artifacts [GENEPIO:0100573]; low signal to noise ratio [GENEPIO:0100574]; low coverage of characteristic mutations [GENEPIO:0100575] | low average genome coverage [GENEPIO:0100570] |
| quality control details | The details surrounding a low quality determination in a quality control assessment.   | GENEPIO:0100561 | String | No prescribed values | CT value of 39. Low viral load. Low DNA concentration after amplification. |

### Limitations and Considerations

1. The QC tags are intended to address an array of issues which may be more applicable to certain types of sequencing techniques. When certain tags are not appropriate then they should not be used. 
2. The tags are also meant to describe QC results of sequence data rather than downstream analytical results. 
3. The application of these attribute tags may be subjective and dependent on the QC processes performed. It is recommended that other information pertaining to QC be included in other contextual data fields not specified in this work (e.g. choice of reference genome) in order for users to better evaluate and interpret the QC determinations proposed. The tags should always be interpreted in light of the other methodological metadata included in the record (i.e. Experiment/SRA contextual data). 
4. The attributes are intended to flag issues rather than capture all methods in detail. Information affecting the selection of one tag over another can also be included in the “quality_control_details” field. 
5. Quality control tags refer to a particular sample obtained at one point in time, and not the comparison of a set of samples across time or from different tissues of the same host.

## Supporting Materials

### [QC Tag Specification Reference Guide](https://github.com/pha4ge/contextual_data_QC_tags/blob/main/PHA4GE%20QC%20Tag%20Reference%20Guide.xlsx)
Field and term definitions as well as guidance for use are available in the QC Tag Specification Reference Guide.

### [The QC Tag Specification in Machine-Amenable JSON Format](https://github.com/pha4ge/contextual_data_QC_tags/blob/main/QC_Contextual_Data_Tags_Specification.json)
The standardized fields and terms are available as a JSON representation for easier integration in applications. 

### [PHA4GE-modified SRA Submission Form](https://github.com/pha4ge/contextual_data_QC_tags/blob/main/PHA4GE_SRA_QC_Tag.xlsm)
To facilitate the inclusion of QC tags in NCBI submissions to the Sequence Read Archive (SRA), the fields and terms have been supplied as user-defined contextual data in this modified SRA submission form. The “quality control determination” and “quality control issues” fields provide drop-down menus with standardized values and multi-tagging with multiple values is enabled. Note: this file contains macros.

### [New Term Request Template](https://github.com/pha4ge/contextual_data_QC_tags/issues/new/choose)
To better keep standardized attributes aligned with the needs of the public health bioinformatics community, users can submit requests to PHA4GE for additional tags by submitting an issue via the [QC Tag repository IssueTracker](https://github.com/pha4ge/contextual_data_QC_tags/issues). Alternatively, new term requests can be emailed to `datastructures@pha4ge.org`.

Issues should be titled “NTR: [list term label(s)]” and should contain the following information.
* a. For new fields
  * Label (what you want the tag to be called): 
  * Definition/Description (what the tag should mean): 
  * Definition Source (reference, website): 
  * Synonyms or alternative labels (other ways someone might say the same thing): 
  * Additional Comments (not an annotation):

* b. For picklist additions
  * Associated Field(s) (which field the value should belong to): 
  * Parent Term (if the new term is a more specific version of a term already present): 
  * Label (what you want the tag to be called): 
  * Definition/Description (what the tag should mean): 
  * Definition Source (reference, website): 
  * Synonyms or alternative labels (other ways someone might say the same thing): 
  * Additional Comments (not an annotation):


## Contacts

For more information and/or assistance, contact `datastructures@pha4ge.org` or the issue page of this repository.

## License

[MIT License](https://github.com/pha4ge/contextual_data_QC_tags/blob/main/license)
