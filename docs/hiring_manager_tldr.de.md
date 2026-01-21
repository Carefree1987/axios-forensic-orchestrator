# Hiring Manager TL;DR 🎯

## Das Problem
Die meisten algorithmischen Handelssysteme scheitern lautlos. Wenn sie scheitern, gibt es keine Möglichkeit zu verstehen, *was passiert ist* oder *warum*. Das führt zu:
- Unerklärlichen Kapitalverlusten
- Unmöglichkeit, Bugs zu reproduzieren
- Null Accountability bei der Ausführung

## Die Lösung: AXIOS
AXIOS ist ein **forensischer Trading-Orchestrator**. Er behandelt jeden Ausführungslauf wie einen Gerichtsfall: Alles muss dokumentiert, zeitgestempelt und verifizierbar sein.

### Kern-Innovationen
| Feature | Was es tut |
| :--- | :--- |
| **Proof-6 Gates** | 6 obligatorische Checkpoints, die BESTANDEN werden müssen |
| **Exchange-as-Truth** | Lokaler State ist sekundär; Broker-Balance ist einzige Wahrheit |
| **Handoff ZIP** | Jeder Lauf produziert ein fälschungssicheres Beweis-Archiv |
| **Run Ladder (L0-L3)** | Strikte Progression von Sandbox bis Produktion |

## Tech Highlights
- **Sprachen**: Python (typisiert), Bash
- **Infra**: Docker-ready, CI/CD, Linux-gehärtet
- **Security**: Keine Secrets im Repo, automatisierte `detect-secrets` Scans
- **Testing**: Synthetische Proof Packs für sichere Demonstration

## Was Sie in 90 Sekunden evaluieren können
1. Dieses Repo klonen
2. Ausführen: `python scripts/verify_synthetic_pack.py examples/proof_pack_synthetic/golden_a1b2c3d4`
3. Sehen: `GLOBAL STATUS: PASS`

**Das ist die Disziplin, die Dennis in jedes System einbringt.**

---

## Über Dennis
- Hat die gesamte AXIOS-Architektur von Grund auf entworfen
- Das Proof-6 Sicherheitsprotokoll implementiert
- Die "Exchange-as-Truth" Reconciliation-Engine gebaut
- Verantwortet das gesamte DevOps/Server-Hardening (Hetzner Cloud)

[LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/Carefree1987)
