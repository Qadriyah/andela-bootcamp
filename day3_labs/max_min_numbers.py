def find_max_min(numbers):

    result = []
    if isinstance(numbers, list):
        if len(numbers) > 0:
            flag = 0
            for i in numbers:
                if type(i) is not int:
                    flag = 1
                    break
            if flag == 0:
                numbers.sort()
                last_item_pos = len(numbers) - 1
            if numbers[0] == numbers[last_item_pos]:
                result.append(len(numbers))
                return result
            result.append(numbers[0])
            result.append(numbers[last_item_pos])
            return result
