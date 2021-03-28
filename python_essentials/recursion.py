from pprint import pprint
import copy

exceptions = open('../data/test_input_2.1.7')
sequences = open('../data/test_input_2.1.7_2')
final_indexes_set = set()
final_values_list = list()
sequence_of_exceptions = list()
relations_virtual_space = dict()


def relations_creator(list_for_formatting):
    class_to_create = list_for_formatting[0]
    if class_to_create not in relations_virtual_space:
        relations_virtual_space[class_to_create] = {'parents': [], 'childrens': []}
    while len(list_for_formatting) != 1:
        parent_from_all_parents = list_for_formatting.pop()
        if parent_from_all_parents not in relations_virtual_space:
            relations_virtual_space[parent_from_all_parents] = {'parents': [], 'childrens': []}
        relations_virtual_space[class_to_create]['parents'].append(parent_from_all_parents)
        relations_virtual_space[parent_from_all_parents]['childrens'].append(class_to_create)
    pprint(relations_virtual_space)


for line in exceptions:
    list_with_values_from_string = line.split()
    if ':' in list_with_values_from_string:
        list_with_values_from_string.remove(':')
    relations_creator(list_with_values_from_string)


def compare_for_delete(potential_parent, index_of_potential_child,
                       list_for_compare):
    potential_child = list_for_compare[index_of_potential_child]
    potential_parents = copy.copy(relations_virtual_space[potential_parent]['childrens'])
    if potential_parent == potential_child:
        final_indexes_set.add(index_of_potential_child)
    else:
        if potential_parents:
            for another_child_of_potential_parent in potential_parents:
                compare_for_delete(another_child_of_potential_parent, index_of_potential_child, list_for_compare)


def exceptions_to_delete(list_of_exceptions):
    for parent_index in range(len(list_of_exceptions)):
        for child_index in range(len(list_of_exceptions)):
            if parent_index >= child_index:
                continue
            else:
                value_potential_parent = list_of_exceptions[parent_index]
                compare_for_delete(value_potential_parent, child_index, list_of_exceptions)


for sequence in sequences:
    sequence_of_exceptions.append(sequence.strip())

print(sequence_of_exceptions)
exceptions_to_delete(sequence_of_exceptions)
final_indexes_set = list(final_indexes_set)
final_indexes_set.sort()
print(final_indexes_set)


for value_from_original_list in final_indexes_set:
    current_exception_value = sequence_of_exceptions[value_from_original_list]
    if current_exception_value not in final_values_list:
        final_values_list.append(current_exception_value)


print(final_values_list)


for answer_value in final_values_list:
    print(answer_value)
