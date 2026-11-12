# Hyperparameter records

`configs/hpo_results/` contains the available selected experiment settings in the
project's dictionary format. Dataset names are `ETT_h1`, `wind_turbine`, `ItalyAir`,
and `GuangzhouTraffic`. The `HPO_RESULTS` mapping in that directory's `__init__.py`
provides a common lookup. The same records are available as
`selected_configurations.json` for language-independent inspection.

Model identifiers retain project naming: `GPVAE` denotes GP-VAE, `TimeMixerPP`
denotes TimeMixer++, and `MG_Transformer` denotes MG-Transformer. `SADI_MPB`
contains the selected SADI settings used for the RM-to-MPB experiment protocol.
Its hyperparameters are selected through the `SADI_RM` search space. The second
stage uses partial-blackout probability 0.5, one fixed mask draw, at most 100
epochs, and patience 10. The selected stage-control settings are recorded in
`configs/experiment_protocols.json`.

Search-space definitions are under their original paths in
`auto_tuning/models_tuning_space_setting/`. JSON `_type` and `_value` entries use
NNI's original representation. They describe proposed parameter choices and do
not encode completed trial counts. GTEE's published configuration records use
the offline-search family.

The selection protocol budgets 100 random-search trials for each model-dataset
pair under 50% point missingness and selects by validation loss. The selected
settings are reused across the five missingness settings. Random seeds and fixed
protocol values are documented separately from the selected parameter records.

For GLSM, frequency-estimation keys have prefix `GC_`. Remove that prefix when
passing them to the frequency-estimation interface. `GC_K` cannot exceed
`GC_K_prime`. `TS_*` keys control global periodic modeling and normalization.
`top_k`, `hidden_dim`, `dropout`, and `num_layers` control local refinement.
The configuration learning rate belongs to the optimizer rather than the core
network constructor. The main reconstruction weights are ORT=1 and MIT=1.

GuangzhouTraffic's GLSM settings describe the experiment that used the accelerated
execution path; parameter values are retained under the GLSM method name.
