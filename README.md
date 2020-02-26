# med7

This repository contains trained models, compatible with spaCy, for clinical named-entity recognition (NER) tasks. The `en_core_med7_lg` models is trained on MIMIC-III free-text electronic health reacords and is able to recognise seven categories:


![Image description](https://github.com/kormilitzin/med7/blob/master/images/Screenshot%202020-02-26%20at%2018.18.54.png)

The trained model comprises three components in its pipeline:
* tagger
* parser
* clinical NER with seven categories.


