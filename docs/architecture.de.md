# AXIOS Systemarchitektur 🏗️

[English](architecture.en.md)

## Übersicht
AXIOS ist ein modularer Trading-Orchestrator, der für hochzuverlässige Ausführung konzipiert wurde. Im Gegensatz zu herkömmlichen Trading-Bots behandelt AXIOS jeden Ausführungslauf als forensisches Ereignis, das durch Artefakte belegt werden muss.

## Kernschichten

### 1. Intelligence Layer (Horus)
- **Rolle**: Signalgenerierung und Marktanalyse (Market Regime Detection).
- **Unabhängigkeit**: Horus fungiert als zustandsloser Berater. AXIOS akzeptiert nur Signale, die strikte kryptographische und logische Schwellenwerte erfüllen.

### 2. Orchestration Layer (Der Kern)
- **Rolle**: Zustandsverwaltung und Durchsetzung von Sicherheitsregeln (Gates).
- **Philosophie**: "Gucken, dann Anfassen." Ohne positive Proof-6 Gates erfolgt keine Interaktion mit dem Broker.

### 3. Execution Layer (Broker Bridge)
- **Rolle**: Schnittstelle zu Kryptobörsen (z.B. Binance Futures).
- **Kontrolle**: Implementiert einen "Exchange-as-Truth"-Reconcile-Loop, der sicherstellt, dass der lokale Zustand immer das reale Kontoguthaben widerspiegelt.

---

## Die forensische Pipeline
Jeder Lauf folgt einem deterministischen Pfad:
1. **Bootstrap**: Laden der Konfiguration und Initialisierung sicherer Standardwerte.
2. **Preflight**: Ausführung der Proof-6 Gates. Abbruch bei Integritätsverletzung.
3. **Loop**: Ausführung der Strategie-Logik, State-Reconciliation und lückenloses Logging.
4. **Handoff**: Bündelung aller Logs und Zustände in ein fälschungssicheres ZIP-Archiv.
