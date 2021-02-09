def get_slice(data,start_date, end_date):
    slice = {}
    in_range = False
    for i in data:
        if i == start_date:
            in_range = True
        if in_range == True:
            slice[i] = data[i]
        if i == end_date:
            return slice