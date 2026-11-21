# SHIMA-Python Installation Guide

SHIMA-Python requires Python 3.12 or later. Port `8050` is used by the application.

## System requirements

- Python 3.12 or later
- macOS, Linux, or Windows
- 4 GB RAM minimum; 8 GB or more is recommended
- A modern browser
- Docker and Docker Compose are optional

## Install with pip

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m shima
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Open <http://127.0.0.1:8050>.

For an installed wheel:

```bash
python -m pip install dist/shima_python-1.0.1-py3-none-any.whl
python -m shima
```

## Optional Louvain support

Leiden clustering is the default and requires no Louvain extra.

Louvain generation is optional and only supported where the `louvain` package is installable, with the extra currently marked for Python below 3.12:

```bash
python -m pip install "shima-python[louvain]"
```

Louvain is not claimed as supported on Python 3.12. Existing AnnData/H5AD objects containing a `louvain` column can still be loaded and analyzed. Louvain requests on unsupported environments produce an actionable error.

## Conda

Conda validation is static because Conda is not required for local pip installation.

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
conda env create -f environment.yml
conda activate shima-python
python -m shima
```

The environment is named `shima-python` and declares Python 3.12 or later.

Update the environment with:

```bash
conda activate shima-python
conda env update -f environment.yml --prune
```

Remove it with:

```bash
conda env remove -n shima-python
```

## Docker

The Docker image uses Python 3.12.16 and preserves port 8050.

```bash
git clone https://github.com/msherafatian/shima-python.git
cd shima-python
docker build -t shima-python:1.0.1 .
docker run --rm -p 8050:8050 --name shima-python shima-python:1.0.1
```

Open <http://localhost:8050>.

With Docker Compose:

```bash
docker compose up --build
```

The Compose service is named `shima` and the container name is `shima-python`.

Stop and remove the service with:

```bash
docker compose down
docker rmi shima-python:1.0.1
```

## Verification

```bash
python --version
python -c "import shima; print(shima.__version__)"
python -c "import scanpy; print(scanpy.__version__)"
python -m pip check
python -m pytest -q
python -m shima
```

Expected package version: `1.0.1`.

## Entry points

Supported application launch:

```bash
python -m shima
```

Docker also launches the existing `app:server` application entry point with Gunicorn.

## Troubleshooting

### Port 8050 is already in use

On macOS or Linux:

```bash
lsof -ti:8050 | xargs kill
```

Start the application again after stopping the conflicting process.

### Louvain request fails

Leiden remains the default. Louvain generation may require the optional extra on a supported Python version:

```bash
python -m pip install "shima-python[louvain]"
```

On Python 3.12, Louvain generation is not claimed as supported.

### Missing package

Confirm that the virtual environment is active:

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pip check
```

## Legacy MASIH-Python

The historical MASIH-Python software and DOI records remain unchanged:

- Concept DOI: <https://doi.org/10.5281/zenodo.17824054>
- Version-specific DOI: <https://doi.org/10.5281/zenodo.17824053>
- Historical repository: <https://github.com/msherafatian/masih-python>

The `masih` Python namespace is retained as a deprecated compatibility alias for one release cycle.

## Related repository

- SHIMA-Python: <https://github.com/msherafatian/shima-python>
- SHIMA R/Shiny: <https://github.com/msherafatian/shima>
