# SHIMA — Single-cell Heterogeneity and Interactive Molecular Analysis

<img src="shima/assets/logo.PNG" alt="SHIMA logo" width="120" align="right" />

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/msherafatian/shima-python.svg)](https://github.com/msherafatian/shima-python/issues)

SHIMA-Python is a Python/Dash/Scanpy implementation of SHIMA for interactive analysis of single-cell RNA sequencing (scRNA-seq) data. It provides quality control, clustering, marker-gene analysis, functional pathway scoring, trajectory analysis, cell-cycle analysis, interactive visualization, and data/plot export.

The Python implementation is linked to the separate [SHIMA R/Shiny implementation](https://github.com/msherafatian/shima). The Python and R implementations have separate source repositories and separate scholarly records.

## Features

- 10X Genomics, H5AD, CSV/TSV, and expression-matrix input
- Quality control and configurable preprocessing
- Leiden clustering by default
- Optional Louvain clustering on compatible older Python environments
- PCA, UMAP, and t-SNE dimensionality reduction
- Marker-gene detection and visualization
- CancerSEA functional-state scoring
- PAGA-based trajectory analysis
- Cell-cycle analysis
- Excel, CSV, H5AD, PNG, PDF, and SVG export

## Quick start

### Pip installation

Python 3.12 or later is required.

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m shima
```

Open <http://127.0.0.1:8050>.

The package distribution can also be installed from a local build:

```bash
python -m pip install dist/shima_python-1.0.1-py3-none-any.whl
```

### Docker

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
docker compose up --build
```

Open <http://localhost:8050>. The Compose service remains on port `8050`.

### Conda

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
conda env create -f environment.yml
conda activate shima-python
python -m shima
```

See [INSTALL.md](INSTALL.md) for full instructions.

## Louvain clustering

Leiden clustering is the default and is included with the normal SHIMA-Python installation.

Louvain generation is optional and is currently limited to Python versions below 3.12:

```bash
python -m pip install "shima-python[louvain]"
```

Louvain support is not claimed for Python 3.12 because the package could not be built reliably in the validated Python 3.12 environment. Existing H5AD/AnnData objects that already contain Louvain result columns remain supported and can be loaded and displayed.

## Supported data

- 10X Genomics Cell Ranger output
- H5AD files
- CSV/TSV expression matrices
- Existing processed AnnData objects

## Analysis modules

- Upload and quality control
- Cluster analysis
- Cell-cycle analysis
- Marker genes
- CancerSEA pathways
- Trajectory analysis
- Cross-cluster/pathway comparison
- Interactive cell explorer
- Publication and data export

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m pip check
python -m build
```

## Citation

SHIMA-Python version 1.0.1 does not yet have a new Zenodo DOI. The DOI should be registered and linked only after a Zenodo deposit is created.

### Historical MASIH-Python citation

Historical MASIH-Python releases should continue to cite:

- Concept DOI: <https://doi.org/10.5281/zenodo.17824054>
- Version-specific DOI: <https://doi.org/10.5281/zenodo.17824053>

BibTeX for the historical software identity:

```bibtex
@software{masih_python_2024,
  author = {Sherafatian, Masih},
  title = {MASIH-Python: Modular Analysis Suite for Interactive Heterogeneity},
  year = {2024},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.17824054},
  url = {https://doi.org/10.5281/zenodo.17824054}
}
```

## Compatibility

The deprecated `masih` Python namespace is retained for one release cycle and forwards imports to `shima`.

```python
# Current
from shima.utils.data_store import DataStoreManager

# Deprecated compatibility namespace
from masih.utils.data_store import DataStoreManager
```

## License

SHIMA-Python is licensed under GPL-3.0-or-later. See [LICENSE](LICENSE).

## Related projects

- [SHIMA R/Shiny](https://github.com/msherafatian/shima)
- [SHIMA-Python GitHub repository](https://github.com/msherafatian/shima-python)
