# TAM Observer SDK

**Trading Admissibility Mapper — Observer Edition**

A diagnostic instrument for classifying trading admissibility. Observer-only, non-predictive.

## What This Is

TAM Observer classifies market intervals as **admissible** or **inadmissible** based on execution constraints. It answers:

> "Given my execution friction and minimum required move, is this interval structurally viable?"

## What This Is NOT

This SDK does **not**:

- Predict future prices or market movements
- Recommend trades or generate entry/exit signals
- Optimize parameters or tune thresholds
- Provide financial advice of any kind

It is a **diagnostic instrument**, not a trading system.

## Installation

```bash
pip install tam-observer
```

## Quick Start

```python
from tam_observer import TAMObserver, ExecutionConstraints, OHLCVBar

# Define your execution environment (not tunable parameters)
constraints = ExecutionConstraints(
    friction_floor=0.0015,  # 0.15% execution friction
    min_move=0.01,          # 1% minimum required move
)

# Create observer
observer = TAMObserver(constraints)

# Observe market data
bars = [
    OHLCVBar("2025-01-01T09:30:00", 100.0, 101.0, 99.5, 100.5, 1000000),
    OHLCVBar("2025-01-01T09:45:00", 100.5, 102.0, 100.0, 101.8, 1200000),
    # ... more bars
]

for record in observer.observe(bars):
    print(f"{record.timestamp}: {record.state.value} (admissible={record.admissible})")
```

## States

| State | Meaning |
|-------|---------|
| `basin` | Structurally confined, friction-bound |
| `tension` | Transitional, approaching boundary |
| `escape` | Admissible excursion from basin |
| `invalidated` | Structure violated |
| `exhausted` | Admissibility depleted |

## Dominant Modes

Each observation includes a `dominant_mode` that attributes why the state was classified:

- `friction_lethal` — Execution friction exceeds available move
- `excursion_headroom` — Limited room for admissible excursion
- `reentry_risk` — High risk of returning to basin
- `regime_veto` — Market regime incompatible with admissibility
- `structure_invalidated` — Underlying structure violated

## Doctrine

This SDK adheres to **Observer Edition** constraints:

1. **Read-only** — No writes to external systems
2. **Diagnostic-only** — Labels, not recommendations
3. **Non-predictive** — Past-tense observations only
4. **Immutable** — All records are append-only

## License

Apache 2.0

## Disclaimer

This software is a diagnostic tool for analytical purposes only. It does not constitute financial advice, trading recommendations, or investment guidance. Use at your own risk.
