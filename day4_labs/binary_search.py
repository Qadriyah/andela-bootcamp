
class BinarySearch(list):

    def __init__(self, a, b):
        item_list = [x for x in range(b, (a * b) + 1, b)]
        for item in item_list:
            self.append(item)
        self.length = a

    def search(self, number):
        result = {}
        count = 0
        first_item_pos = 0
        last_item_pos = self.length - 1
        while first_item_pos <= last_item_pos:
            mid_point = (first_item_pos + last_item_pos)//2
            if number == self[mid_point]:
                break
            else:
                if number > self[mid_point]:
                    first_item_pos = mid_point + 1
                else:
                    last_item_pos = mid_point - 1
            count += 1
        if self[mid_point] != number:
            mid_point = -1
        result.update({'count': count})
        result.update({'index': mid_point})
        return result
