# Dataset sources and use

| Dataset | Original source or accompanying study | Required inputs |
| --- | --- | --- |
| ETTh1 | [ETDataset](https://github.com/zhouhaoyi/ETDataset), accompanying Informer | ETTh1 measurements and timestamps, as loaded through TSDB |
| ItalyAir | [UCI Air Quality](https://doi.org/10.24432/C59K5F) | The TSDB `italy_air_quality` representation with Date, Time, and 13 measurement columns |
| WindTurbine | [Wind Turbine SCADA Dataset](https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset), also described in [GTEE](https://doi.org/10.1016/j.inffus.2026.104220) | The project-formatted chronological CSV with one date column and four numeric measurement columns |
| GuangzhouTraffic | [Urban Traffic Speed Dataset of Guangzhou, China](https://doi.org/10.5281/zenodo.1205229), Zenodo | `tensor.mat`, `day_information_table.csv`, and `time_information_table.csv` |

Obtain datasets from their original providers and follow the applicable access,
citation, and reuse terms. The software license does not grant additional rights
to third-party datasets. This resource snapshot provides processing specifications
and source links rather than redistributing the raw measurements.

Keep timestamps, feature order, chronological splits, scaler fitting, native
missingness, and artificial-mask conventions aligned with
[PREPROCESSING.md](PREPROCESSING.md) and `data/preprocess/protocols.json`.
