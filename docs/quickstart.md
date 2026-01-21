# Quickstart Guide 🚀

[Deutsch](#deutsch)

## Prerequisites
- Python 3.10+
- Git

## 1. Clone the Repository
```bash
git clone https://github.com/Carefree1987/axios-forensic-orchestrator.git
cd axios-forensic-orchestrator
```

## 2. Generate a Synthetic Proof Pack
```bash
python scripts/generate_synthetic_proof_pack.py
```
This will create a new pack in `examples/proof_pack_synthetic/run_<id>/`.

## 3. Verify the Proof Pack
```bash
python scripts/verify_synthetic_pack.py examples/proof_pack_synthetic/run_8a2b3c4d
```
Expected output: `GLOBAL STATUS: PASS`.

---

<br id="deutsch">

# Schnellstart-Anleitung 🚀

[English](#quickstart-guide-)

## Voraussetzungen
- Python 3.10+
- Git

## 1. Repository klonen
```bash
git clone https://github.com/Carefree1987/axios-forensic-orchestrator.git
cd axios-forensic-orchestrator
```

## 2. Synthetisches Proof Pack erstellen
```bash
python scripts/generate_synthetic_proof_pack.py
```

## 3. Proof Pack verifizieren
```bash
python scripts/verify_synthetic_pack.py examples/proof_pack_synthetic/run_8a2b3c4d
```
Erwartetes Ergebnis: `GLOBAL STATUS: PASS`.
