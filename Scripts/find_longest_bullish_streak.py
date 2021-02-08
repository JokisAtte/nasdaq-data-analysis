from Utils import dates_in_data

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

def find_longest_steak(data, start_date, end_date):
    data_slice = get_slice(data, start_date, end_date)
    longest = recursive(data_slice)
    return longest

def recursive(data, index=0, streak=0, longest=0):
    if index != len(data)-1:
        key_N = list(data.keys())[index]   # Date for day N
        key_Next = list(data.keys())[index + 1]   # Date for previous day (day N-1)
        close_N = float(data[key_N]["Close/Last"].strip("$"))
        close_N_minus1 = float(data[key_Next]["Close/Last"].strip("$"))
        index += 1
        if close_N > close_N_minus1:
            streak += 1
            if streak > longest:
                longest = streak
        else:
            streak = 0
        longest = recursive(data, index, streak, longest)
        return longest
    else:
        return longest

