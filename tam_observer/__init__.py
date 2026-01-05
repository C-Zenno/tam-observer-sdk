"""
TAM Observer SDK — Trading Admissibility Mapper

Observer Edition | Diagnostic Instrument | No Predictions

This SDK provides read-only admissibility classification for trading data.
It does NOT provide trade signals, recommendations, or predictions.
"""

__version__ = "0.1.0"

from .observer import TAMObserver
from .types import (
    AdmissibilityState,
    DominantMode,
    ObservationRecord,
    ExecutionConstraints,
)

__all__ = [
    "TAMObserver",
    "AdmissibilityState",
    "DominantMode",
    "ObservationRecord",
    "ExecutionConstraints",
]
