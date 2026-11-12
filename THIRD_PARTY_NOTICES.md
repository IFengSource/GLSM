# Third-party notices

## Retained configuration and utility notices

The selected-configuration files preserve their original notices:

```text
Created by Fanxing Liu <fanxingliu2020@gmail.com>
License: BSD-3-Clause
```

The shared experiment settings and metric interface preserve the original
attribution to Wenjie Du and the BSD-3-Clause identifier. These attributions
remain in addition to the GLSM-specific additions. Reformatting a configuration
record or publishing a reduced interface does not transfer its original rights
to Yuan Feng (fengyuan2022@zju.edu.cn).

The retained PyPOTS license is provided in `LICENSES/PyPOTS.txt`. The BenchPOTS
license is provided in `LICENSES/BenchPOTS.txt` for the credited processing
conventions. Neither package's full implementation is vendored here.

## External software and method acknowledgments

- [PyPOTS](https://github.com/WenjieDu/PyPOTS): experiment framework conventions,
  shared settings, and metric interface attribution; BSD-3-Clause.
- [BenchPOTS](https://github.com/WenjieDu/BenchPOTS): dataset-processing conventions;
  BSD-3-Clause.
- [PyGrinder](https://github.com/WenjieDu/PyGrinder): artificial missingness tools,
  used as an external dependency.
- [TSDB](https://github.com/WenjieDu/TSDB): dataset loading, used as an external
  dependency.
- [SAITS](https://doi.org/10.1016/j.eswa.2023.119619): observed and artificially
  masked reconstruction-objective structure used by the research implementation.
- [RevIN](https://openreview.net/forum?id=cGDAkQo1C0p): reversible normalization
  background. This snapshot contains a normalization interface, not a copy of the
  original RevIN numerical implementation.

Baseline parameter records identify experiment settings. They do not redistribute
baseline model source code or assign a new license to external implementations.
Python, NumPy, PyTorch, SciPy, pandas, scikit-learn, h5py, and NNI retain their
respective licenses.

## Data

Dataset links and attribution are listed in [docs/DATASETS.md](docs/DATASETS.md).
No raw dataset is included and the project software license does not replace
dataset-provider terms.
