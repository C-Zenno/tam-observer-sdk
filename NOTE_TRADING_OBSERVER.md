# Structural Admissibility Note: Trading (Observer Edition)

**Phase A — Diagnostic Instrument (Observer-Only)**
**Applies to:** TAM Observer SDK v0.1.x

## Summary

This note defines what the TAM Observer measures, what its labels mean, and what the system explicitly refuses to do. TAM is an **observer-only diagnostic instrument** intended to support structural auditability of automated trading systems under **stated execution constraints**. It does not predict markets, recommend actions, or optimize strategies.

---

## 1. Purpose

Trading systems often fail not because data is missing, but because **execution constraints** make continuation structurally inadmissible (fees, spreads, slippage, liquidity frictions, regime incompatibility, or boundary violations). TAM provides **read-only classification** of whether observed intervals were admissible under a declared execution environment.

TAM answers a single question:

> **Given stated execution constraints, was this observed interval admissible or inadmissible?**

---

## 2. Non-Goals (Hard Boundaries)

TAM is not a trading system and must not be used as one.

TAM does **not**:

* forecast future prices, volatility, or regimes
* provide trade signals, entries, exits, position sizing, or timing
* recommend any action, including "take" or "avoid" a trade
* optimize parameters or tune thresholds for performance
* execute, route, place, or modify orders
* function as a control layer for any live system

TAM produces **labels and diagnostics only**, describing past observations under stated constraints.

---

## 3. Inputs

TAM consumes two categories of inputs:

### 3.1 Market Observation Data

* Time-indexed OHLCV (or comparable bar/interval representation)

### 3.2 Execution Constraints (Declared Environment)

These are **fixed per session** and represent the user's execution environment, not tunable strategy parameters:

* `friction_floor` — minimum execution friction (fees + spread + slippage floor)
* `min_move` — minimum required move for structural viability under the user's mandate

TAM may derive an internal requirement such as:

* `m_req` — a required move threshold derived from declared constraints

---

## 4. Outputs (Labels Only)

TAM emits **classification records**. Each record includes:

* an **admissibility state label**
* a **dominant mode** attribution describing the primary limiting factor
* optional **diagnostics** (opaque, descriptive values; non-normative)

### 4.1 Admissibility States (Observer Labels)

The following labels are **diagnostic classifications**, not action triggers:

* `basin` — observed interval was structurally confined under constraints
* `tension` — observed interval was transitional, approaching a boundary
* `escape` — observed interval exhibited an admissible excursion under constraints
* `invalidated` — structural violation detected; observation suspended or flagged
* `exhausted` — admissibility was depleted; structure returning toward confinement

### 4.2 Dominant Modes (Attribution)

Dominant modes provide attribution for *why* a label was assigned (diagnostic only):

* `friction_lethal`
* `excursion_headroom`
* `reentry_risk`
* `regime_veto`
* `structure_invalidated`
* `unknown`

**Interpretation constraint:** No semantic meaning beyond classification is assigned to these labels. They do not imply profit, edge, or a recommended response.

---

## 5. Language Constraint (Past-Tense Only)

All TAM outputs use observational, past-tense language:

* "was classified as"
* "exhibited"
* "was observed"
* "was recorded"

TAM must not output:

* "will"
* "should"
* "recommended"
* "expected return"
* "buy/sell/hold"

This constraint is intentional: it preserves the observer boundary.

---

## 6. Determinism and Auditability

For a given:

* input data
* declared constraints
* SDK version

…the observer should produce consistent classifications. Where the SDK includes integrity mechanisms (e.g., record chaining, hashes, or trace links), they are intended to support auditability and evidentiary review.

**Important:** diagnostic values may evolve across versions and are not guaranteed comparable between releases.

---

## 7. Liability Boundary

TAM is provided for analytical and diagnostic purposes only. It does not constitute financial advice, trading recommendations, or investment guidance. Users remain solely responsible for any actions taken.

---

## 8. Versioning

This note applies to **TAM Observer SDK v0.1.x**.
Changes to doctrine-level constraints (observer-only boundary, non-goals, output semantics) require a **major version increment**.

---

## Appendix: Practical Use (Non-Prescriptive)

**Permitted uses:**

* annotating backtests with admissibility labels (as metadata)
* auditing strategy behavior under friction assumptions
* generating evidence logs for structural review
* comparing constraint environments (by changing declared execution constraints)

**Prohibited uses:**

* converting labels into trade triggers
* optimizing around labels to increase returns
* routing execution decisions through TAM
