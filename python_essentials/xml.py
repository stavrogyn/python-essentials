from xml.etree import ElementTree as ET

root = ET.fromstring(input())
recursion_number = 0
color_counter = dict()
template_to_track_recursion = 'Number of recursion {number}: '

def children_getter(file_root, recursion_number):
    recursion_number += 1
    print('\nCurrent element is - ', file_root.tag, file_root.attrib, file_root)
    current_color = file_root.attrib['color']
    current_level_elements = file_root.findall("cube")
    color_apper(current_color, recursion_number)
    print('Childrens of current element: ', current_level_elements)
    if current_level_elements:
        recursion_number += 1
    for child in current_level_elements:
        print(template_to_track_recursion.format(number=recursion_number), child.tag, child.attrib, child)
        color_apper(child.attrib['color'], recursion_number)
        inner_elements = child.findall("cube")
        print(inner_elements)
        if inner_elements:
            for sub_element in inner_elements:
                children_getter(sub_element, recursion_number)

def color_apper(color, recursoion):
    if color not in color_counter:
        color_counter[color] = recursoion
    else:
        color_counter[color] += recursoion


children_getter(root, recursion_number)
print(color_counter['red'], color_counter['green'], color_counter['blue'])