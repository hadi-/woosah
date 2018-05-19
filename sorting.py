def simple_sort(num):
    # set the correct answer by sorted function
    answer = sorted(num)
    
    # check if the input already sorted
    if num == answer:
        return 'yes'
    
    # set default index    
    start = -1
    end = -1

    # if index value not same with answer index value set the first found index
    for i in range(len(num)):
        if num[i] != answer[i]:
            start = i
            break
    # if index value not same with answer index value set the first found index in backwards mode
    for i in range(len(num) - 1, -1, -1):
        if num[i] != answer[i]:
            end = i
            break
    # swap the diff index 
    num[start], num[end] = num[end], num[start]
    # if after swap array matches the answer then set swap is true
    if num == answer:
        return 'Yes\nswap ' + str(start + 1) + str(end + 1)
    # reverse the array
    num[start+1:end] = num[start + 1:end][::-1]
    # if after reverse array matches the answer then set swap is true
    if num == answer:
        return 'Yes\nreverse ' + str(start + 1) + str(end + 1)
    return 'No'



numbs = input("your number: ")
a = list(map(int, numbs.split()))
print(simple_sort(a))