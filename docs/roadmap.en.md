# AXIOS Roadmap 🗺️

## The Run Ladder (Operational Phases)

AXIOS follows a strict progression model to manage risk from development to production.

| Phase | Name | Description | Risk Level |
| :---: | :--- | :--- | :---: |
| **L0** | Sandbox | Synthetic data, local logic tests | None |
| **L1** | Paper | Real-time data, paper broker, zero capital risk | None |
| **L2** | Micro-Live | Strictly capped live orders, forensic audit required | Low |
| **L3** | Production | Full-scale execution, restricted access | High |

## Gating Rules
- **L0 → L1**: Must pass all unit tests and local verification.
- **L1 → L2**: Requires 72h+ stable paper run + manual sign-off.
- **L2 → L3**: Requires complete audit trail review + external validation.

## Operational Capabilities (Abstracted)
| Capability | Status |
| :--- | :--- |
| Automated Preflight (Proof-6) | ✅ Implemented |
| Cron-based Scheduling | ✅ Implemented |
| Kill-Switch Hierarchy | ✅ Implemented |
| Forensic JSONL Traces | ✅ Implemented |
| Multi-Account Sentinel | ✅ Designed |
| Real-time Monitoring Dashboard | 🔜 Planned |

## Future Enhancements
- Multi-exchange support (abstracted)
- Advanced regime detection
- Automated incident response
