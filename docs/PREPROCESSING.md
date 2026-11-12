# Data-processing protocol

## Dataset preparation

All partitions preserve chronological order. Values are standardized separately
for each variable using a `StandardScaler` fitted on the training partition only.
The same fitted transformation is applied to validation and test data. Windows
are built inside each partition, with the window length also used as the stride.
The existing BenchPOTS-style windowing convention is used, including its handling
of partition tails. Windows do not cross partition boundaries.

| Dataset | Variables | Sampling interval | Window length | Chronological split |
| --- | ---: | --- | ---: | --- |
| ETTh1 | 7 | 1 hour | 48 | First 14 observed calendar months for training, next 5 for validation, remaining months for testing |
| WindTurbine | 4 | 10 minutes | 72 | First 255 observed calendar days for training, next 37 for validation, remaining days for testing |
| ItalyAir | 13 | 1 hour | 12 | With `v = round(0.2 * N)`, training uses the first `N - 2*v` rows, followed by `v` validation and `v` test rows |
| GuangzhouTraffic | 214 | 10 minutes | 48 | First 43 complete days for training, next 6 for validation, remaining 12 for testing |

For ETTh1, use the seven numeric measurement columns. For WindTurbine, the date
column provides coordinates and the remaining four columns provide measurements.
For ItalyAir, combine `Date` and `Time` to obtain timestamps and use the remaining
13 columns as features. The dataset values follow the TSDB/BenchPOTS evaluation
convention used in the experiments, including the numeric `-200` sentinel values.
Actual NaNs remain unavailable observations.

For GuangzhouTraffic, use the official `tensor.mat` and adjacent day/time mapping
CSVs. Preserve the road order, flatten the day and ten-minute-slot axes into
chronological time, and convert native zero-valued absent readings to NaN. Do not
interpolate these native gaps before splitting or standardization.

## Global time coordinates

Convert timestamps to numeric nanoseconds. On training timestamps, let `s` be the
first timestamp and let `g` be the integer quotient of the first-to-last timestamp
distance by `N_train - 1`. Transform each timestamp with `(timestamp - s) // g`.
Reuse the same `s` and `g` for validation and test timestamps. Coordinates retain
their global origin and are windowed in alignment with the measurements.

GLSM frequency estimation reads the incomplete training history and its aligned
global coordinates. A continuous validation sequence retained by the shared data
interface is distinct from this training-only frequency reference.

## Artificial missingness

Dataset generation uses seed `2024`. The five reported settings are point
missingness at 50%, 70%, and 90%, block missingness at nominal 50%, and subsequence
missingness at nominal 50%. The exact generation arguments are listed in
`data/preprocess/protocols.json`.

Point masks use PyGrinder `mcar`; subsequence masks use `seq_missing`; block masks
use `block_missing`. A block-generation factor is not a missing-rate argument.
Overlaps and native missing positions can affect realized mask coverage. Retain
the pre-mask values for evaluation and keep artificial masks separate from native
missingness. For GuangzhouTraffic, draw the artificial mask on an all-observed
array of the window shape, then apply it to the window containing native NaNs.

Validation and test targets are originally available values that have been
artificially hidden. Native NaNs are not evaluation targets. The five model-run
seeds are `2024`, `2025`, `2026`, `2027`, and `2028`. Training-time re-masking is
separate from dataset-generation masks; the GLSM training re-masking rate is 0.2.

## Evaluation convention

Reported imputation MAE and MSE use the training-standardized measurement scale
and the artificial evaluation mask. Measurements in physical units can be
obtained using the inverse training scaler, but they are not substituted for the
paper's standardized metrics.
