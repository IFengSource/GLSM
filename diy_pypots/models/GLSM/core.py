"""GLSM constructor and serial assembly skeleton, without numerical operators."""

# Copyright (c) 2026, Yuan Feng <fengyuan2022@zju.edu.cn>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Callable, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn

from diy_pypots.nn.modules.timestamp.backbone import TSbackbone_pattern_idv
from diy_pypots.nn.modules.residual.backbone import MultiHopResidualImputer
from diy_pypots.utils.metrics.error import calc_mse
from my_utils.model_utils import ShrinkageRevIN


class _GLSM(nn.Module):
    """Research-project interface and normalization -> global -> local wiring.

    Inputs use X/missing_mask of shape (B,T,C) and X_TS of shape (B,T,1).
    Components are interfaces in this snapshot, not fitted numerical models.
    """

    def __init__(self, TS_freqs_params: np.ndarray, TS_control_point_num: int, TS_hidden_dim: int, TS_hidden_layer_num: int, TS_intrinsic_mode_init_method: str, TS_intrinsic_mode_scale_factor: float, TS_revin_init_kappa: float, TS_revin_min_std: float, top_k: int, hidden_dim: int, dropout: float, num_layers: int, loss_adjust_weight: float, ORT_weight: float, MIT_weight: float, n_steps: int, n_features: int, customized_loss_func: Callable=calc_mse):
        super().__init__()
        self.n_steps = n_steps
        self.n_features = n_features
        self.register_buffer("TS_freqs_params", torch.as_tensor(TS_freqs_params, dtype=torch.float32))
        self.TS_model = TSbackbone_pattern_idv(
            freqs_num=self.TS_freqs_params.shape[-1], feature_num=n_features,
            control_point_num=TS_control_point_num, hidden_dim=TS_hidden_dim,
            hidden_layer_num=TS_hidden_layer_num,
            intrinsic_mode_init_method=TS_intrinsic_mode_init_method,
            intrinsic_mode_scale_factor=TS_intrinsic_mode_scale_factor)
        self.revin = ShrinkageRevIN(n_features=n_features, affine=False,
                                   init_kappa=TS_revin_init_kappa, min_std=TS_revin_min_std)
        self.residual_model = MultiHopResidualImputer(
            n_features=n_features, n_steps=n_steps, top_k=top_k,
            hidden_dim=hidden_dim, dropout=dropout, num_layers=num_layers)
        self.loss_configuration = dict(loss_adjust_weight=loss_adjust_weight,
                                       ORT_weight=ORT_weight, MIT_weight=MIT_weight)
        self.customized_loss_func = customized_loss_func

    def forward(self, inputs: dict, training: bool=True, return_diagnostics: bool=True):
        """Show the inference assembly; training and diagnostics are separate."""
        if training:
            raise NotImplementedError("Training objectives are outside this interface snapshot.")
        if return_diagnostics:
            raise NotImplementedError("Diagnostic operators are outside this interface snapshot.")
        observed = inputs["X"]
        mask = inputs["missing_mask"]
        normalized = self.revin(observed, mask, mode="norm")
        global_estimate, _, _, _ = self.TS_model(inputs["X_TS"], self.TS_freqs_params)
        local = self.residual_model(X_local=normalized, missing_mask=mask,
                                    X_global=global_estimate, return_diagnostics=False)
        restored = self.revin(local["imputed_data"], mask, mode="denorm")
        return {"imputed_data": mask * observed + (1 - mask) * restored}
