"""Local residual refinement Interface-only resource snapshot."""

# Copyright (c) 2026, Yuan Feng <fengyuan2022@zju.edu.cn>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Callable, Optional, Tuple, Union

import numpy as np
import torch
import torch.nn as nn


class MultiHopResidualImputer(nn.Module):
    """Local residual refinement; constructor names match the research project."""

    def __init__(self, n_features: int, n_steps: int, top_k: int=3, hidden_dim: int=64, dropout: float=0.1, num_layers: int=3, detach_global: bool=True, pos_dim: int=0):
        super().__init__()
        self.interface_configuration = {'n_features': n_features, 'n_steps': n_steps, 'top_k': top_k, 'hidden_dim': hidden_dim, 'dropout': dropout, 'num_layers': num_layers, 'detach_global': detach_global, 'pos_dim': pos_dim}

    def forward(self, X_local, missing_mask, X_global, return_diagnostics: bool=False):
        """Numerical operators will be supplied in a subsequent release."""
        raise NotImplementedError("This snapshot provides the component interface only.")
