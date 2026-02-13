import re

def read_file(filepath):
    try:
        with open(filepath, "r",encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found->{filepath}")
        exit(1)

# def remove_single_line_comment(code):
#     # removes // comments
#     # re.sub(pattern, replacement, input_string) --> Find text that matches a pattern → replace it with something else.
#     return re.sub(r"//."," ",code)
#     # r"//.*" → the pattern --> // followed by anything, as much as possible, until the line ends


# def remove_single_line_comments(code):
#     result = []
#     i = 0
#     in_string = False

#     while i < len(code):
#         ch = code[i]

#         # entering or leaving a string (ignore escaped quotes)
#         if ch == '"' and (i == 0 or code[i-1] != '\\'):
#             in_string = not in_string
#             result.append(ch)
#             i += 1
#             continue

#         # start of comment (only if not inside string)
#         if not in_string and code[i:i+2] == "//":
#             # skip everything till newline
#             while i < len(code) and code[i] != "\n":
#                 i += 1
#             continue

#         result.append(ch)
#         i += 1

#     return "".join(result)

# def remove_multi_line_comments(code):
#     # removes /* ... */ blocks
#     return re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)



def remove_comments(code: str) -> str:
    """
    Remove C/C++ style comments from source code.

    Handles:
    - single line comments  -> //
    - block comments        -> /* ... */
    - ignores comment markers inside string and char literals
    """

    result = []                 # final characters collected
    i = 0                       # current index in input
    n = len(code)

    in_string = False           # inside "..."
    in_char = False             # inside '...'
    in_line_comment = False     # after //
    in_block_comment = False    # after /*

    while i < n:
        ch = code[i]
        nxt = code[i + 1] if i + 1 < n else ""

        # ==============================
        # 1. If currently inside a line comment
        # ==============================
        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
                result.append(ch)   # keep newline
            i += 1
            continue

        # ==============================
        # 2. If inside a block comment
        # ==============================
        if in_block_comment:
            if ch == "*" and nxt == "/":
                in_block_comment = False
                i += 2              # skip */
            else:
                i += 1              # skip comment content
            continue

        # ==============================
        # 3. If inside a string literal
        # ==============================
        if in_string:
            result.append(ch)

            # exit string if quote not escaped
            if ch == '"' and code[i - 1] != "\\":
                in_string = False

            i += 1
            continue

        # ==============================
        # 4. If inside a character literal
        # ==============================
        if in_char:
            result.append(ch)

            # exit char if quote not escaped
            if ch == "'" and code[i - 1] != "\\":
                in_char = False

            i += 1
            continue

        # ==============================
        # 5. We are in NORMAL CODE
        # ==============================

        # start of line comment?
        if ch == "/" and nxt == "/":
            in_line_comment = True
            i += 2
            continue

        # start of block comment?
        if ch == "/" and nxt == "*":
            in_block_comment = True
            i += 2
            continue

        # start of string?
        if ch == '"':
            in_string = True
            result.append(ch)
            i += 1
            continue

        # start of char literal?
        if ch == "'":
            in_char = True
            result.append(ch)
            i += 1
            continue

        # otherwise normal character
        result.append(ch)
        i += 1

    return "".join(result)


def remove_blank_lines(code):
    lines = code.splitlines()
    cleaned = [line for line in lines if line.strip() != ""]
    return "\n".join(cleaned)


def preprocess(code):
    # code = remove_single_line_comments(code)
    code = remove_comments(code)
    code = remove_blank_lines(code)
    return code