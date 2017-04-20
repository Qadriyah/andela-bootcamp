
def find_missing(list1, list2):

    bigger_list = list2
    smaller_list = list1
    missing_number = 0
    if len(list1) == 0 or len(list2) == 0:
        return missing_number
    if len(list1) == len(list2):
        return missing_number
    if len(list1) > len(list2):
        bigger_list = list1
        smaller_list = list2
    for item in bigger_list:
        flag = 0
        for number in smaller_list:
            if item == number:
                flag = 1
                break
        if flag == 0:
            missing_number = item
            break
    return missing_number
