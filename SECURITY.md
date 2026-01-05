# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in the TAM Observer SDK, please report it responsibly.

### How to Report

1. **Do not** open a public GitHub issue for security vulnerabilities
2. Email security concerns to the maintainers directly
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact assessment
   - Any suggested fixes (optional)

### What to Expect

- Acknowledgment within 48 hours
- Status update within 7 days
- Coordinated disclosure timeline discussion

### Scope

This security policy covers:

- The `tam_observer` Python package
- Example code in `examples/`
- Documentation that could lead to misuse

### Out of Scope

- Misuse of observer outputs as trading signals (this is a doctrine violation, not a security issue)
- Issues in dependencies (report to upstream maintainers)

## Security Design

The TAM Observer SDK is designed with security-by-architecture:

- **Read-only**: No writes to external systems
- **No network**: No outbound connections
- **No secrets**: No credential handling
- **Deterministic**: Same inputs produce same outputs
- **Observer-only**: No control surfaces or action triggers
