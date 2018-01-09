#!/usr/bin/env python
# -*- coding: utf-8 -*-

import filecmp
import os
import subprocess
import tempfile

import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sb
import tqdm


sb.set(style="white")
matplotlib.rcParams['font.family'] = 'PT Sans'


@pytest.fixture(scope='module')
def recording_list():
    return sorted(os.listdir('audio'))


@pytest.fixture(scope='module')
def meta():
    return pd.read_csv('meta/esc50.csv')


def test_dataset_size(recording_list):
    assert len(recording_list) == 2000


def test_recordings(recording_list):
    for recording in tqdm.tqdm(recording_list):
        signal, rate = librosa.load('audio/' + recording, sr=None, mono=False)

        assert rate == 44100
        assert len(signal.shape) == 1  # mono
        assert len(signal) == 220500  # 5 seconds
        assert np.max(signal) > 0
        assert np.min(signal) < 0
        assert np.abs(np.mean(signal)) < 0.2  # rough DC offset check


def test_previews(meta):
    np.random.seed(20171207)

    recordings = meta.groupby('target')['filename'].apply(lambda cat: cat.sample(1)).reset_index()['filename']

    f, ax = plt.subplots(1, 1, sharey=False, sharex=False, figsize=(8, 2))

    with tempfile.TemporaryDirectory() as tmpdir:
        for index in range(len(recordings)):
            recording = recordings[index]
            signal = librosa.load('audio/' + recording, sr=44100)[0]
            spec = librosa.feature.melspectrogram(signal, sr=44100, n_fft=2205, hop_length=441)
            spec = librosa.power_to_db(spec)

            category = meta[meta.filename == recording].category.values[0]

            ax.imshow(spec, origin='lower', interpolation=None, cmap='viridis', aspect=1.1)
            ax.set_title(f'{category} - {recording}', fontsize=11)
            ax.get_yaxis().set_visible(False)
            ax.get_xaxis().set_visible(False)
            f.tight_layout()
            plt.savefig(f'{tmpdir}/{index:02d}.png', bbox_inches='tight', dpi=72)

        subprocess.call(['convert', '-delay', '100', '-loop', '0', f'{tmpdir}/*.png', '_esc50.gif'])

    assert filecmp.cmp('esc50.gif', '_esc50.gif')
