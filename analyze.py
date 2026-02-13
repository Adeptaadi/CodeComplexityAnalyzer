import sys
from utils import read_file, preprocess
from metrics import compute_metrics
from scoring import calculate_score
from suggestions import generate_suggestions

def print_report(filepath,metrics, score, level, advice):
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
            
    print("\n==============================\n")

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

    # Step6: print
    print_report(filepath,metrics,score,level,advice)

if __name__=="__main__":
    main()
