"""
TAM Observer — Main Entry Point

Observer Edition | Diagnostic Instrument | No Predictions

This module provides the TAMObserver class for classifying trading data.
It is read-only, diagnostic-only, and non-predictive.
"""

from dataclasses import dataclass
from typing import Iterator, List, Sequence

from .types import (
    AdmissibilityState,
    DominantMode,
    ExecutionConstraints,
    ObservationRecord,
)


@dataclass
class OHLCVBar:
    """Single OHLCV bar. Immutable input data."""
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: float


class TAMObserver:
    """
    Trading Admissibility Mapper — Observer Interface.

    This class observes OHLCV data and classifies each bar's admissibility.
    It does NOT:
    - Predict future prices or states
    - Recommend trades or actions
    - Optimize parameters or thresholds
    - Generate entry/exit signals

    It DOES:
    - Classify past states as admissible or inadmissible
    - Attribute dominant failure modes
    - Detect boundary events between states

    Internal constants are implementation details and carry no semantic meaning.

    Usage:
        constraints = ExecutionConstraints(friction_floor=0.0015, min_move=0.01)
        observer = TAMObserver(constraints)

        for record in observer.observe(bars):
            print(f"{record.timestamp}: {record.state.value}")
    """

    __WINDOW_SIZE = 64  # Internal constant; value is non-semantic

    def __init__(self, constraints: ExecutionConstraints):
        """
        Initialize the observer with execution constraints.

        Args:
            constraints: Fixed execution environment parameters.
                         These are not tunable — they describe the environment.
        """
        self._constraints = constraints

    @property
    def constraints(self) -> ExecutionConstraints:
        """Return the execution constraints (read-only)."""
        return self._constraints

    def observe(self, bars: Sequence[OHLCVBar]) -> Iterator[ObservationRecord]:
        """
        Observe a sequence of OHLCV bars and yield admissibility records.

        This is the main entry point for the observer.
        It processes each bar and yields a diagnostic record.

        Args:
            bars: Sequence of OHLCV bars to observe.

        Yields:
            ObservationRecord for each bar.

        Note:
            The observer requires a minimum window of data before
            producing meaningful classifications. Early records may
            have reduced diagnostic confidence.
        """
        # Placeholder implementation
        # Full implementation imports from core/ (internal)
        for bar in bars:
            yield self._observe_single(bar)

    def _observe_single(self, bar: OHLCVBar) -> ObservationRecord:
        """
        Observe a single bar. Internal method.

        This is a placeholder. The real implementation uses
        the internal core/ module which is not exported.
        """
        # Placeholder: return basin state for all bars
        # Real implementation uses geometry evaluation
        return ObservationRecord(
            timestamp=bar.timestamp,
            state=AdmissibilityState.BASIN,
            dominant_mode=DominantMode.FRICTION_LETHAL,
            friction_floor=self._constraints.friction_floor,
            min_move=self._constraints.min_move,
            m_req=self._constraints.m_req,
            diagnostics={},  # Opaque; populated by real implementation
        )

    def observe_batch(self, bars: Sequence[OHLCVBar]) -> List[ObservationRecord]:
        """
        Observe all bars and return a list of records.

        Convenience method for non-streaming use.

        Args:
            bars: Sequence of OHLCV bars.

        Returns:
            List of ObservationRecord for each bar.
        """
        return list(self.observe(bars))
