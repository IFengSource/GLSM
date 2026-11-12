"""Metric interface used by the GLSM constructor."""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: BSD-3-Clause
# Interface-only adaptation by Yuan Feng <fengyuan2022@zju.edu.cn>; numerical code is not vendored.

from __future__ import annotations

from typing import Callable, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn


def calc_mse(predictions: Union[np.ndarray, torch.Tensor], targets: Union[np.ndarray, torch.Tensor], masks: Optional[Union[np.ndarray, torch.Tensor]]=None):
    """Masked metric interface; numerical implementation is supplied separately."""
    raise NotImplementedError("This snapshot provides the metric interface only.")
