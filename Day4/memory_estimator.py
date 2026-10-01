BYTES_PER_PARAM = {
    "FP16": 2.00,
    "Q8_0": 1.00,
    "Q6_K": 0.81,
    "Q5_K_M": 0.68,
    "Q4_K_M": 0.57,
    "Q3_K_M": 0.43,
}

KV_GB_PER_B_PER_1K = 0.02
OVERHEAD = 1.10


def estimate(params_b, precision, context_k):
    weights_gb = params_b * BYTES_PER_PARAM[precision]
    kv_gb = params_b * context_k * KV_GB_PER_B_PER_1K
    total_gb = (weights_gb + kv_gb) * OVERHEAD

    return weights_gb, kv_gb, total_gb


def verdict(total_gb, available_gb):
    if total_gb <= available_gb * 0.7:
        return "Fits comfortably"
    elif total_gb <= available_gb:
        return "Fits, but tight"
    else:
        return "Does NOT fit"


def report(name, params_b, precision, context_k, available_gb):
    weights, kv, total = estimate(
        params_b, precision, context_k
    )

    print(
        f"{name:<18} "
        f"{params_b:>5.1f}B "
        f"{precision:<7} "
        f"ctx {context_k:>3}K "
        f"weights {weights:>6.2f} GB "
        f"KV {kv:>5.2f} GB "
        f"total {total:>6.2f} GB "
        f"-> {verdict(total, available_gb)}"
    )


if __name__ == "__main__":

    AVAILABLE_GB = 8.0

    print(f"Available memory: {AVAILABLE_GB} GB\n")

    # Four model configurations for the scenario
    report("1.5B Q4", 1.5, "Q4_K_M", 8, AVAILABLE_GB)
    report("8B Q4", 8.0, "Q4_K_M", 8, AVAILABLE_GB)
    report("8B FP16", 8.0, "FP16", 8, AVAILABLE_GB)
    report("30B Q4", 30.0, "Q4_K_M", 8, AVAILABLE_GB)

    print("\nContext length experiment:")

    for context in (4, 8, 32, 128):
        report(
            "8B Q4",
            8.0,
            "Q4_K_M",
            context,
            AVAILABLE_GB
        )

    print("\nQuantization experiment:")

    for precision in (
        "Q3_K_M",
        "Q4_K_M",
        "Q5_K_M",
        "Q8_0",
        "FP16"
    ):
        report(
            "8B model",
            8.0,
            precision,
            8,
            AVAILABLE_GB
        )