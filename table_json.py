#!/usr/bin/env python

import argparse
import csv
import json
import re
from ast import literal_eval

FIELDNAMES = ['Field','Definition','Ontology ID','Data Type','Values','Example']
SEPARATOR = ';'
QUOTE = '"'

def string_list_to_list(string):
    to_list = [n.strip() for n in string.split(SEPARATOR)]
    return to_list

def interface_label_to_property_key(interface_label):
    property_key = re.sub(r'[^\w {}]', '_', interface_label).replace(' ', '_').replace('__', '_').lower()
    property_key = re.sub(r'_$', '', property_key)

    return property_key


def parse_properties_table(path_to_properties_table):
    datatype_map = {
        "String": "string",
        "Date": "string",
        "Int": "integer",
        "Float": "number",
        "Email": "string",
        "Bioproject_ID": "string",
        "Biosample_ID": "string",
        "SRA_ID": "string",
        "Genbank_ID": "string",
        "GISAID_ID": "string",
        "Enums":{
                "type": "string",
                "enum": "",
            },
        "Integer_or_Range": [
            {
                "type": "integer",
            },
            {
                "type": "string",
                "pattern": "\\d+-\\d+",
            }
        ],
    }

    format_map = {
        "String": None,
        "Date": "date",
        "Int": None,
        "Float": None,
        "Email": "email",
        "Bioproject_ID": None,
        "Biosample_ID": None,
        "SRA_ID": None,
        "Genbank_ID": None,
        "GISAID_ID": None,
        "Integer_or_Range": None,
        'Enums': None
    }

    pattern_map = {
        "String": None,
        "Date": None,
        "Int": None,
        "Float": None,
        "Email": None,
        "Bioproject_ID": "^PRJ(N|E|D)([a-zA-Z]?)[0-9]+*",
        "Biosample_ID": "^SAM(D|N|E([AG]?))[0-9]+",
        "SRA_ID": "^(SRR|ERR|DRR)[0-9]+",
        "Genbank_ID": "^([a-zA-Z]{2})\d*.\d{1}",
        "GISAID_ID": "^EPI_ISL_\d*",
        "Integer_or_Range": None,
        "Enums": None
    }

    properties = {}

    with open(path_to_properties_table) as f:
        reader = csv.DictReader(f,
                                delimiter=SEPARATOR,
                                quotechar=QUOTE)
        for row in reader:
            print(row)
            property_key = interface_label_to_property_key(row['Field'])
            properties[property_key] = {}
            properties[property_key]['description'] = row['Definition']
            properties[property_key]['ontology'] = row['Ontology ID']
            type = datatype_map[row['Data Type']]
            properties[property_key]['type'] = type
            format = format_map[row['Data Type']]
            if format:
                properties[property_key]['format'] = format
            pattern = pattern_map[row['Data Type']]
            if pattern:
                properties[property_key]['pattern'] = pattern
            examples = list(map(str.strip, row['Example'].split(';')))  # examples separated by semicolon
            for i in range(len(examples)):
                if properties[property_key]['type'] == 'integer':
                    examples[i] = int(examples[i])
                elif properties[property_key]['type'] == 'number':
                    examples[i] = float(examples[i])
            
            # Special case: enumns
            if row['Data Type'] == "Enums":
                type = datatype_map[row['Data Type']]
                properties[property_key]['type'] = "string"
                properties[property_key]['Enums'] = string_list_to_list(row['Values'])
            
            properties[property_key]['examples'] = examples

    return properties


def main(args):
    
    schema = {
        "$schema": "http://json-schema.org/draft/2019-09/schema#",
        "type": "object",
        "properties": {},
    }
    
    schema["properties"] = parse_properties_table(args.input)

    #print(json.dumps(schema))
    with open("QC_Contextual_Data_Tags_Specification.json", "w") as fh:
        fh.write(json.dumps(schema))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', help='Input schema attributes table')

    args = parser.parse_args()
    main(args)
