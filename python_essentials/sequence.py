import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    list_with_matches = re.findall('cat', line)
    if len(list_with_matches) >= 2:
        print(line)