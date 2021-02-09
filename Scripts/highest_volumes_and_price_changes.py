from Utils import get_slice, ask_date_range

def get_highest_volumes_and_price_changes(data):
    start_date, end_date = ask_date_range.ask_date_range()
    data_slice = get_slice.get_slice(data, start_date, end_date)
    