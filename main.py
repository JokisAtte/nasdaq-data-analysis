import csv


def dict_filter(it, *keys):
    for d in it:
        yield dict((k, d[k]) for k in keys)


def read_data(filename):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        lines = 0
        data = {}
        raw_data = []
        print(f"Processing file {filename}...")
        for row in reader:
            raw_data.append(row)
            filtered = dict_filter(row, "Close/Last", "Volume", "Open", "High", "Low")
            data[row["Date"]] = filtered
            lines += 1
        print(f"processed {lines} rows of data")
        print(f"column names are: {list(raw_data[0].keys())} ")
        i = 0
        for d in dict_filter(raw_data, "Close/Last", "Volume", "Open", "High", "Low"):
            date = raw_data[i]["Date"]
            data[date] = d
            i += 1


def main():
    read_data('HistoricalQuotes.csv')



main()