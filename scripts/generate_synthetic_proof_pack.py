import json
import hashlib
import os
import random
import time
from datetime import datetime, timezone

def generate_pack(run_id=None):
    if not run_id:
        run_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]
    
    base_dir = f"examples/proof_pack_synthetic/run_{run_id}"
    os.makedirs(base_dir, exist_ok=True)
    
    timestamp = datetime.now(timezone.utc).isoformat()
    
    # 1. run_manifest.json
    manifest = {
        "run_id": run_id,
        "timestamp": timestamp,
        "mode": "PAPER_L1",
        "market": "BTCUSDT",
        "exchange": "BINANCE_FUTURES",
        "declared_symbols": ["BTCUSDT"],
        "version": "1.3.0-golden"
    }
    # Force LF endings for SHA256 integrity
    with open(f"{base_dir}/run_manifest.json", "w", newline='\n') as f:
        json.dump(manifest, f, indent=2)
    
    # 2. gate_report.json
    report = {
        "overall_status": "PASS",
        "gates": [
            {"name": "INTEGRITY", "status": "PASS", "score": 10.0},
            {"name": "CONNECTIVITY", "status": "PASS", "score": 10.0},
            {"name": "RISK_CAPS", "status": "PASS", "score": 10.0},
            {"name": "SENTINEL", "status": "PASS", "score": 10.0},
            {"name": "COMPLIANCE", "status": "PASS", "score": 10.0},
            {"name": "HANDOFF", "status": "PASS", "score": 10.0}
        ]
    }
    with open(f"{base_dir}/gate_report.json", "w", newline='\n') as f:
        json.dump(report, f, indent=2)
    
    # 3. verify_proof_6.txt (EXACT 6 lines)
    proof_lines = [
        f"G1_INTEGRITY: PASS | HASH: {hashlib.sha256(b'code').hexdigest()[:12]}",
        "G2_CONNECTIVITY: PASS | LATENCY: 12ms",
        "G3_RISK_CAPS: PASS | EXPOSURE: < 0.5x",
        "G4_SENTINEL: PASS | HEARTBEAT: ACTIVE",
        "G5_COMPLIANCE: PASS | TRACE: CLEAN",
        f"G6_HANDOFF: PASS | ZIP_SHA: {hashlib.sha256(b'pack').hexdigest()[:12]}"
    ]
    with open(f"{base_dir}/verify_proof_6.txt", "w", newline='\n') as f:
        f.write("\n".join(proof_lines) + "\n")
    
    # 4. manifest_sha256.txt
    file_hashes = []
    # Sort files to ensure deterministic manifest order
    files = sorted([f for f in os.listdir(base_dir) if f != "manifest_sha256.txt"])
    for f in files:
        with open(f"{base_dir}/{f}", "rb") as rb:
            h = hashlib.sha256(rb.read()).hexdigest()
            file_hashes.append(f"{h}  {f}")
    
    with open(f"{base_dir}/manifest_sha256.txt", "w", newline='\n') as f:
        f.write("\n".join(file_hashes) + "\n")
    
    print(f"Generated synthetic proof pack: {base_dir}")
    return run_id

if __name__ == "__main__":
    generate_pack("8a2b3c4d")
