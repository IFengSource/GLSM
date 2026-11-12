"""Selected settings by dataset."""

# Copyright (c) 2026, Yuan Feng <fengyuan2022@zju.edu.cn>
# SPDX-License-Identifier: BSD-3-Clause

from .ett_h1 import ETT_h1
from .wind_turbine import wind_turbine
from .italy_air import ItalyAir
from .guangzhou_traffic import GuangzhouTraffic

HPO_RESULTS = {
    "ETT_h1": ETT_h1,
    "wind_turbine": wind_turbine,
    "ItalyAir": ItalyAir,
    "GuangzhouTraffic": GuangzhouTraffic,
}
