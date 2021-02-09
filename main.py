from Scripts import read_data, find_longest_bullish_streak, get_price_change_per_day

def main():
    data = read_data.read_data('HistoricalQuotes.csv')
    choises = {1: find_longest_bullish_streak.find_longest_steak}
    while True:
        print(" ")
        print("-----------------------------------------------------------")
        print("Available actions: ")
        print(" -Find longest bullish streak (1)")
        print(" -Highest volumes and price changes (2)")
        print("-----------------------------------------------------------")

        print("Select action by typing in its' number. Quit by typing q")
        user_input = input("Select your action:")
        print(" ")
        try:
            action = int(user_input)
            if action == 1:
                find_longest_bullish_streak.find_longest_steak(data)
            if action == 2:
                get_price_change_per_day.get_price_change_per_day(data)
            if action == "q":
                break
        except ValueError:
            if user_input == "q":
                print("Bye bye")
                break
            else:
                print("ERROR: Bad input. Select action by typing its number represented in parentheses")
                print(" ")

main()