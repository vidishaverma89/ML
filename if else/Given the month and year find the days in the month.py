month = int(input("month:"))


if month == 2:
    year = int(input("year:"))
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("number of days is 29")
    else:
        print("number of days is 28")
elif (
    month == 1
    or month == 3
    or month == 5
    or month == 7
    or month == 8
    or month == 10
    or month == 12
):
    print("number of days is 31")
else:
    print("number of days is 30")
