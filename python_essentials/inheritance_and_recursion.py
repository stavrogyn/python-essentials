from pprint import pprint
import json

class_repeated_counter = dict()
classes_relations_space = dict()

date_in_string_form = "".join(open("../data/test_input_3.5.4", "r").readlines())
test_input = json.loads(date_in_string_form)
pprint(test_input)


def from_json_to_string(list_with_objects):
    for class_instance in list_with_objects:
        class_name = class_instance['name']
        class_repeated_counter[class_name] = 1
    print(class_repeated_counter, '\n')

def relations_maker(list_with_objects):
    for class_instance in list_with_objects:
        class_name = class_instance['name']
        class_parents = class_instance['parents']
        for parent in class_parents:
            if parent not in classes_relations_space:
                classes_relations_space[parent] = {'parents': [], 'children': [class_name]}
            else:
                classes_relations_space[parent]['children'].append(class_name)
            if class_name not in classes_relations_space:
                classes_relations_space[class_name] = {'parents': [parent], 'children': []}
            else:
                classes_relations_space[class_name]['parents'].append(parent)
    pprint(classes_relations_space)

from_json_to_string(test_input)
relations_maker(test_input)

def all_parents_plus_one_relation(parent, virtual_space_of_added_classes):
    print(parent, virtual_space_of_added_classes)
    class_parents = classes_relations_space[parent]['parents']
    if parent not in virtual_space_of_added_classes:
        virtual_space_of_added_classes.append(parent)
        class_repeated_counter[parent] += 1
        print('В последовательности уже добавлены', virtual_space_of_added_classes)
        if class_parents:
            for another_parent in class_parents:
                print("Рекурсия начата от", parent, "к", another_parent)
                all_parents_plus_one_relation(another_parent, virtual_space_of_added_classes)
    return virtual_space_of_added_classes


def children_counter(class_element):
    virtual_space_of_added_classes = list()
    print(class_element, classes_relations_space[class_element]['children'], classes_relations_space[class_element]['parents'])
    class_parents = classes_relations_space[class_element]['parents']
    if class_parents:
        for parent in class_parents:
            all_parents_plus_one_relation(parent, virtual_space_of_added_classes)

def recycling_objects(space_with_objects):
    for class_element in space_with_objects:
        children_counter(class_element)


recycling_objects(classes_relations_space)
for k, v in sorted(class_repeated_counter.items(), key=lambda item: item[0]):
    print(k, ':', v)