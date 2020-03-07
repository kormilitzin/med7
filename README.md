# Med7

This repository dedicated to the first release of [Med7: a transferable clinical natural language processing model for electronic health records](https://arxiv.org/abs/2003.01271), compatible with [spaCy](https://spacy.io), for clinical named-entity recognition (NER) tasks. The `en_core_med7_lg` model is trained on MIMIC-III free-text electronic health records and is able to recognise 7 categories:


![Image description](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-26%20at%2018.18.54.png)

The trained model comprises three components in its pipeline:
* tagger
* parser
* clinical NER with seven categories.

Self-supervised pre-training has shown its efficiency in achieving good results even with a small number of gold-annotated training data. We have experimented with the `spacy pretrain` approach and trained a number of weights for model initialisation for various parameters of the width and depth of convolutional layers. Following the notations of [spaCy pretrain](https://spacy.io/api/cli#pretrain) with `--width`, `--depth`, `--embed-rows` flags for width, depth and the number of embedding rows respectively:

| --width  | --depth | --embed-rows    |model size (MB) | epochs | URL      |
| --------:| -------:| -------------:  |--------------: |------: |-----:    |
| 96       |      4  |   10000         |      3.8       |    350 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_096_04_350.bin) |
| 128      |      8  |   10000         |      18.3      |    596 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_128_08_596.bin) |
| 256      |      8  |   10000         |      47.6      |    450 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_08_450.bin) |
| 256      |      16  |   10000         |     66.1      |    332 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_256_16_332.bin) |
| 300      |      8  |    20000       |       89.6      |    338 | [Link](https://med7.s3.eu-west-2.amazonaws.com/t2v/model_300_08_338.bin) |

The models were pre-trained on the entire MIMIC-III data, comprising a collection of 2,083,054 documents with the total of 3,129,334,419 words. Models' losses (logarithmically scaled) are presented below:


<img src="https://github.com/kormilitzin/med7/blob/master/images/myfile_1-1.png" width="350">

The model achieved a lenient (strict) micro-averaged F1 score of 0.957 (0.893) across all seven categories.

## Installation

It is recommended to create a dedicated virtual environment and install all recent required packages in there. The trained model was tested with spaCy version 2.2.3 and Python 3.7. For example, if the [anaconda distribution of Python](https://www.anaconda.com/distribution/#download-section) is already installed:

create a new virtual environment:

`(base) conda create -n med7 python=3.7`

activate and install spaCy:

```
(base) conda activate med7

(med7) pip install -U spacy
```

once all went through smoothly, install the Med7 model:

`(med) pip install https://med7.s3.eu-west-2.amazonaws.com/en_core_med7_lg.tar.gz`

## Usage

```python
import spacy

med7 = spacy.load("en_core_med7_lg")

# create distinct colours for labels
col_dict = {}
seven_colours = ['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
for label, colour in zip(med7.pipe_labels['ner'], seven_colours):
    col_dict[label] = colour

options = {'ents': med7.pipe_labels['ner'], 'colors':col_dict}

text = 'A patient was prescribed Magnesium hydroxide 400mg/5ml suspension PO of total 30ml bid for the next 5 days.'
doc = med7(text)

spacy.displacy.render(doc, style='ent', jupyter=True, options=options)

[(ent.text, ent.label_) for ent in doc.ents]
```

The Med7 model identifies correctly all seven entities in the following example and highlights them in different colours for better visualisation:

![](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-27%20at%2013.42.04.png)


and the resulting output:

```
[('Magnesium hydroxide', 'DRUG'),
 ('400mg/5ml', 'STRENGTH'),
 ('suspension', 'FORM'),
 ('PO', 'ROUTE'),
 ('30ml', 'DOSAGE'),
 ('bid', 'FREQUENCY'),
 ('for the next 5 days', 'DURATION')]
```

It is straightforward to extract relations between the entities, since Med7 has both `parser` and `tagger` pipelines, similar to [this example.](https://github.com/explosion/spaCy/blob/master/examples/information_extraction/entity_relations.py)

<!---The fact that the trained Med7 model comprises both, the `tagger` and `parser` components, it is possible to find relationships among the entities, [inspired by this example.](https://github.com/explosion/spaCy/blob/master/examples/information_extraction/entity_relations.py) A very simple example:--->






The code in above can also be run in [Colab](https://colab.research.google.com/drive/1mY36G-vzBc_x4DGAYfyeb0OLIUcRMgff)




## Citing

This model is the very first step in our programme on clinical NLP for electronic health records (cNLPEHR). We are committed to developing FAIR - Findable, Accessible, Interoperable and Reusable tools which will benefit the wider community. 

If you found this model useful, please acknowledge by citing as:

```
@article{kormilitzin2020med7,
  title={Med7: a transferable clinical natural language processing model for electronic health records},
  author={Kormilitzin, Andrey and Vaci, Nemanja and Liu, Qiang and Nevado-Holgado, Alejo},
  journal={arXiv preprint arXiv:2003.01271},
  year={2020}
}
```




	
