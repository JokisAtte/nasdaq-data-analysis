from Scripts import read_data, find_longest_bullish_streak

def main():
    data = read_data.read_data('HistoricalQuotes.csv')
    print("Available actions: ")
    print("Find ")

    longest = find_longest_bullish_streak.find_longest_steak(data, "01/20/2021", "10/23/2020")
    print("longest bull streak: ", longest)


main()