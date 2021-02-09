from Utils import dates_in_data, get_slice, ask_date_range

def find_longest_steak(data):
    start_date, end_date = ask_date_range.ask_date_range()
    if dates_in_data.dates_in_data(data, start_date, end_date):
        data_slice = get_slice.get_slice(data, start_date, end_date)
        longest = count_longest_streak(data_slice)
        print(" ")
        print("Result:")
        print(f"In Apple stock historical data the Close/Last price increased {longest}"
              f" days in a row between {end_date} and {start_date}.")
        return longest
    else:
        print("Dates not found")

def count_longest_streak(data, index=0, streak=0, longest=0):
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
        longest = count_longest_streak(data, index, streak, longest)
        return longest
    else:
        return longest
