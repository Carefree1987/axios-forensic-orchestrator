import os
import sys
import hashlib

def verify_pack(pack_path):
    print(f"--- AXIOS Forensic Verifier 🦅 ---")
    print(f"Target: {pack_path}")
    
    if not os.path.exists(pack_path):
        print(f"ERROR: Pack not found at {pack_path}")
        return False
    
    manifest_file = os.path.join(pack_path, "manifest_sha256.txt")
    if not os.path.exists(manifest_file):
        print("ERROR: manifest_sha256.txt missing.")
        return False
    
    print("Step 1: Checking file integrity...")
    with open(manifest_file, "r") as f:
        for line in f:
            expected_hash, filename = line.strip().split("  ")
            actual_file = os.path.join(pack_path, filename)
            
            if not os.path.exists(actual_file):
                print(f"FAIL: {filename} missing.")
                return False
            
            with open(actual_file, "rb") as rb:
                actual_hash = hashlib.sha256(rb.read()).hexdigest()
                if actual_hash != expected_hash:
                    print(f"FAIL: {filename} hash mismatch!")
                    return False
                print(f"OK: {filename}")
    
    print("\nStep 2: Checking Proof-6 Gates...")
    proof_file = os.path.join(pack_path, "verify_proof_6.txt")
    with open(proof_file, "r") as f:
        lines = f.readlines()
        if len(lines) != 6:
            print(f"FAIL: Proof file must have exactly 6 lines. Found {len(lines)}.")
            return False
        for line in lines:
            if "PASS" not in line:
                print(f"FAIL: Gate failure detected: {line.strip()}")
                return False
            print(f"VERIFIED: {line.strip()}")
            
    print("\n--- GLOBAL STATUS: PASS ---")
    print("Forensic integrity confirmed.")
    return True

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "examples/proof_pack_synthetic/run_8a2b3c4d"
    sys.exit(0 if verify_pack(path) else 1)
