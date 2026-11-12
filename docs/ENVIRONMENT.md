# Environment specification

`environment.yml` and `requirements.txt` record a portable selection of the
experiment dependencies. The source environment uses Python 3.10.20 and
PyTorch 2.4.1 with CUDA 12.1. Package versions are retained while machine-specific
Conda build strings, local installation prefixes, and private mirror settings
are removed.

For a Python 3.10 environment:

```bash
python -m pip install -r requirements.txt
```

Alternatively:

```bash
conda env create -f environment.yml
conda activate glsm
```

Choose a PyTorch wheel suitable for the operating system and GPU using the
[official PyTorch instructions](https://pytorch.org/get-started/previous-versions/).
The reference CUDA 12.1 installation is:

```bash
python -m pip install torch==2.4.1 --index-url https://download.pytorch.org/whl/cu121
```

PyPOTS, BenchPOTS, PyGrinder, TSDB, and NNI are external dependencies. Their
implementations and licenses remain with their respective projects. Reading the
JSON configuration records requires only the Python standard library.
