def ask_date_range():
    start_date = input("Enter start date (mm/dd/yyyy)")
    end_date = input("Enter end date (mm/dd/yyyy)")
    if start_date == "aa":  # for testing
        start_date = "01/20/2021"
        end_date = "12/16/2020"
    return start_date, end_date