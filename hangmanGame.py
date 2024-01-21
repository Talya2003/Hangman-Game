#ACCOUNT_NUMBER
#amount_of_money

# "Shuffle, Shuffle, Shuffle", say it together! Change colors and directions, Don't back down and stop the player! Do you want to play Taki? Press y\n

# str1 = "\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,"
# str2 = "\nDon't back down and stop the player!\n\tDo you want to play Taki? \n\tPress y\\n"
# print(str1+str2)

# encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
# print(str(encrypted_message[-1::-2]))


# str = input("Please enter a string: ")
# new_str = str[1::]
# new_text = new_str.replace(str[0], "e")
#
# print(str[0] + new_text)

# str = input("Please enter a string: ")
# size = len(str)
# str_left = str[:(size//2)]
# str_right = str[(size//2):]
# print(str_left.lower() + str_right.upper())

# #polindrom
#
# str = input("Enter a word: ")
# str_new = str.lower()
#
# str_new = str_new.replace(' ' , '')
#
# if (str_new[:] == str_new[-1::-1]) :
#     print("OK")
# else:
#     print("NOT")


# # degrees
#
# str = input("Insert the temperature you would like to convert: ")
# num_of_deg = float(str[:-1:1])
# calc_deg = 0
#
# if str[-1] == 'F' or str[-1] == 'f':
#     calc_deg = (5*num_of_deg - 160) / 9
#     print("The new degree is:", calc_deg, "C")
#
# elif str[-1] == 'C' or str[-1] == 'c':
#         calc_deg = (9 * num_of_deg + 160) / 5
#         print("The new degree is:", calc_deg, " F")


from datetime import datetime

date_input = input("Enter a date (YYYY-MM-DD): ")

date_obj = datetime.strptime(date_input, '%Y-%m-%d')

day_of_week = date_obj.weekday()

if (day_of_week == 6):
    day_of_week = 'Sunday'
elif (day_of_week == 0):
    day_of_week = 'Monday'
elif (day_of_week == 1):
    day_of_week = 'Tuesday'
elif (day_of_week == 2):
    day_of_week = 'Wednesday'
elif (day_of_week == 3):
    day_of_week = 'Thursday'
elif (day_of_week == 4):
    day_of_week = 'Friday'
elif (day_of_week == 5):
    day_of_week = 'Saturday'

print(f"The day of the week for {date_input} is {day_of_week}.")
