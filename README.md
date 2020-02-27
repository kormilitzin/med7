# Med7

This repository contains a trained model, compatible with [spaCy](https://spacy.io), for clinical named-entity recognition (NER) tasks. The `en_core_med7_lg` model is trained on MIMIC-III free-text electronic health records and is able to recognise 7 categories:


![Image description](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-26%20at%2018.18.54.png)

The trained model comprises three components in its pipeline:
* tagger
* parser
* clinical NER with seven categories.

Self-supervised pre-training has shown its efficientcy in achieving good results even with a small number of gold-annotated training data. We have experimented with the `spacy pretrain` approach and trained a number of weights for model initialisation for various parameters of the width and depth of convolutional layers. Following the notations of [spaCy pretrain](https://spacy.io/api/cli#pretrain) with `--width`, `--depth`, `--embed-rows` flags for width, depth and the number of embedding rows respectively:

| --width  | --depth | --embed-rows    |model size (MB) | epochs | URL      |
| --------:| -------:| -------------:  |--------------: |------: |-----:    |
| 96       |      4  |   10000         |      3.8       |    350 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_096_04_350.bin) |
| 128      |      8  |   10000         |      18.3      |    596 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_128_08_596.bin) |
| 256      |      8  |   10000         |      47.6      |    450 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_08_450.bin) |
| 256      |      16  |   10000         |     66.1      |    332 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_16_332.bin) |
| 300      |      8  |    20000       |       89.6      |    338 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_300_08_338.bin) |

The models were pre-trained on the entire MIMIC-III corpus, comprsing a collection of 2,083,054 documents with the total of 3,129,334,419 words. Models' losses (logarithmically scaled) are presented below:

![Image description](https://github.com/kormilitzin/med7/blob/master/images/myfile_1.pdf)



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

text = "A patient was prescribed Magnesium hydroxide 400mg/5ml suspension, Sig: 30 ml for the next 5 days."
doc = med7(text)

[(ent.text, ent.label_) for ent in doc.ents]
```

and the resulting output:

```
[('Magnesium hydroxide', 'DRUG'),
 ('400mg/5ml', 'STRENGTH'),
 ('suspension', 'FORM'),
 ('30 ml', 'DOSAGE'),
 ('for the next 5 days', 'DURATION')]
```


