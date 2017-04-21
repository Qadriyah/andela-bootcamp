
def data_type(input_data):
    try:
        if type(input_data) is str:
            return len(input_data)
        if type(input_data) is bool:
            return input_data
        if type(input_data) is int:
            if input_data < 100:
                return 'less than 100'
            elif input_data > 100:
                return 'more than 100'
            else:
                return 'equal to 100'
        if type(input_data) is list:
            if len(input_data) >= 3:
                return input_data[2]
            else:
                return None
        return 'no value'
    except TypeError:
        raise 'type error'