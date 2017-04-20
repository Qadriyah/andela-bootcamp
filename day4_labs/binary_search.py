
class BinarySearch(list):

    def __init__(self, a, b):
        item = b
        for x in range(a):
            if item > a:
                break
            self.append(item)
            item += b
        self.length = len(self)

    def searchs(self, item):
        result = {}
        count = 0
        first_item_pos = 0
        last_item_pos = self.length - 1
        while first_item_pos < last_item_pos:
            mid_point = (first_item_pos + last_item_pos)//2
            if item > self[mid_point]:
                first_item_pos = mid_point + 1
            else:
                last_item_pos = mid_point
            count += 1
        if self[first_item_pos] != item:
            first_item_pos = -1
        result.update({count: first_item_pos})
        return result