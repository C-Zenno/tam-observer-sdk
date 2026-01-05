"""
TAM Observer Types

Observer Edition | Diagnostic Instrument | No Predictions
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AdmissibilityState(str, Enum):
    """
    Admissibility classification for a market interval.

    These are diagnostic labels, not trading signals.
    """
    BASIN = "basin"           # Structurally confined, friction-bound
    TENSION = "tension"       # Transitional, approaching boundary
    ESCAPE = "escape"         # Admissible excursion from basin
    INVALIDATED = "invalidated"  # Structure violated, observation suspended
    EXHAUSTED = "exhausted"   # Admissibility depleted, returning to basin


class DominantMode(str, Enum):
    """
    Attribution of why a state was classified as it was.

    Diagnostic only. Does not imply causation or prediction.
    """
    FRICTION_LETHAL = "friction_lethal"
    EXCURSION_HEADROOM = "excursion_headroom"
    REENTRY_RISK = "reentry_risk"
    REGIME_VETO = "regime_veto"
    STRUCTURE_INVALIDATED = "structure_invalidated"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class ExecutionConstraints:
    """
    Execution environment constraints.

    These are fixed inputs, not tunable parameters.
    They represent the trading environment, not optimization targets.
    """
    friction_floor: float  # Minimum execution friction (e.g., 0.0015 = 0.15%)
    min_move: float        # Minimum required move (e.g., 0.01 = 1%)

    @property
    def m_req(self) -> float:
        """Required move threshold: min_move + 2*friction_floor."""
        return self.min_move + 2 * self.friction_floor


@dataclass(frozen=True)
class ObservationRecord:
    """
    A single observation from the TAM observer.

    This is a diagnostic record, not a trading signal.
    All fields describe past state, not future expectation.
    """
    timestamp: str
    state: AdmissibilityState
    admissible: bool
    dominant_mode: DominantMode

    # Diagnostic metrics (all derived from past data)
    basin_compression: float
    escape_slope: float
    persistence: float
    excursion_headroom: float
    reentry_risk: float

    # Environment constraints (fixed, not tuned)
    friction_floor: float
    min_move: float
    m_req: float

    # Boundary events (if any)
    boundary_event: Optional[str] = None
    invalidation_reason: Optional[str] = None
