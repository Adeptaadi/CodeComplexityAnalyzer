def calculate_score(metrics):
    loops = metrics["loops"]
    conditionals = metrics["conditionals"]
    functions = metrics["functions"]
    nesting = metrics["max_nesting"]
    loc = metrics["loc"]

    score = (
        loops * 2 +
        conditionals * 1.5 +
        functions * 1 +
        max(0, nesting - 2) * 2 +   # ignore shallow nesting
        loc * 0.03
    )

    if score < 10:
        level = "Easy"
    elif score < 20:
        level = "Moderate"
    elif score < 35:
        level = "Hard"
    else:
        level = "Very Hard"

    return round(score, 2), level
