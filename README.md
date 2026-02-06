# TAM Observer SDK

**Trading Admissibility Mapper — Observer Edition**

## Overview

This repository provides a **non-authoritative, observer-only evaluation SDK**
intended solely for **research, demonstration, and educational use**.

The software enables descriptive inspection of market intervals and emits bounded,
machine-readable admissibility classifications. It **does not** provide decisions,
recommendations, controls, or operational authority of any kind.

> This SDK is **not licensed for production use**, system integration,
> automation at scale, decision-making, or commercial deployment.

Use of this repository is governed by the **Observer Evaluation License (OEL-1.0)**.
By cloning, running, or modifying this software, you agree to those terms.

If you are seeking production, embedded, or commercial use, this repository
is not the appropriate artifact. Contact the authors for licensed SDKs,
applications, or certification frameworks.

> **Note:** This repo is an automated subtree export. Contributions should be opened against the source monorepo, not here.

---

## What This Is

TAM Observer classifies market intervals as **admissible** or **inadmissible** based on execution constraints. It answers:

> "Given my execution friction and minimum required move, is this interval structurally admissible under stated execution constraints?"

## What This Is NOT

This SDK does **not**:

- Predict future prices or market movements
- Recommend trades or generate entry/exit signals
- Optimize parameters or tune thresholds
- Provide financial advice of any kind
- Provide any indication that a trade *should* or *should not* be taken

It is a **diagnostic instrument**, not a trading system.

## Installation

```bash
pip install tam-observer  # available with first public release
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

## Contracts

Receipt Envelope (RE-V0) and Export Discipline (ED-V0) live in [`C-Zenno/zoa-contracts`](https://github.com/C-Zenno/zoa-contracts).

## License

**Observer Evaluation License (OEL-1.0)**

This software is provided for non-authoritative, observer-only evaluation purposes only.
See [LICENSE](LICENSE) for full terms.

## Disclaimer

This software operates strictly in an observer-only capacity.

- It does not make decisions
- It does not provide recommendations
- It does not control or influence systems
- It does not predict outcomes
- It does not optimize behavior
- It does not certify admissibility, safety, or correctness

All outputs are descriptive artifacts produced for evaluation purposes only.
Any interpretation or use of outputs is solely the responsibility of the user.

This software must not be used where decisions, automation, or operational
authority are required.

See [DISCLAIMER.md](DISCLAIMER.md) for full disclaimer.
