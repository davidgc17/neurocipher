import csv
import os
from datetime import datetime

def log_recovery_result(
    original_bytes: bytes,
    recovered_bytes: bytes,
    noise_level: float,
    version: str,
    annealing_start: float,
    annealing_steps: int,
    bit_diff: int,
    pattern_id: str,
    repetitions: int,
    chunk_size: int
):
    filename = f"recovery_results_{version}.csv"
    filepath = os.path.join("logs", filename)
    os.makedirs("logs", exist_ok=True)

    total_bits = len(original_bytes) * 8
    precision = 100 * (total_bits - bit_diff) / total_bits
    exact = original_bytes == recovered_bytes

    fieldnames = [
        "timestamp", "pattern_id", "version", "annealing_start", "annealing_steps",
        "noise_level", "bit_diff", "precision", "exact_match",
        "repetitions", "chunk_size"
    ]

    with open(filepath, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.stat(filepath).st_size == 0:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.now().isoformat(),
            "pattern_id": pattern_id,
            "version": version,
            "annealing_start": annealing_start,
            "annealing_steps": annealing_steps,
            "noise_level": noise_level,
            "bit_diff": bit_diff,
            "precision": f"{precision:.2f}",
            "exact_match": exact,
            "repetitions": repetitions,
            "chunk_size": chunk_size
        })
