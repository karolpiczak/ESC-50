import pandas as pd

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
META_PATH = ROOT / "meta" / "esc50.csv"
AUDIO_DIR = ROOT / "audio"


def test_metadata_has_expected_columns():
    metadata = pd.read_csv(META_PATH)
    expected = {
        "filename", "fold", "target", "category",
        "esc10", "src_file", "take"
    }
    assert expected.issubset(metadata.columns)


def test_metadata_has_no_missing_values_or_duplicate_filenames():
    metadata = pd.read_csv(META_PATH)
    assert not metadata.isnull().any().any()
    assert not metadata["filename"].duplicated().any()


def test_metadata_targets_are_valid():
    metadata = pd.read_csv(META_PATH)
    assert metadata["target"].between(0, 49).all()


def test_metadata_folds_are_valid():
    metadata = pd.read_csv(META_PATH)
    assert metadata["fold"].isin([1, 2, 3, 4, 5]).all()


def test_each_class_has_40_recordings():
    metadata = pd.read_csv(META_PATH)
    counts = metadata.groupby("target").size()
    assert len(counts) == 50
    assert (counts == 40).all()


def test_metadata_audio_files_exist():
    metadata = pd.read_csv(META_PATH)
    expected_files = set(metadata["filename"])
    actual_files = {path.name for path in AUDIO_DIR.iterdir() if path.is_file()}
    assert expected_files == actual_files
