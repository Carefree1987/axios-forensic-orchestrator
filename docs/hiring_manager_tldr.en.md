# Hiring Manager TL;DR 🎯

## The Problem
Most algorithmic trading systems fail silently. When they do fail, there's no way to understand *what happened* or *why*. This leads to:
- Unexplained capital losses
- Inability to reproduce bugs
- Zero accountability in execution

## The Solution: AXIOS
AXIOS is a **Forensic-Grade Trading Orchestrator**. It treats every execution run as a court case: everything must be documented, timestamped, and verifiable.

### Core Innovations
| Feature | What It Does |
| :--- | :--- |
| **Proof-6 Gates** | 6 mandatory checkpoints that must PASS before any trade |
| **Exchange-as-Truth** | Local state is secondary; broker balance is the only source of truth |
| **Handoff ZIP** | Every run produces a non-repudiable evidence archive |
| **Run Ladder (L0-L3)** | Strict progression from sandbox to production |

## Tech Highlights
- **Languages**: Python (typed), Bash
- **Infra**: Docker-ready, CI/CD, Linux-hardened
- **Security**: Zero secrets in repo, automated `detect-secrets` scans
- **Testing**: Synthetic proof packs for safe demonstration

## What You Can Evaluate in 90 Seconds
1. Clone this repo
2. Run: `python scripts/verify_synthetic_pack.py examples/proof_pack_synthetic/golden_a1b2c3d4`
3. See: `GLOBAL STATUS: PASS`

**That's the discipline Dennis brings to every system he builds.**

---

## About Dennis
- Architected the entire AXIOS system from scratch
- Built the Proof-6 safety protocol
- Designed the "Exchange-as-Truth" reconciliation engine
- Handles all DevOps/Server hardening (Hetzner Cloud)

[LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/Carefree1987)
