
def get_price_change_per_day(data,start_date = "01/20/2021",end_date = "01/08/2021"):
    for day in data:
        high = data[day]["High"].strip("$")
        low = data[day]["Low"].strip("$")
        change = "{:.2f}".format(float(high) - float(low))
        change_str = str(f"${change}")
        change_rel = "{:.2f}".format(100 - float(low)/float(high) * 100)
        rel_str = str(f"{change_rel}%")
        data[day]["Change absolute"] = change_str
        data[day]["Change relative"] = rel_str
    return data
