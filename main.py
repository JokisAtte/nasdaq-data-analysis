from Scripts import read_data, find_longest_bullish_streak

def main():
    data = read_data.read_data('HistoricalQuotes.csv')
    choises = {1: find_longest_bullish_streak.find_longest_steak}
    while True:
        print(" ")
        print("-----------------------------------------------------------")
        print("Available actions: ")
        print(" -Find longest bullish streak (1)")
        print("-----------------------------------------------------------")

        print("Select action by typing in its' number. Quit by typing q")
        user_input = input("Select your action:")
        print(" ")
        try:
            action = int(user_input)
            if action == 1:
                find_longest_bullish_streak.find_longest_steak(data)
            if action == "q":
                break
        except ValueError:
            if user_input == "q":
                print("Bye bye")
                break
            else:
                print("ERROR: Bad input. Select action by typing its number represented in parentheses")
                print(" ")




    #longest = find_longest_bullish_streak.find_longest_steak(data, "01/20/2021", "10/23/2020")


main()