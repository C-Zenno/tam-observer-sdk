# TAM Observer Doctrine

**Observer Edition | Phase A | Diagnostic Instrument**

This document defines the constraints and principles governing the TAM Observer SDK.

---

## Core Doctrine: Observer-Only

The TAM Observer is a **diagnostic instrument**, not a trading system.

### What It Does

1. **Observes** — Reads market data
2. **Classifies** — Labels intervals as admissible/inadmissible
3. **Attributes** — Identifies dominant failure modes
4. **Records** — Produces immutable diagnostic records

### What It Does NOT Do

1. **Predict** — No forecasting of future states
2. **Recommend** — No trade signals or action suggestions
3. **Optimize** — No parameter tuning or threshold adjustment
4. **Control** — No writes to external systems
5. **Interpret** — No semantic meaning is assigned to labels beyond classification

---

## Language Constraints

All outputs use **past-tense, observational language**:

| Allowed | Forbidden |
|---------|-----------|
| "was classified as" | "will be" |
| "exhibited" | "should" |
| "recorded" | "predicts" |
| "observed" | "recommends" |

---

## Parameter Policy

### Fixed Constraints (Inputs)

These describe the execution environment and are provided by the user:

- `friction_floor` — Execution friction (immutable per session)
- `min_move` — Minimum required move (immutable per session)

### Internal Constants (Frozen)

These are set by the observer and never exposed:

- Window sizes
- Threshold values
- Normalization parameters

**Rule:** Internal constants are hashed, not configurable.

---

## Artifact Integrity

All observer outputs maintain:

1. **Hash chains** — Each record links to previous via cryptographic hash
2. **Append-only** — No modifications to historical records
3. **Determinism** — Same inputs always produce same outputs
4. **Traceability** — All outputs link to input data and version

---

## Liability Boundary

The TAM Observer:

- Does NOT constitute financial advice
- Does NOT recommend any trading action
- Does NOT predict market movements
- Does NOT guarantee any outcome

Users are solely responsible for any actions taken based on observer outputs.

---

## Version

This doctrine applies to TAM Observer SDK v0.1.x.

Changes to this doctrine require a major version increment.
