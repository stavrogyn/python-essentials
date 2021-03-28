with open('../data/test_input_2.3.7.txt', 'r') as dataset, open('../data/test_input_2.3.7_2.txt', 'w') as reverse_dataset:
    transfer_list = list()
    for line in dataset:
        line = line.strip()
        transfer_list.append(line)
    transfer_list.reverse()
    transfer_list = '\n'.join(transfer_list)
    reverse_dataset.write(transfer_list)
