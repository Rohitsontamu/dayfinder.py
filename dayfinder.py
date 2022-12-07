from time import sleep

print("~ Welcome to the Dayfinder guys! ~")
print(" ")
print("Let's find the Weekday to any Date!!")
print("____________________________ ")
print("---------------------------- ")
print("Please Enter the following in numerals:")
print(" ")
day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))
print(" ")


def switch(h):
    return {
        0: "Saturday!",
        1: "woohoo it's SUNDAY!",
        2: "Monday!",
        3: "Tuesday!",
        4: "Wednesday!",
        5: "Thursday!",
        6: "Friday!",
    }[h]


def Weekday(day, month, year):
    if (month == 1):
        month = 13
        year = year - 1

    if (month == 2):
        month = 14
        year = year - 1
    q = day
    m = month
    k = year % 100;
    j = year // 100;
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    print("The Weekday of the given Date is:")
    print(switch(h))


Weekday(day, month, year)
sleep(1.34)
print("________________________________________ ")
print(" ")
print("WANNA FIND ANOTHER DAY LET'S GO!!")
sleep(5)
print("Relaunch the program to find the day to another date...")
sleep(13)