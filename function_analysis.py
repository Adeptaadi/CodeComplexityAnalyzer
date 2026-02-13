import re
from  metrics import compute_metrics
from scoring import calculate_score
from explain import explain_complexity


FUNCTION_PATTERN = re.compile(
    r"\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^;]*\)\s*\{"
)

BLACKLIST={"if","for","while","switch","catch"}

def extract_function(code):
    """
    Returns list of tuples:
    (function_name, function_code)
    """
    functions=[]

    for match in FUNCTION_PATTERN.finditer(code):
        name=match.group(1)

        if name in BLACKLIST:
            continue
        start=match.end()-1

        depth =1
        i=start+1

        while i<len(code) and depth>0:
            if code[i]=="{":
                depth+=1
            elif code[i]=="}":
                depth-=1
            i+=1

        body=code[match.start():i]
        functions.append((name, body))  

    return functions

def analyze_functions(code):
    """
    For each function:
    compute metrics + score
    """

    results=[]

    for name,body in extract_function(code):
        metrics=compute_metrics(body)
        score, level=calculate_score(metrics)

        results.append({
            "name":name,
            "metrics":metrics,
            "score":score,
            "level":level,
            "reasons": explain_complexity(metrics)
        })
    return results
def find_worst_function(results):
    if not results:
        return None
    return max(results, key=lambda x:x["score"])

    