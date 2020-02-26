# Med7

This repository contains a trained model, compatible with [spaCy](https://spacy.io), for clinical named-entity recognition (NER) tasks. The `en_core_med7_lg` model is trained on MIMIC-III free-text electronic health records and is able to recognise 7 categories:


![Image description](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-26%20at%2018.18.54.png)

The trained model comprises three components in its pipeline:
* tagger
* parser
* clinical NER with seven categories.


## Installation

Assuming, spaCy is installed and you have Python 3.6+, the model can be easily install by using the direct link:

`pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg-0.0.1.tar.gz`



