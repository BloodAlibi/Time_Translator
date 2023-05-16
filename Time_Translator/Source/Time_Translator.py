# BloodAlibi // 2022

import time

print("Hello, welcome to Time Translator.")

def Initialize():
   print("\n\nPlease indicate below the amount of time you want to convert. To do so, use this format :\n- [Number]S for seconds\n- [Number]Min for minutes\n- [Number]H for hours\n- [Number]D for days\n- [Number]W for weeks\n- [Number]M for months")
   time = input("\n>>>\t")
   print("-"*20)
   return time

def Answer(_input):
    # Get digit out of the input
    digit = ""
    for character in _input:
        if character.isdigit() == True:
           digit += character
    if _input.find(".") != -1 or _input.find(",") != -1:
        print("Please only use integers as values, such as 2, 5, or 9000.")
        return
    try:
        digit = int(digit)
    except ValueError:
        print("The input entered is invalid. Please use the correct format. Example : 10S for 10 seconds.")
        return
    
    # Begin translation
    months = 0
    weeks = 0
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    tempdigit = digit
    if _input.find("S") != -1:
        months, tempdigit = divmod(tempdigit, 2592000)
        weeks, tempdigit = divmod(tempdigit, 604800)
        days, tempdigit = divmod(tempdigit, 86400)
        hours, tempdigit = divmod(tempdigit, 3600)
        minutes, tempdigit = divmod(tempdigit, 60)
        seconds = tempdigit
    elif _input.find("Min") != -1:
        months, tempdigit = divmod(tempdigit, 43800)
        weeks, tempdigit = divmod(tempdigit, 10080)
        days, tempdigit = divmod(tempdigit, 1440)
        hours, tempdigit = divmod(tempdigit, 60)
        minutes = tempdigit
    elif _input.find("H") != -1:
        months, tempdigit = divmod(tempdigit, 730)
        weeks, tempdigit = divmod(tempdigit, 168)
        days, tempdigit = divmod(tempdigit, 24)
        hours = tempdigit
    elif _input.find("D") != -1:
        months, tempdigit = divmod(tempdigit, 30)
        weeks, tempdigit = divmod(tempdigit, 7)
        days = tempdigit
    elif _input.find("W") != -1:
        months, tempdigit = divmod(tempdigit, 4)
        weeks = tempdigit
    elif _input.find("M") != -1:
        months = tempdigit
    else:
        print("Please don't forget to indicate the type of value you entered, like S for seconds.")
        return
    print("There is " + str(months) + " months, " + str(weeks) + " weeks, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds in " + str(_input))

# ----------------------
# Main program       
while True:
    time.sleep(1)
    Answer(Initialize())
