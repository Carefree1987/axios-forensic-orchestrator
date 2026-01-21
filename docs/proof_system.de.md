# AXIOS Proof System 🛡️

[English](proof_system.en.md)

## Die Philosophie der "Forensischen Integrität"
AXIOS basiert auf dem Prinzip, dass eine Ausführung nur dann valide ist, wenn sie auditierbar ist. Jeder "Run" produziert ein **Proof Pack** – ein in sich geschlossener, kryptographisch signierter Satz von Beweismitteln.

## Die Proof-6 Gates
Das Proof-6 System besteht aus einer Reihe deterministischer Kontrollpunkte, die bestanden werden müssen, bevor das System in den Ausführungsmodus wechselt.

1. **G1: INTEGRITÄT**
   - **Check**: Validiert, dass der Code-Stand der autorisierten Repository-Baseline entspricht.

2. **G2: KONNEKTIVITÄT**
   - **Check**: Pings zu Börsen- und Sentinel-Endpunkten.
   - **Limit**: Latenz muss < 50ms sein.

3. **G3: RISK_CAPS**
   - **Check**: Strikte Einhaltung der Expositionslimits (z.B. max. 0,5x Hebel).

4. **G4: SENTINEL**
   - **Check**: Prüft, ob der externe Sicherheits-Wächter (Sentinel) aktiv ist.

5. **G5: COMPLIANCE**
   - **Check**: Sicherstellung, dass alle Logging-Handler aktiv sind.

6. **G6: HANDOFF**
   - **Check**: Bündelung aller Ergebnisse in ein ZIP mit abgesetzter SHA256-Signatur.
