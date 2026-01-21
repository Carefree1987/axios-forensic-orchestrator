# Recruiter FAQ 💼

## Q: What am I looking at exactly?
**A**: AXIOS is a "trading orchestrator." It’s the layer that sits between raw market data/signals and the actual execution on an exchange. Its job is to ensure that trading is safe, auditable, and compliant with risk limits.

## Q: Why is the code so focused on "Forensics"?
**A**: In high-stakes trading, "what happened" is just as important as "how much did we make." Forensics allow Dennis (the developer) to pinpoint exactly why a trade was taken, which security gate passed it, and what the network latency was at that exact microsecond. This is what makes it "institutional-grade."

## Q: Is this a bot that anyone can use?
**A**: No. It is a specialized tool. In this showcase, the core proprietary execution engines are abstracted to demonstrate the **architecture** and **discipline**, which are more important for evaluating a senior developer than raw trading strategies.

## Q: What does Dennis's role involve in this project?
**A**: Dennis designed the entire architecture from scratch, implemented the Proof-6 safety protocol, built the "Exchange-as-Truth" reconciliation engine, and handles the DevOps/Server hardening required to run this in a production cloud environment (Hetzner).

---

## Q: Was genau sehe ich hier?
**A**: AXIOS ist ein "Trading Orchestrator". Es ist die Schicht zwischen Marktdaten/Signalen und der Börse. Er sorgt dafür, dass der Handel sicher, auditierbar und regelkonform ist.

## Q: Warum liegt der Fokus so stark auf "Forensik"?
**A**: Im Hochrisiko-Trading ist das "Warum" entscheidend. Forensik ermöglicht es, jede Entscheidung sekundengenau zu belegen. Das macht das System "institutionell".

## Q: Was war Dennis' Rolle?
**A**: Dennis hat die Architektur entworfen, das Proof-6 Protokoll implementiert, die Reconcile-Engine gebaut und das gesamte Server-Hardening (Hetzner) übernommen.
