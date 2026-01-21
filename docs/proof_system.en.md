# AXIOS Proof System 🛡️

[Deutsch](#deutsch)

## The Philosophy of "Forensic Integrity"
AXIOS is built on the principle that execution is only valid if it is auditable. Every run must produce a **Proof Pack**—a self-contained, cryptographically signed set of evidence.

## The Proof-6 Gates
The Proof-6 system is a series of deterministic checkpoints that must be passed before the system enters its execution loop.

1. **G1: INTEGRITY**
   - **Check**: Validates that the codebase matches the authorized repository state.
   - **Artifact**: `run_manifest.json` (SHA256 hashed).

2. **G2: CONNECTIVITY**
   - **Check**: Pings the exchange and sentinel endpoints.
   - **Threshold**: Latency must be < 50ms (configurable).

3. **G3: RISK_CAPS**
   - **Check**: Validates that all positions are within the strict risk factor limits (e.g., max 0.5x exposure).
   - **Implementation**: Deterministic RiskV5 Controller.

4. **G4: SENTINEL**
   - **Check**: Verifies that the external safety sentinel is alive and monitoring all account balances.

5. **G5: COMPLIANCE**
   - **Check**: Ensures all logging handlers are active and writing to the forensic JSONL trace.

6. **G6: HANDOFF**
   - **Check**: Bundles all previous gate results and states into a ZIP file with a detached SHA256 signature.

---

## Artifact Anatomy
- **`run_manifest.json`**: The identity of the run (ID, timestamp, mode).
- **`gate_report.json`**: The pass/fail status of each gate.
- **`agent_trace.jsonl`**: Every internal state transition of the orchestrator.
- **`reconcile_report.jsonl`**: Detailed audit of Local vs Exchange state.

---

<br id="deutsch">

# AXIOS Proof System 🛡️

[English](#axios-proof-system-)

## Philosophie der forensischen Integrität
AXIOS basiert auf dem Prinzip, dass eine Ausführung nur dann valide ist, wenn sie auditierbar ist. Jeder "Run" produziert ein **Proof Pack**.

## Die Proof-6 Gates
1. **G1: INTEGRITÄT**: Prüft den Code-Zustand gegen bekannte Hashes.
2. **G2: KONNEKTIVITÄT**: Latenzprüfung zur Börse (< 50ms).
3. **G3: RISK_CAPS**: Harte Durchsetzung von Expositionslimits.
4. **G4: SENTINEL**: Externer Sicherheits-Wächter aktiv.
5. **G5: COMPLIANCE**: Forensische Logs aktiv.
6. **G6: HANDOFF**: Bündelung und Signierung aller Daten.
