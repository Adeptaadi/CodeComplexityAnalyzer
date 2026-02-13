def generate_suggestions(metrics):
    """
    Provide improvement hints based on metric thresholds.
    Returns a list of strings.
    """

    advice = []

    if metrics["max_nesting"] >= 5:
        advice.append(
            "High nesting detected. Consider splitting logic into smaller functions."
        )

    if metrics["loops"] >= 5:
        advice.append(
            "Too many loops. Check if some logic can be simplified or reused."
        )

    if metrics["conditionals"] >= 7:
        advice.append(
            "Large number of conditionals. Maybe refactor using polymorphism, maps, or strategy patterns."
        )

    if metrics["functions"] == 0:
        advice.append(
            "No functions found. Modularizing code will improve readability and testing."
        )

    if metrics["loc"] > 300:
        advice.append(
            "File is quite large. Splitting into multiple modules may help maintainability."
        )

    return advice
