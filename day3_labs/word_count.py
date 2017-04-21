import re


def words(data):
    result = {}
    data = re.sub('\s+', ' ', data)
    data = data.split()
    if len(data) == 1:
        result.update({data[0]: 1})
        return result
    for item in data:
        item = item.strip()
        if len(item) != 0:
            counter = 0
            for i in range(len(data)):
                if item == data[i]:
                    counter += 1
            try:
                item = int(item)
            except ValueError:
                pass
            result.update({item: counter})

    return result