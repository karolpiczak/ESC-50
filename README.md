## ESC-50: Dataset for Environmental Sound Classification

> ###### [Overview](#esc-50-dataset-for-environmental-sound-classification) | [Download](#download) | [Results](#results) | [Repository content](#repository-content) | [License](#license) | [Citing](#citing) | [Caveats](#caveats) | [Changelog](#changelog)
>
> <a href="https://circleci.com/gh/karoldvl/ESC-50"><img src="https://circleci.com/gh/karoldvl/ESC-50.svg?style=svg" /></a>&nbsp;
<a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC-blue.svg" />&nbsp;
<a href="https://github.com/karoldvl/ESC-50/archive/master.zip"><img src="https://img.shields.io/badge/download-.zip-ff69b4.svg" alt="Download" /></a>&nbsp;

<img src="esc50.gif" alt="ESC-50 clip preview" title="ESC-50 clip preview" align="right" />

The **ESC-50 dataset** is a labeled collection of 2000 environmental audio recordings suitable for benchmarking methods of environmental sound classification.

The dataset consists of 5-second-long recordings organized into 50 semantical classes (with 40 examples per class) loosely arranged into 5 major categories:

| <sub>Animals</sub> | <sub>Natural soundscapes & water sounds </sub> | <sub>Human, non-speech sounds</sub> | <sub>Interior/domestic sounds</sub> | <sub>Exterior/urban noises</sub> |
| :--- | :--- | :--- | :--- | :--- |
| <sub>Dog</sub> | <sub>Rain</sub> | <sub>Crying baby</sub> | <sub>Door knock</sub> | <sub>Helicopter</sub></sub> |
| <sub>Rooster</sub> | <sub>Sea waves</sub> | <sub>Sneezing</sub> | <sub>Mouse click</sub> | <sub>Chainsaw</sub> |
| <sub>Pig</sub> | <sub>Crackling fire</sub> | <sub>Clapping</sub> | <sub>Keyboard typing</sub> | <sub>Siren</sub> |
| <sub>Cow</sub> | <sub>Crickets</sub> | <sub>Breathing</sub> | <sub>Door, wood creaks</sub> | <sub>Car horn</sub> |
| <sub>Frog</sub> | <sub>Chirping birds</sub> | <sub>Coughing</sub> | <sub>Can opening</sub> | <sub>Engine</sub> |
| <sub>Cat</sub> | <sub>Water drops</sub> | <sub>Footsteps</sub> | <sub>Washing machine</sub> | <sub>Train</sub> |
| <sub>Hen</sub> | <sub>Wind</sub> | <sub>Laughing</sub> | <sub>Vacuum cleaner</sub> | <sub>Church bells</sub> |
| <sub>Insects (flying)</sub> | <sub>Pouring water</sub> | <sub>Brushing teeth</sub> | <sub>Clock alarm</sub> | <sub>Airplane</sub> |
| <sub>Sheep</sub> | <sub>Toilet flush</sub> | <sub>Snoring</sub> | <sub>Clock tick</sub> | <sub>Fireworks</sub> |
| <sub>Crow</sub> | <sub>Thunderstorm</sub> | <sub>Drinking, sipping</sub> | <sub>Glass breaking</sub> | <sub>Hand saw</sub> |

