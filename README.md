# Code Complexity Analyzer

A lightweight static analysis tool that estimates structural complexity of C-like source code using heuristic metrics.

## Features
- Lines of code
- Loop count
- Conditional count
- Function detection
- Maximum nesting depth
- Weighted complexity score
- Improvement suggestions

## How it works
The tool preprocesses the source file, extracts structural patterns using regex and simple parsing,
then converts metrics into a calibrated difficulty rating.

This is not a compiler-level analyzer; it is a fast heuristic estimator.

## Usage

```bash
python analyze.py samples/sample.c

