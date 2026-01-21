# AXIOS System Architecture 🏗️

[Deutsch](#deutsch)

## Overview
AXIOS is a modular trading orchestrator built for high-reliability execution. Unlike traditional trading bots, AXIOS treats every execution run as a forensic event that must be justified through artifacts.

## Core Layers

### 1. Intelligence Layer (Horus)
- **Role**: Signal generation and market regime detection.
- **Independence**: Horus acts as a stateless advisor. AXIOS only accepts signals that meet strict cryptographic and logical thresholds.

### 2. Orchestration Layer (The Core)
- **Role**: State management and gate enforcement.
- **Philosophy**: "Verify, then Execute." The core will refuse to touch the broker interface unless all Proof-6 gates are green.

### 3. Execution Layer (Broker Bridge)
- **Role**: Interface with exchanges (e.g., Binance Futures).
- **Control**: Implements an "Exchange-as-Truth" reconcile loop, ensuring that the local state always reflects the actual account balance and positions.

---

## The Forensic Pipeline
Each run follows this deterministic path:
1. **Bootstrap**: Load configuration and initialize safe-defaults.
2. **Preflight**: Run Proof-6 gates. Fail fast if integrity is compromised.
3. **Loop**: Execute strategy logic, reconcile state, and log every decision.
4. **Handoff**: Bundle all logs and states into a non-repudiable ZIP archive.

---

<br id="deutsch">

# AXIOS Systemarchitektur 🏗️

[English](#axios-system-architecture-)

## Übersicht
AXIOS ist ein modularer Trading-Orchestrator, der für hochzuverlässige Ausführung konzipiert wurde. Im Gegensatz zu herkömmlichen Trading-Bots behandelt AXIOS jeden Ausführungslauf als forensisches Ereignis, das durch Artefakte belegt werden muss.

## Kernschichten

### 1. Intelligence Layer (Horus)
- **Rolle**: Signalgenerierung und Marktanalyse.
- **Unabhängigkeit**: Horus fungiert als zustandsloser Berater.

### 2. Orchestration Layer (Der Kern)
- **Rolle**: Zustandsverwaltung und Durchsetzung von Sicherheitsregeln.
- **Philosophie**: "Gucken, dann Anfassen." Ohne positive Proof-6 Gates erfolgt keine Broker-Interaktion.

### 3. Execution Layer (Broker Bridge)
- **Rolle**: Schnittstelle zu Börsen.
- **Kontrolle**: "Exchange-as-Truth"-Reconcile-Loop sorgt für Datenkonsistenz.
