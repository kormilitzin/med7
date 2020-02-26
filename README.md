# Med7

This repository contains a trained model, compatible with [spaCy](https://spacy.io), for clinical named-entity recognition (NER) tasks. The `en_core_med7_lg` model is trained on MIMIC-III free-text electronic health records and is able to recognise 7 categories:


![Image description](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-26%20at%2018.18.54.png)

The trained model comprises three components in its pipeline:
* tagger
* parser
* clinical NER with seven categories.


TODO:
## Put example of NER with displacy and ent

## show metrics for each of categories and the number of tokens it is trained on

## Installation

Assuming you have the most recent version of spaCy (2.2.3) and Python 3.6+, the model can be easily installed by downloading from the direct link:

`pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg-0.0.1.tar.gz`


## Usage

```python
import spacy

med7 = spacy.load("en_core_med7_lg")

text = "A patient was prescribed Magnesium hydroxide 400mg/5ml suspension Sig: 30 ml for the next 5 days."
doc = med7(text)

[(ent.text, ent.label_) for ent in doc.ents]
```