Clips in this dataset have been manually extracted from public field recordings gathered by the **[Freesound.org project](http://freesound.org/)**. The dataset has been prearranged into 5 folds for comparable cross-validation, making sure that fragments from the same original source file are contained in a single fold.

A more thorough description of the dataset is available in the original [paper](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf) with some supplementary materials on GitHub: **[ESC: Dataset for Environmental Sound Classification - paper replication data](https://github.com/karoldvl/paper-2015-esc-dataset)**.


## Download

The dataset can be downloaded as a single .zip file (~600 MB):

**[Download ESC-50 dataset](https://github.com/karoldvl/ESC-50/archive/master.zip)**


## Results

Numerous machine learning & signal processing approaches have been evaluated on the ESC-50 dataset. Most of them are listed here. If you know of some other reference, you can message me or open a Pull Request directly.

> ###### Terms used in the table:
> 
> <sub>• CNN - Convolutional Neural Network<br />• CRNN - Convolutional Recurrent Neural Network<br />• GMM - Gaussian Mixture Model<br />• GTCC - Gammatone Cepstral Coefficients<br />• GTSC - Gammatone Spectral Coefficients<br />• k-NN - k-Neareast Neighbors<br />• MFCC - Mel-Frequency Cepstral Coefficients<br />• MLP - Multi-Layer Perceptron<br />• RBM - Restricted Boltzmann Machine<br />• RNN - Recurrent Neural Network<br />• SVM - Support Vector Machine<br />• TEO - Teager Energy Operator<br />• ZCR - Zero-Crossing Rate</sub>

| <sub>Title</sub> | <sub>Notes</sub> | <sub>Accuracy</sub> | <sub>Paper</sub> | <sub>Code</sub> |
| :--- | :--- | :--- | :--- | :--- |
| <sub>**AST: Audio Spectrogram Transformer**</sub> | <sub>Pure Attention Model Pretrained on AudioSet</sub> | <sub>95.70%</sub> | <sub>[gong2021](https://arxiv.org/pdf/2104.01778.pdf)</sub> | <a href="https://github.com/YuanGongND/ast">:scroll:</a> |
| <sub>**A Sequential Self Teaching Approach for Improving Generalization in Sound Event Recognition**</sub> | <sub>Multi-stage sequential learning with knowledge transfer from Audioset</sub> | <sub>94.10%</sub> | <sub>[kumar2020](https://arxiv.org/pdf/2007.00144.pdf)</sub> |  |
| <sub>**Efficient End-to-End Audio Embeddings Generation for Audio Classification on Target Applications**</sub> | <sub>CNN model pretrained on AudioSet</sub> | <sub>92.32%</sub> | <sub>[lopez-meyer2021](https://ieeexplore.ieee.org/document/9414229)</sub> |  |
| <sub>**Urban Sound Tagging using Multi-Channel Audio Feature with Convolutional Neural Networks**</sub> | <sub>Pretrained model with multi-channel features</sub> | <sub>89.50%</sub> | <sub>[kim2020](http://dcase.community/documents/challenge2020/technical_reports/DCASE2020_JHKim_21_t5.pdf)</sub> | <a href="https://github.com/JaehunKim-DeepLearning/Dcase2020_Task5">:scroll:</a> |
| <sub>**An Ensemble of Convolutional Neural Networks for Audio Classification**</sub> | <sub>CNN ensemble with data augmentation</sub> | <sub>88.65%</sub> | <sub>[nanni2020](https://arxiv.org/pdf/2007.07966.pdf)</sub> | <a href="https://github.com/LorisNanni/Ensemble-of-Convolutional-Neural-Networks-for-Bioimage-Classification">:scroll:</a> |
| <sub>**Environmental Sound Classification on the Edge: A Pipeline for Deep Acoustic Networks on Extremely Resource-Constrained Devices**</sub> | <sub>CNN model (ACDNet) with potential compression</sub> | <sub>87.1%</sub> | <sub>[mohaimenuzzaman2021](https://arxiv.org/pdf/2103.03483.pdf)</sub> | <a href="https://anonymous.4open.science/r/71077d05-6666-43a7-ae73-ec5ce2bef91b/">:scroll:</a> |
| <sub>**Unsupervised Filterbank Learning Using Convolutional Restricted Boltzmann Machine for Environmental Sound Classification**</sub> | <sub>CNN with filterbanks learned using convolutional RBM + fusion with GTSC and mel energies</sub> | <sub>86.50%</sub> | <sub>[sailor2017](https://pdfs.semanticscholar.org/f6fd/1be38a2d764d900b11b382a379efe88b3ed6.pdf)</sub> |  |
| <sub>**AclNet: efficient end-to-end audio classification CNN**</sub> | <sub>CNN with mixup and data augmentation</sub> | <sub>85.65%</sub> | <sub>[huang2018](https://arxiv.org/pdf/1811.06669.pdf)</sub> |  |
| <sub>**On Open-Set Classification with L3-Net Embeddings for Machine Listening Applications**</sub> | <sub>x-vector network with openll3 embeddings</sub> | <sub>85.00%</sub> | <sub>[wilkinghoff2020](https://www.eurasip.org/Proceedings/Eusipco/Eusipco2020/pdfs/0000800.pdf)</sub> |  |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>EnvNet-v2 ([tokozume2017a](http://www.mi.t.u-tokyo.ac.jp/assets/publication/LEARNING_ENVIRONMENTAL_SOUNDS_WITH_END-TO-END_CONVOLUTIONAL_NEURAL_NETWORK-poster.pdf)) + data augmentation + Between-Class learning</sub> | <sub>84.90%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Novel Phase Encoded Mel Filterbank Energies for Environmental Sound Classification**</sub> | <sub>CNN working with phase encoded mel filterbank energies (PEFBEs), fusion with Mel energies</sub> | <sub>84.15%</sub> | <sub>[tak2017](https://www.researchgate.net/profile/Dharmesh_Agrawal/publication/320733074_Novel_Phase_Encoded_Mel_Filterbank_Energies_for_Environmental_Sound_Classification/links/5a084c780f7e9b68229c8947/Novel-Phase-Encoded-Mel-Filterbank-Energies-for-Environmental-Sound-Classification.pdf)</sub> |  |
| <sub>**Knowledge Transfer from Weakly Labeled Audio using Convolutional Neural Network for Sound Events and Scenes**</sub> | <sub>CNN pretrained on AudioSet</sub> | <sub>83.50%</sub> | <sub>[kumar2017](https://arxiv.org/pdf/1711.01369.pdf)</sub> | <a href="https://github.com/anuragkr90/weak_feature_extractor">:scroll:</a> |
| <sub>**Unsupervised Filterbank Learning Using Convolutional Restricted Boltzmann Machine for Environmental Sound Classification**</sub> | <sub>CNN with filterbanks learned using convolutional RBM + fusion with GTSC</sub> | <sub>83.00%</sub> | <sub>[sailor2017](https://pdfs.semanticscholar.org/f6fd/1be38a2d764d900b11b382a379efe88b3ed6.pdf)</sub> |  |
| <sub>**Deep Multimodal Clustering for Unsupervised Audiovisual Learning**</sub> | <sub>CNN + unsupervised audio-visual learning</sub> | <sub>82.60%</sub> | <sub>[hu2019](http://openaccess.thecvf.com/content_CVPR_2019/papers/Hu_Deep_Multimodal_Clustering_for_Unsupervised_Audiovisual_Learning_CVPR_2019_paper.pdf)</sub> |  |
| <sub>**Novel TEO-based Gammatone Features for Environmental Sound Classification**</sub> | <sub>Fusion of GTSC & TEO-GTSC with CNN</sub> | <sub>81.95%</sub> | <sub>[agrawal2017](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570347591.pdf)</sub> |  |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>EnvNet-v2 ([tokozume2017a](http://www.mi.t.u-tokyo.ac.jp/assets/publication/LEARNING_ENVIRONMENTAL_SOUNDS_WITH_END-TO-END_CONVOLUTIONAL_NEURAL_NETWORK-poster.pdf)) + Between-Class learning</sub> | <sub>81.80%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| :headphones: <sub>***Human accuracy***</sub> | <sub>Crowdsourcing experiment in classifying ESC-50 by human listeners</sub> | <sub>81.30%</sub> | <sub>[piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf)</sub> | <a href="https://github.com/karoldvl/paper-2015-esc-dataset">:scroll:</a> |
| <sub>**Objects that Sound**</sub> | <sub>*Look, Listen and Learn* (L3) network ([arandjelovic2017a](https://arxiv.org/pdf/1705.08168.pdf)) with stride 2, larger batches and learning rate schedule</sub> | <sub>79.80%</sub> | <sub>[arandjelovic2017b](https://arxiv.org/pdf/1712.06651.pdf)</sub> |  |
| <sub>**Look, Listen and Learn**</sub> | <sub>8-layer convolutional subnetwork pretrained on an audio-visual correspondence task</sub> | <sub>79.30%</sub> | <sub>[arandjelovic2017a](https://arxiv.org/pdf/1705.08168.pdf)</sub> |  |
| <sub>**Learning Environmental Sounds with Multi-scale Convolutional Neural Network**</sub> | <sub>Multi-scale convolutions with feature fusion (waveform + spectrogram)</sub> | <sub>79.10%</sub> | <sub>[zhu2018](https://arxiv.org/pdf/1803.10219.pdf)</sub> |  |
| <sub>**Novel TEO-based Gammatone Features for Environmental Sound Classification**</sub> | <sub>GTSC with CNN</sub> | <sub>79.10%</sub> | <sub>[agrawal2017](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570347591.pdf)</sub> |  |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>EnvNet-v2 ([tokozume2017a](http://www.mi.t.u-tokyo.ac.jp/assets/publication/LEARNING_ENVIRONMENTAL_SOUNDS_WITH_END-TO-END_CONVOLUTIONAL_NEURAL_NETWORK-poster.pdf)) + data augmentation</sub> | <sub>78.80%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Unsupervised Filterbank Learning Using Convolutional Restricted Boltzmann Machine for Environmental Sound Classification**</sub> | <sub>CNN with filterbanks learned using convolutional RBM</sub> | <sub>78.45%</sub> | <sub>[sailor2017](https://pdfs.semanticscholar.org/f6fd/1be38a2d764d900b11b382a379efe88b3ed6.pdf)</sub> |  |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>Baseline CNN ([piczak2015b](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf)) + Batch Normalization + Between-Class learning</sub> | <sub>76.90%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Novel TEO-based Gammatone Features for Environmental Sound Classification**</sub> | <sub>TEO-GTSC with CNN</sub> | <sub>74.85%</sub> | <sub>[agrawal2017](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570347591.pdf)</sub> |  |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>EnvNet-v2 ([tokozume2017a](http://www.mi.t.u-tokyo.ac.jp/assets/publication/LEARNING_ENVIRONMENTAL_SOUNDS_WITH_END-TO-END_CONVOLUTIONAL_NEURAL_NETWORK-poster.pdf))</sub> | <sub>74.40%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Soundnet: Learning sound representations from unlabeled video**</sub> | <sub>8-layer CNN (raw audio) with transfer learning from unlabeled videos</sub> | <sub>74.20%</sub> | <sub>[aytar2016](http://papers.nips.cc/paper/6146-soundnet-learning-sound-representations-from-unlabeled-video.pdf)</sub> | <a href="https://github.com/cvondrick/soundnet">:scroll:</a> |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>18-layer CNN on raw waveforms ([dai2016](https://arxiv.org/pdf/1610.00087.pdf)) + Between-Class learning</sub> | <sub>73.30%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Novel Phase Encoded Mel Filterbank Energies for Environmental Sound Classification**</sub> | <sub>CNN working with phase encoded mel filterbank energies (PEFBEs)</sub> | <sub>73.25%</sub> | <sub>[tak2017](https://www.researchgate.net/profile/Dharmesh_Agrawal/publication/320733074_Novel_Phase_Encoded_Mel_Filterbank_Energies_for_Environmental_Sound_Classification/links/5a084c780f7e9b68229c8947/Novel-Phase-Encoded-Mel-Filterbank-Energies-for-Environmental-Sound-Classification.pdf)</sub> |  |
| <sub>**Classifying environmental sounds using image recognition networks**</sub> | <sub>16 kHz sampling rate, GoogLeNet on spectrograms (40 ms frame length)</sub> | <sub>73.20%</sub> | <sub>[boddapati2017](https://www.sciencedirect.com/science/article/pii/S1877050917316599)</sub> | <a href="https://github.com/bkasvenkatesh/Classifying-Environmental-Sounds-with-Image-Networks">:scroll:</a> |
| <sub>**Learning from Between-class Examples for Deep Sound Recognition**</sub> | <sub>Baseline CNN ([piczak2015b](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf)) + Batch Normalization</sub> | <sub>72.40%</sub> | <sub>[tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> |  |
| <sub>**Novel TEO-based Gammatone Features for Environmental Sound Classification**</sub> | <sub>Fusion of MFCC & TEO-GTCC with GMM</sub> | <sub>72.25%</sub> | <sub>[agrawal2017](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570347591.pdf)</sub> |  |
| <sub>**Learning environmental sounds with end-to-end convolutional neural network (EnvNet)**</sub> | <sub>Combination of spectrogram and raw waveform CNN</sub> | <sub>71.00%</sub> | <sub>[tokozume2017a](http://www.mi.t.u-tokyo.ac.jp/assets/publication/LEARNING_ENVIRONMENTAL_SOUNDS_WITH_END-TO-END_CONVOLUTIONAL_NEURAL_NETWORK-poster.pdf)</sub> |  |
| <sub>**Novel TEO-based Gammatone Features for Environmental Sound Classification**</sub> | <sub>TEO-GTCC with GMM</sub> | <sub>68.85%</sub> | <sub>[agrawal2017](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570347591.pdf)</sub> |  |
| <sub>**Classifying environmental sounds using image recognition networks**</sub> | <sub>16 kHz sampling rate, AlexNet on spectrograms (30 ms frame length)</sub> | <sub>68.70%</sub> | <sub>[boddapati2017](https://www.sciencedirect.com/science/article/pii/S1877050917316599)</sub> | <a href="https://github.com/bkasvenkatesh/Classifying-Environmental-Sounds-with-Image-Networks">:scroll:</a> |
| <sub>**Very Deep Convolutional Neural Networks for Raw Waveforms**</sub> | <sub>18-layer CNN on raw waveforms</sub> | <sub>68.50%</sub> | <sub>[dai2016](https://arxiv.org/pdf/1610.00087.pdf), [tokozume2017b](https://openreview.net/forum?id=B1Gi6LeRZ)</sub> | <a href="https://github.com/philipperemy/very-deep-convnets-raw-waveforms">:scroll:</a> |
| <sub>**Classifying environmental sounds using image recognition networks**</sub> | <sub>32 kHz sampling rate, GoogLeNet on spectrograms (30 ms frame length)</sub> | <sub>67.80%</sub> | <sub>[boddapati2017](https://www.sciencedirect.com/science/article/pii/S1877050917316599)</sub> | <a href="https://github.com/bkasvenkatesh/Classifying-Environmental-Sounds-with-Image-Networks">:scroll:</a> |
| <sub>**WSNet: Learning Compact and Efficient Networks with Weight Sampling**</sub> | <sub>SoundNet 8-layer CNN architecture with 100x model compression</sub> | <sub>66.25%</sub> | <sub>[jin2017](https://openreview.net/forum?id=H1I3M7Z0b)</sub> |  |
| <sub>**Soundnet: Learning sound representations from unlabeled video**</sub> | <sub>5-layer CNN (raw audio) with transfer learning from unlabeled videos</sub> | <sub>66.10%</sub> | <sub>[aytar2016](http://papers.nips.cc/paper/6146-soundnet-learning-sound-representations-from-unlabeled-video.pdf)</sub> | <a href="https://github.com/cvondrick/soundnet">:scroll:</a> |
| <sub>**WSNet: Learning Compact and Efficient Networks with Weight Sampling**</sub> | <sub>SoundNet 8-layer CNN architecture with 180x model compression</sub> | <sub>65.80%</sub> | <sub>[jin2017](https://openreview.net/forum?id=H1I3M7Z0b)</sub> |  |
| <sub>**Soundnet: Learning sound representations from unlabeled video**</sub> | <sub>5-layer CNN trained on raw audio of ESC-50 only</sub> | <sub>65.00%</sub> | <sub>[aytar2016](http://papers.nips.cc/paper/6146-soundnet-learning-sound-representations-from-unlabeled-video.pdf)</sub> | <a href="https://github.com/cvondrick/soundnet">:scroll:</a> |
| <sub>:bar_chart: **Environmental Sound Classification with Convolutional Neural Networks** - ***CNN baseline***</sub> | <sub>CNN with 2 convolutional and 2 fully-connected layers, mel-spectrograms as input, vertical filters in the first layer</sub> | <sub>64.50%</sub> | <sub>[piczak2015b](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf)</sub> | <a href="https://github.com/karoldvl/paper-2015-esc-convnet">:scroll:</a> |
| <sub>**auDeep: Unsupervised Learning of Representations from Audio with Deep Recurrent Neural Networks**</sub> | <sub>MLP classifier on features extracted with an RNN autoencoder</sub> | <sub>64.30%</sub> | <sub>[freitag2017](https://arxiv.org/pdf/1712.04382.pdf)</sub> | <a href="https://github.com/auDeep/auDeep">:scroll:</a> |
| <sub>**Classifying environmental sounds using image recognition networks**</sub> | <sub>32 kHz sampling rate, AlexNet on spectrograms (30 ms frame length)</sub> | <sub>63.20%</sub> | <sub>[boddapati2017](https://www.sciencedirect.com/science/article/pii/S1877050917316599)</sub> | <a href="https://github.com/bkasvenkatesh/Classifying-Environmental-Sounds-with-Image-Networks">:scroll:</a> |
| <sub>**Classifying environmental sounds using image recognition networks**</sub> | <sub>CRNN</sub> | <sub>60.30%</sub> | <sub>[boddapati2017](https://www.sciencedirect.com/science/article/pii/S1877050917316599)</sub> | <a href="https://github.com/bkasvenkatesh/Classifying-Environmental-Sounds-with-Image-Networks">:scroll:</a> |
| <sub>**Comparison of Time-Frequency Representations for Environmental Sound Classification using Convolutional Neural Networks**</sub> | <sub>3-layer CNN with vertical filters on wideband mel-STFT (*median accuracy*)</sub> | <sub>*56.37%*</sub> | <sub>[huzaifah2017](https://arxiv.org/pdf/1706.07156.pdf)</sub> |  |
| <sub>**Comparison of Time-Frequency Representations for Environmental Sound Classification using Convolutional Neural Networks**</sub> | <sub>3-layer CNN with square filters on wideband mel-STFT (*median accuracy*)</sub> | <sub>*54.00%*</sub> | <sub>[huzaifah2017](https://arxiv.org/pdf/1706.07156.pdf)</sub> |  |
| <sub>**Soundnet: Learning sound representations from unlabeled video**</sub> | <sub>8-layer CNN trained on raw audio of ESC-50 only</sub> | <sub>51.10%</sub> | <sub>[aytar2016](http://papers.nips.cc/paper/6146-soundnet-learning-sound-representations-from-unlabeled-video.pdf)</sub> | <a href="https://github.com/cvondrick/soundnet">:scroll:</a> |
| <sub>**Comparison of Time-Frequency Representations for Environmental Sound Classification using Convolutional Neural Networks**</sub> | <sub>5-layer CNN with square filters on wideband mel-STFT (*median accuracy*)</sub> | <sub>*50.87%*</sub> | <sub>[huzaifah2017](https://arxiv.org/pdf/1706.07156.pdf)</sub> |  |
| <sub>**Comparison of Time-Frequency Representations for Environmental Sound Classification using Convolutional Neural Networks**</sub> | <sub>5-layer CNN with vertical filters on wideband mel-STFT (*median accuracy*)</sub> | <sub>*46.25%*</sub> | <sub>[huzaifah2017](https://arxiv.org/pdf/1706.07156.pdf)</sub> |  |
| :bar_chart: <sub>***Baseline - random forest***</sub> | <sub>Baseline ML approach (MFCC & ZCR + random forest)</sub> | <sub>44.30%</sub> | <sub>[piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf)</sub> | <a href="https://github.com/karoldvl/paper-2015-esc-dataset">:scroll:</a> |
| <sub>**Soundnet: Learning sound representations from unlabeled video**</sub> | <sub>Convolutional autoencoder trained on unlabeled videos</sub> | <sub>39.90%</sub> | <sub>[aytar2016](http://papers.nips.cc/paper/6146-soundnet-learning-sound-representations-from-unlabeled-video.pdf)</sub> | <a href="https://github.com/cvondrick/soundnet">:scroll:</a> |
| :bar_chart: <sub>***Baseline - SVM***</sub> | <sub>Baseline ML approach (MFCC & ZCR + SVM)</sub> | <sub>39.60%</sub> | <sub>[piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf)</sub> | <a href="https://github.com/karoldvl/paper-2015-esc-dataset">:scroll:</a> |
| :bar_chart: <sub>***Baseline - k-NN***</sub> | <sub>Baseline ML approach (MFCC & ZCR + k-NN)</sub> | <sub>32.20%</sub> | <sub>[piczak2015a](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf)</sub> | <a href="https://github.com/karoldvl/paper-2015-esc-dataset">:scroll:</a> |
| <sub>**A mixture model-based real-time audio sources classification method**</sub> | <sub>Dictionary of sound models used for classification (*accuracy is computed on segments instead of files*)</sub> | <sub>*94.00%*</sub> | <sub>[baelde2017](https://hal.archives-ouvertes.fr/hal-01420677v2/document)</sub> |  |
| <sub>**NELS - Never-Ending Learner of Sounds**</sub> | <sub>Large-scale audio crawling with classifiers trained on AED datasets (including ESC-50)</sub> | <sub>N/A</sub> | <sub>[elizalde2017](http://media.aau.dk/smc/wp-content/uploads/2017/12/ML4AudioNIPS17_paper_3.pdf)</sub> | <a href="http://nels.cs.cmu.edu/">:scroll:</a> |
| <sub>**Utilizing Domain Knowledge in End-to-End Audio Processing**</sub> | <sub>End-to-end CNN with learned mel-spectrogram transformation</sub> | <sub>N/A</sub> | <sub>[tax2017](https://arxiv.org/pdf/1712.00254.pdf)</sub> | <a href="https://github.com/corticph/MSTmodel">:scroll:</a> |
| <sub>**Deep Neural Network based learning and transferring mid-level audio features for acoustic scene classification**</sub> | <sub>Transfer learning from various datasets, including ESC-50</sub> | <sub>N/A</sub> | <sub>[mun2017](https://pdfs.semanticscholar.org/5f1e/513aec29b8c471723172f1d5bc2174daa71a.pdf)</sub> |  |
| <sub>**Features and Kernels for Audio Event Recognition**</sub> | <sub>MFCC, GMM, SVM</sub> | <sub>N/A</sub> | <sub>[kumar2016b](https://arxiv.org/pdf/1607.05765.pdf)</sub> |  |
| <sub>**A real-time environmental sound recognition system for the Android OS**</sub> | <sub>Real-time sound recognition for Android evaluated on ESC-10</sub> | <sub>N/A</sub> | <sub>[pillos2016](https://www.cs.tut.fi/sgn/arg/dcase2016/documents/workshop/Pillos-DCASE2016workshop.pdf)</sub> |  |
| <sub>**Comparing Time and Frequency Domain for Audio Event Recognition Using Deep Learning**</sub> | <sub>Discriminatory effectiveness of different signal representations compared on ESC-10 and Freiburg-106</sub> | <sub>N/A</sub> | <sub>[hertel2016](https://arxiv.org/pdf/1603.05824.pdf)</sub> |  |
| <sub>**Audio Event and Scene Recognition: A Unified Approach using Strongly and Weakly Labeled Data**</sub> | <sub>Combination of weakly labeled data (YouTube) with strong labeling (ESC-10) for Acoustic Event Detection</sub> | <sub>N/A</sub> | <sub>[kumar2016a](https://arxiv.org/pdf/1611.04871.pdf)</sub> |  |


## Repository content

- [`audio/*.wav`](audio/)

  2000 audio recordings in WAV format (5 seconds, 44.1 kHz, mono) with the following naming convention:
  
  `{FOLD}-{CLIP_ID}-{TAKE}-{TARGET}.wav`
  
  - `{FOLD}` - index of the cross-validation fold,
  - `{CLIP_ID}` - ID of the original Freesound clip,
  - `{TAKE}` - letter disambiguating between different fragments from the same Freesound clip,
  - `{TARGET}` - class in numeric format [0, 49].

- [`meta/esc50.csv`](meta/esc50.csv)

  CSV file with the following structure:
  
  | <sub>filename</sub> | <sub>fold</sub> | <sub>target</sub> | <sub>category</sub> | <sub>esc10</sub> | <sub>src_file</sub> | <sub>take</sub> |
  | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  
  The `esc10` column indicates if a given file belongs to the *ESC-10* subset (10 selected classes, CC BY license).
  
- [`meta/esc50-human.xlsx`](meta/esc50-human.xlsx)

  Additional data pertaining to the crowdsourcing experiment (human classification accuracy).


## License

The dataset is available under the terms of the [Creative Commons Attribution Non-Commercial license](http://creativecommons.org/licenses/by-nc/3.0/).

A smaller subset (clips tagged as *ESC-10*) is distributed under CC BY (Attribution).

Attributions for each clip are available in the [ LICENSE file](LICENSE).


## Citing

<a href="http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf"><img src="https://img.shields.io/badge/download%20paper-PDF-ff69b4.svg" alt="Download paper in PDF format" title="Download paper in PDF format" align="right" /></a>

If you find this dataset useful in an academic setting please cite:

> K. J. Piczak. **ESC: Dataset for Environmental Sound Classification**. *Proceedings of the 23rd Annual ACM Conference on Multimedia*, Brisbane, Australia, 2015.
> 
> [DOI: http://dx.doi.org/10.1145/2733373.2806390]

    @inproceedings{piczak2015dataset,
      title = {{ESC}: {Dataset} for {Environmental Sound Classification}},
      author = {Piczak, Karol J.},
      booktitle = {Proceedings of the 23rd {Annual ACM Conference} on {Multimedia}},
      date = {2015-10-13},
      url = {http://dl.acm.org/citation.cfm?doid=2733373.2806390},
      doi = {10.1145/2733373.2806390},
      location = {{Brisbane, Australia}},
      isbn = {978-1-4503-3459-4},
      publisher = {{ACM Press}},
      pages = {1015--1018}
    }

## Caveats

Please be aware of potential information leakage while training models on *ESC-50*, as some of the original Freesound recordings were already preprocessed in a manner that might be class dependent (mostly bandlimiting). Unfortunately, this issue went unnoticed when creating the original version of the dataset. Due to the number of methods already evaluated on *ESC-50*, no changes rectifying this issue will be made in order to preserve comparability.


## Changelog

###### v2.0.0 (2017-12-13)

> <sub>• Change to WAV version as default.</sub>

###### v2.0.0-pre (2016-10-10) (wav-files branch)

> <sub>• Replace OGG recordings with cropped WAV files for easier loading and frame-level precision (some of the OGG recordings had a slightly different length when loaded).<br/>• Move recordings to a one directory structure with a meta CSV file.</sub>

###### v1.0.0 (2015-04-15)

> <sub>• Initial version of the dataset (OGG format).</sub>
