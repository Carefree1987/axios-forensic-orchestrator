# AXIOS Roadmap 🗺️

## Die Run-Leiter (Operative Phasen)

AXIOS folgt einem strikten Progressionsmodell zur Risikokontrolle.

| Phase | Name | Beschreibung | Risikolevel |
| :---: | :--- | :--- | :---: |
| **L0** | Sandbox | Synthetische Daten, lokale Logik-Tests | Keines |
| **L1** | Paper | Echtzeit-Daten, Paper-Broker, kein Kapitalrisiko | Keines |
| **L2** | Micro-Live | Strikt begrenzte Live-Orders, forensischer Audit erforderlich | Niedrig |
| **L3** | Produktion | Vollskala-Ausführung, eingeschränkter Zugang | Hoch |

## Gating-Regeln
- **L0 → L1**: Alle Unit-Tests und lokale Verifikation bestanden.
- **L1 → L2**: Erfordert 72h+ stabilen Paper-Lauf + manuelle Freigabe.
- **L2 → L3**: Erfordert kompletten Audit-Trail-Review + externe Validierung.

## Operative Fähigkeiten (Abstrahiert)
| Fähigkeit | Status |
| :--- | :--- |
| Automatisierter Preflight (Proof-6) | ✅ Implementiert |
| Cron-basiertes Scheduling | ✅ Implementiert |
| Kill-Switch Hierarchie | ✅ Implementiert |
| Forensische JSONL Traces | ✅ Implementiert |
| Multi-Account Sentinel | ✅ Konzipiert |
| Echtzeit-Monitoring Dashboard | 🔜 Geplant |

## Zukünftige Erweiterungen
- Multi-Exchange Support (abstrahiert)
- Erweiterte Regime-Erkennung
- Automatisierte Incident Response
