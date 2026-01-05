"""
TAM Observer SDK — Basic Usage Example

This example demonstrates how to use the TAM Observer
to classify trading data admissibility.

NOTE: This is a diagnostic tool, not a trading system.
It does NOT provide trading signals or recommendations.
"""

from tam_observer import (
    TAMObserver,
    ExecutionConstraints,
)
from tam_observer.observer import OHLCVBar


def main():
    # Define execution environment constraints
    # These are NOT tunable parameters — they describe YOUR trading environment
    constraints = ExecutionConstraints(
        friction_floor=0.0015,  # 0.15% execution friction (spread + fees + slippage)
        min_move=0.01,          # 1% minimum required move for viable execution
    )

    print(f"Execution Constraints:")
    print(f"  friction_floor: {constraints.friction_floor:.4f} ({constraints.friction_floor*100:.2f}%)")
    print(f"  min_move: {constraints.min_move:.4f} ({constraints.min_move*100:.2f}%)")
    print(f"  m_req: {constraints.m_req:.4f} ({constraints.m_req*100:.2f}%)")
    print()

    # Create observer with constraints
    observer = TAMObserver(constraints)

    # Sample OHLCV data (replace with your data source)
    bars = [
        OHLCVBar("2025-01-02T09:30:00", 100.00, 100.50, 99.80, 100.20, 1000000),
        OHLCVBar("2025-01-02T09:45:00", 100.20, 101.00, 100.10, 100.90, 1200000),
        OHLCVBar("2025-01-02T10:00:00", 100.90, 102.50, 100.80, 102.30, 1500000),
        OHLCVBar("2025-01-02T10:15:00", 102.30, 102.80, 101.50, 101.80, 1100000),
        OHLCVBar("2025-01-02T10:30:00", 101.80, 102.00, 101.00, 101.20, 900000),
    ]

    # Observe and classify
    print("Observations:")
    print("-" * 70)

    for record in observer.observe(bars):
        print(f"{record.timestamp}")
        print(f"  Classification: {record.state.value}")
        print(f"  Dominant Mode: {record.dominant_mode.value}")
        print()

    print("-" * 70)
    print()
    print("REMINDER: These are diagnostic classifications, not trading signals.")
    print("The observer does NOT recommend any trading action.")


if __name__ == "__main__":
    main()
