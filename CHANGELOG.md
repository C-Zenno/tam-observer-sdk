# Changelog

All notable changes to the TAM Observer SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-01-05

### Added

- Initial public release of TAM Observer SDK
- `TAMObserver` class for admissibility classification
- `ExecutionConstraints` for declaring execution environment
- `ObservationRecord` with opaque diagnostics
- Admissibility state labels: `basin`, `tension`, `escape`, `invalidated`, `exhausted`
- Dominant mode attribution for classification reasoning
- Observer Edition doctrine documentation
- Basic usage example

### Documentation

- `README.md` with quick start guide
- `doctrine.md` defining observer-only constraints
- `NOTE_TRADING_OBSERVER.md` certification-adjacent anchor document
- `NOTE_OBSERVER_NEUTRAL.md` domain-neutral variant for governance review

### Security

- Observer-only architecture (read-only, no control surfaces)
- Opaque diagnostics (non-normative, version-unstable)
- Past-tense language constraint enforcement
