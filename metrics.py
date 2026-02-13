import re

def count_loc(code):
    return len(code.splitlines())

def count_loops(code):
    patterns = [
        r"\bfor\s*\(",
        r"\bwhile\s*\(",
        r"\bdo\b"
    ]
    total=0
    for p in patterns:
        total+=len(re.findall(p,code))
    return total

def count_conditionals(code):
    """
    Count decision points.

    Includes:
    - if
    - else if
    - switch

    Avoids double counting else-if as both else-if and if.
    """

    # Count else-if first
    else_if_count = len(re.findall(r"\belse\s+if\s*\(", code))

    # Remove them so they are not counted again as plain if
    code_without_else_if = re.sub(r"\belse\s+if\s*\(", "", code)

    # Count remaining if
    if_count = len(re.findall(r"\bif\s*\(", code_without_else_if))

    # Count switch
    switch_count = len(re.findall(r"\bswitch\s*\(", code))

    total = else_if_count + if_count + switch_count
    return total


            
def count_functions(code):
    """
    Very rough heuristic.

    We look for:
    return_type name(args) {
    and try to exclude control statements.
    """

    matches = re.findall(r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^;]*\)\s*\{", code)

    blacklist = {"if", "for", "while", "switch", "catch"}

    return sum(1 for m in matches if m not in blacklist)

def calculate_max_nesting(code):
    depth = 0
    max_depth = 0

    for ch in code:
        if ch == "{":
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == "}":
            depth = max(0, depth - 1)

    return max_depth


def compute_metrics(code):
    return {
        "loc": count_loc(code),
        "loops": count_loops(code),
        "conditionals": count_conditionals(code),
        "functions": count_functions(code),
        "max_nesting": calculate_max_nesting(code)
    }