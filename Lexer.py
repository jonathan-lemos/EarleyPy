import sys
import re

regexes = [
    ("ID", r"[a-zA-Z]+"),
    ("INT", r"[0-9]+"),
    ("TYPE", r"int|void"),
    ("KEYWORD", r"if|else|while|return"),
    ("DELIM", r"[,()\[\]{};]"),
    ("ADDOP", r"[+\-]"),
    ("MULOP", r"[*/]"),
    ("=", "="),
    ("RELOP", r">=|<=|==|!=|>|<"),
]

comment = False
for line in open(sys.argv[1], "r"):
    if line.strip() == "":
        continue
    print("Input: '" + line[:-1] + "'")
    line = line.strip()
    while line != "":
        if not comment:
            if line.startswith("//"):
                break
            if line.startswith("/*"):
                line = line[2:]
                comment = True
                continue
            longest = ("ERROR", line[0])
            for token, pattern in regexes:
                mat = re.match(pattern, line)
                if mat:
                    longest = (token, line[:mat.end()])
            print(longest[0] + ": " + longest[1])
            line = line[len(longest[1]):]
            line = line.strip()
        else:
            mat = re.match(r".*?\*/", line)
            if not mat:
                line = ""
            else:
                line = line[mat.end():].strip()
                comment = False

