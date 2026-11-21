"""
Focused clustering tests for Leiden and optional Louvain behavior.
"""

import importlib.util

import anndata as ad
import numpy as np
import pytest
import scanpy as sc

from shima.utils.data_store import DataStoreManager
from shima.utils.scanpy_utils import find_clusters


def make_adata():
    adata = ad.AnnData(
        X=np.array(
            [
                [0.0, 0.0, 1.0],
                [0.0, 1.0, 1.0],
                [1.0, 1.0, 0.0],
                [1.0, 0.0, 0.0],
            ],
            dtype="float32",
        )
    )
    adata.obs_names = [f"cell-{index}" for index in range(4)]
    adata.var_names = [f"gene-{index}" for index in range(3)]
    sc.pp.pca(adata, n_comps=2)
    sc.pp.neighbors(adata, n_neighbors=2, n_pcs=2)
    return adata


def test_leiden_remains_default_clustering():
    adata = make_adata()

    find_clusters(adata)

    assert "leiden" in adata.obs
    assert adata.obs["leiden"].nunique() >= 1


def test_missing_louvain_dependency_returns_actionable_error(monkeypatch):
    adata = make_adata()
    monkeypatch.setattr(importlib.util, "find_spec", lambda name: None)

    with pytest.raises(ImportError, match=r"pip install"):
        find_clusters(adata, algorithm="louvain")

    assert "louvain" not in adata.obs


def test_existing_louvain_result_is_preserved(tmp_path):
    adata = make_adata()
    adata.obs["louvain"] = ["lou-0", "lou-1", "lou-0", "lou-1"]

    store = DataStoreManager(base_dir=str(tmp_path))
    metadata = store.store_adata(adata)
    loaded = store.load_adata(metadata["session_id"])

    assert "louvain" in loaded.obs
    assert loaded.obs["louvain"].tolist() == ["lou-0", "lou-1", "lou-0", "lou-1"]
