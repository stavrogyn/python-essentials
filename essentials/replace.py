first_string = str(input())
second_string = str(input())
third_string = str(input())

count_of_including = 0
impossible_flag = False

while True:
    if second_string in first_string:
        count_of_including += 1
        first_string = first_string.replace(second_string, third_string)
        if count_of_including >= 1000:
            impossible_flag = True
            print('Impossible')
            break
    else:
        break

if impossible_flag == False:
    print(count_of_including)

