def explain_complexity(metrics):
    reasons = []

    if metrics["max_nesting"] >= 4:
        reasons.append(f"deep nesting ({metrics['max_nesting']})")

    if metrics["conditionals"] >= 3:
        reasons.append(f"many conditionals ({metrics['conditionals']})")

    if metrics["loops"] >= 2:
        reasons.append(f"multiple loops ({metrics['loops']})")

    if metrics["loc"] >= 20:
        reasons.append(f"long function ({metrics['loc']} LOC)")

    return reasons
