# AXIOS Sicherheitskonzept 🔐

[English](security.en.md)

## Security-First Design
Sicherheit ist in AXIOS kein Zusatz, sondern das Fundament. Das System ist darauf ausgelegt, institutionelle Risiken zu managen.

## Secret Management
- **Keine Hardcoded Secrets**: AXIOS nutzt Umgebungsvariablen und verschlüsselte lokale Speicher.
- **Showcase-Richtlinie**: Dieses Repo enthält **KEINE GEHEIMNISSE**. Alle API-Keys, IPs und Wallet-Adressen in Beispielen sind synthetisch oder geschwärzt.

## Defensive Execution
- **Kill-Switch Hierarchie**: Mehrstufiges Not-Aus-System (Manuell -> Logik-basiert -> Sentinel-erzwungen).
- **Netzwerk-Isolation**: Betrieb in isolierten VLANs mit strikten Outbound-Only Regeln vorgesehen.
