# GLSM

Resources for **From Global Periodic Modeling to Local Neighborhood Refinement:
A Coarse-to-Fine Serial Framework for Multivariate Time Series Imputation**.

Authors: Yuan Feng, Hui Liu, Zhenyu Liu, Rui Li, Weiqiang Jia, and Jianrong Tan.

Repository: <https://github.com/IFengSource/GLSM>

## Current materials

This snapshot provides the GLSM model interfaces and serial architecture
skeleton, selected experiment settings, hyperparameter search-space definitions,
an environment specification, and data-processing protocols. The source and
configuration files retain the directory organization of the research project.

The model files describe interfaces and module connections. Numerical operators
are represented by explicit interface methods. Complete numerical implementations
and documented training and evaluation entry points will be provided in future
updates.

## File map

| Path | Contents |
| --- | --- |
| `diy_pypots/models/GLSM/core.py` | Model constructor and global-to-local serial assembly skeleton |
| `diy_pypots/nn/modules/timestamp/backbone.py` | Global periodic component interface |
| `diy_pypots/nn/modules/residual/backbone.py` | Local residual refinement interface |
| `my_utils/model_utils.py` | Missingness-aware normalization interface |
| `data/preprocess/pipeline.py` | Global frequency-estimation interface |
| `data/preprocess/protocols.json` | Dataset split, window, coordinate, and masking specifications |
| `configs/hpo_results/` | Selected parameter dictionaries grouped by dataset |
| `auto_tuning/models_tuning_space_setting/` | Search-space definitions in the original JSON format |
| `configs/global_config.py` | Experiment seeds and shared settings |
| `configs/experiment_protocols.json` | Selection and evaluation conventions |
| `environment.yml`, `requirements.txt` | Reference dependency versions |

Read [data processing](docs/PREPROCESSING.md), [dataset access](docs/DATASETS.md),
[parameter conventions](docs/HYPERPARAMETERS.md), and
[environment setup](docs/ENVIRONMENT.md) for the accompanying specifications.

Configuration records can be inspected independently of the model interfaces:

```python
from configs.hpo_results import HPO_RESULTS

parameters = HPO_RESULTS["ETT_h1"]["GLSM"]
print(parameters)
```

The interface constructor remains at its original import path:

```python
from diy_pypots.models.GLSM.core import _GLSM
```

## License and attribution

GLSM-authored additions are distributed under the BSD 3-Clause License in
[LICENSE](LICENSE). Existing author notices are retained in configuration files.
Separately credited material retains its original ownership and applicable
terms; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and `LICENSES/`.
Dataset access and redistribution terms are governed by their original sources.
