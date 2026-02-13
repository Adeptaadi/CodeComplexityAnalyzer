import sys
from utils import read_file, preprocess
from metrics import compute_metrics
from scoring import calculate_score
from suggestions import generate_suggestions
from function_analysis import analyze_functions, find_worst_function


def print_report(filepath,metrics, score, level, advice,func_results=None, worst=None):
    print("\n==============================")
    print(" Code Complexity Report")
    print("==============================\n")
    print(f"File: {filepath}\n")
    print("Metrics:")
    print(f"  Lines of Code : {metrics['loc']}")
    print(f"  Functions     : {metrics['functions']}")
    print(f"  Loops         : {metrics['loops']}")
    print(f"  Conditionals  : {metrics['conditionals']}")
    print(f"  Max Nesting   : {metrics['max_nesting']}")
    print("\nScore:")
    print(f"  Complexity Score : {score}")
    print(f"  Difficulty Level : {level}")

    print("\nSuggestions:")
    if not advice:
        print(" No major issues detected.")
    else:
        for tip in advice:
            print(f" -{tip}")
            
    func_results = sorted(func_results, key=lambda x: x["score"], reverse=True)

    if func_results is not None:
        print("\nFunction Breakdown:")
        print("--------------------------------")

        if not func_results:
            print(" No functions detected.")
        else:
            for f in func_results:
                print(f"{f['name']:15} → {f['level']} ({f['score']})")

                if f["reasons"]:
                    print("   reasons:")
                    for r in f["reasons"]:
                        print(f"    - {r}")

    if worst:
        print(f"\nWorst function: {worst['name']} ({worst['score']})")


def main():
    if len(sys.argv)!=2:#for terminal correctness of 2 vectors one analyze.py and other the file that needs to be analyzed
        print("Usage: python analyze.py <source-file>")
        sys.exit(1)
    filepath=sys.argv[1]

    # Step1: read
    content=read_file(filepath)

    # Step2: clean
    clean_code=preprocess(content)

    # Step3: compute
    metrics=compute_metrics(clean_code)

    # Step4: score
    score,level=calculate_score(metrics)

    # Step5: suggestions
    advice=generate_suggestions(metrics)

    # Step6: function analysis
    func_results = analyze_functions(clean_code)
    worst = find_worst_function(func_results)

    # Step7: print
    print_report(filepath,metrics,score,level,advice,func_results,worst)

    

if __name__=="__main__":
    main()
