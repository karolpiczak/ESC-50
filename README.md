[![GitHub license](https://img.shields.io/badge/license-CC%20BY--NC%203.0-blue.svg)](LICENSE)
[![CircleCI](https://circleci.com/gh/karoldvl/ESC-50.svg?style=svg)](https://circleci.com/gh/karoldvl/ESC-50)

## ESC-50: Dataset for Environmental Sound Classification

### Overview

<img src="esc50.gif" alt="ESC-50 clip preview" title="ESC-50 clip preview" align="right" />

The **ESC-50 dataset** is a labeled collection of 2000 environmental recordings suitable as a benchmark environmental sound classification task.

The dataset consists of 50 classes of 5-second-long recordings (40 examples per class) arranged in 5 major categories:

|  | <sub>Animals</sub> | <sub>Natural soundscapes & water sounds </sub> | <sub>Human, non-speech sounds</sub> | <sub>Interior/domestic sounds</sub> | <sub>Exterior/urban noises</sub> |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <sub>1.</sub>| <sub>Dog</sub> | <sub>Rain</sub> | <sub>Crying baby</sub> | <sub>Door knock</sub> | <sub>Helicopter</sub></sub> |
| <sub>2.</sub> | <sub>Rooster</sub> | <sub>Sea waves</sub> | <sub>Sneezing</sub> | <sub>Mouse click</sub> | <sub>Chainsaw</sub> |
| <sub>3.</sub> | <sub>Pig</sub> | <sub>Crackling fire</sub> | <sub>Clapping</sub> | <sub>Keyboard typing</sub> | <sub>Siren</sub> |
| <sub>4.</sub> | <sub>Cow</sub> | <sub>Crickets</sub> | <sub>Breathing</sub> | <sub>Door, wood creaks</sub> | <sub>Car horn</sub> |
| <sub>5.</sub> | <sub>Frog</sub> | <sub>Chirping birds</sub> | <sub>Coughing</sub> | <sub>Can opening</sub> | <sub>Engine</sub> |
| <sub>6.</sub> | <sub>Cat</sub> | <sub>Water drops</sub> | <sub>Footsteps</sub> | <sub>Washing machine</sub> | <sub>Train</sub> |
| <sub>7.</sub> | <sub>Hen</sub> | <sub>Wind</sub> | <sub>Laughing</sub> | <sub>Vacuum cleaner</sub> | <sub>Church bells</sub> |
| <sub>8.</sub> | <sub>Insects (flying)</sub> | <sub>Pouring water</sub> | <sub>Brushing teeth</sub> | <sub>Clock alarm</sub> | <sub>Airplane</sub> |
| <sub>9.</sub> | <sub>Sheep</sub> | <sub>Toilet flush</sub> | <sub>Snoring</sub> | <sub>Clock tick</sub> | <sub>Fireworks</sub> |
  | <sub>10.</sub> | <sub>Crow</sub> | <sub>Thunderstorm</sub> | <sub>Drinking, sipping</sub> | <sub>Glass breaking</sub> | <sub>Hand saw</sub> |

Clips in this dataset have been manually extracted from public field recordings gathered by the **[Freesound.org project](http://freesound.org/)**. The dataset has been prearranged into 5 folds for comparable cross-validation, making sure that fragments from the same original source file are contained in a single fold.

A more thorough description of the dataset is available in the original [paper](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf) with some supplementary materials - **[ESC: Dataset for Environmental Sound Classification - paper replication data](https://github.com/karoldvl/paper-2015-esc-dataset)**.

### Download

The dataset can be downloaded as a single .zip file (~600 MB):

**[Download ESC-50 dataset](https://github.com/karoldvl/ESC-50/archive/master.zip)**

### License

The dataset is available under the terms of the [Creative Commons Attribution Non-Commercial license](http://creativecommons.org/licenses/by-nc/3.0/).

A smaller subset (clips tagged as *ESC-10*) is distributed under CC BY (Attribution).

Attributions for each clip are available in the [ LICENSE file](https://raw.githubusercontent.com/karoldvl/ESC-50/master/LICENSE).

### Citing

If you find this dataset useful in an academic setting please cite:

> K. J. Piczak. **ESC: Dataset for Environmental Sound Classification**. *Proceedings of the 23rd Annual ACM Conference on Multimedia*, Brisbane, Australia, 2015.

> [DOI: http://dx.doi.org/10.1145/2733373.2806390]

### Caveats

Please be aware of potential information leakage while training models on *ESC-50*, as some of the original Freesound recordings were already preprocessed in a manner that might be class dependent (mostly bandlimiting). Unfortunately, this issue went unnoticed when creating the original version of the dataset. Due to the number of methods evaluated on*ESC-50* that have already been published, no changes rectifying this issue will be made in order to preserve comparability.
