"""Global periodic component Interface-only resource snapshot."""

# Copyright (c) 2026, Yuan Feng <fengyuan2022@zju.edu.cn>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Callable, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn


class TSbackbone_pattern_idv(nn.Module):
    """Global periodic component; constructor names match the research project."""

    def __init__(self, freqs_num: int, feature_num: int, control_point_num: int, hidden_dim: int, hidden_layer_num: int=2, intrinsic_mode_init_method: str='sincos', intrinsic_mode_scale_factor: float=0.1):
        super().__init__()
        self.interface_configuration = {'freqs_num': freqs_num, 'feature_num': feature_num, 'control_point_num': control_point_num, 'hidden_dim': hidden_dim, 'hidden_layer_num': hidden_layer_num, 'intrinsic_mode_init_method': intrinsic_mode_init_method, 'intrinsic_mode_scale_factor': intrinsic_mode_scale_factor}

    def forward(self, TS_data: torch.Tensor, TS_freqs_params: torch.Tensor):
        """Numerical operators will be supplied in a subsequent release."""
        raise NotImplementedError("This snapshot provides the component interface only.")
