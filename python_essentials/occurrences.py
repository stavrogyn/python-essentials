first_string = input()
second_string = input()

slice_mark = 0
space_of_included = set()

while True:
    if len(first_string[slice_mark:]) < len(second_string):
        break
    including_mark = first_string.find(second_string, slice_mark)
    slice_mark += 1
    if including_mark not in space_of_included and including_mark != -1:
        space_of_included.add(including_mark)
    if slice_mark >= len(first_string):
        break

print(len(space_of_included))

