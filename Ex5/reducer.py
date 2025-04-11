import sys

phrase_dict = {}

# Read input from mapper
for line in sys.stdin:
    phrase, cnt = line.split('\t', 1)
    try:
        cnt = int(cnt)
    except ValueError:
        continue

    if phrase in phrase_dict:
        phrase_dict[phrase] += cnt
    else:
        phrase_dict[phrase] = cnt


max_key = max(phrase_dict, key=phrase_dict.get)
max_value = phrase_dict[max_key]

print(f"{max_key}\t{max_value}")
