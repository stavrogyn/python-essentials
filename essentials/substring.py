import re
import sys

for line in sys.stdin:
    flag_to_print_line = 0
    clear_string = line.rstrip()
    list_with_only_one_clear_word = re.findall(r"\w+\b", clear_string)
    print(list_with_only_one_clear_word)
    for word in list_with_only_one_clear_word:
        if len(word) % 2 == 0:
            end_index_of_first_part = int(len(word) / 2)
            first_part = word[:end_index_of_first_part]
            print(first_part)
            list_with_matches = re.findall(first_part, word)
            if len(list_with_matches) >= 2:
                flag_to_print_line += 1
    if flag_to_print_line > 0:
        print(line.strip())