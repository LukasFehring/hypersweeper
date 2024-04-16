"""Config for HyperSMAC sweeper."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hydra.core.config_store import ConfigStore


@dataclass
class HyperSMACConfig:
    """Config for HyperSMAC sweeper."""

    _target_: str = "hydra_plugins.hyper_smac.hyper_smac.HyperSMAC"
    search_space: dict | None = field(default_factory=dict)
    resume: str | bool = False
    budget: Any | None = None
    budget_variable: str | None = None
    loading_variable: str | None = None
    saving_variable: str | None = None
    sweeper_kwargs: dict | None = field(default_factory=dict)


ConfigStore.instance().store(
    group="hydra/sweeper",
    name="HyperSMAC",
    node=HyperSMACConfig,
    provider="hypersweeper",
)
