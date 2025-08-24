#Finding Max without using max function
def find_max_min(list1):
    max = list1[0]
    min = list1[0]
    for i in range(1,len(list1)):
        if (list1[i]) > max:
            max = list1[i]
        if (list1[i] < min):
            min = list1[i]
    return max

numbers = [-1001,-200,-999]
max= find_max_min(numbers)
print("Maximum: ", max)

