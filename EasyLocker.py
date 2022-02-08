import random
import sys
import json
import requests
import json
import numpy as np

# API used: https://api.datamuse.com/words?ml=

# Just some colors and shit
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
question = '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'
highest_speed = 10**12


def easy_to_rem_pass():
    name = input('%s Your Name: ' % question).lower()
    choice = input(
        '%s Do you want to Obsfucate (replace letters with special charcters) the name? [Y/n] ' % question).lower()
    if choice == 'n':
        obsfucate = False
    else:
        obsfucate = True

    generated_passwords = []

    with open("data.json", "r") as datafile:
        dicti = json.load(datafile)
        verb = dicti["verb"]
        adjective = dicti["adjective"]
        seperators = dicti["seperators"]
        numbers = dicti["numbers"]

    def generate(name, object):

        wordlist = []
        temp_words = []
        temp_words.append(random.choice(verb))
        temp_words.append(random.choice(adjective))
        temp_words.append(object)

        for i in range(3):
            str1 = temp_words[i]
            randindx = 0  # np.random.randint(0, len(str1))
            lst = list(str1)
            lst[randindx] = lst[randindx].upper()
            str2 = ""
            for char in lst:
                str2 = str2 + char
            wordlist.append(str2)

        seperator = str(random.choice(seperators)) + \
            str(random.choice(numbers))
        name = name.title()
        password = name + seperator + seperator.join(wordlist)
        pool_size = 94
        #entropy = (log(pool_size)/log(2)) * len(password)
        seconds_in_one_year = 3.15576e+7
        time_to_crack1 = ((pool_size**len(password)) /
                          (highest_speed))/seconds_in_one_year
        time_to_crack = str(time_to_crack1)
        for i in range(len(time_to_crack)):
            if time_to_crack[i] == '+':
                break
        for j in range(len(time_to_crack)):
            if time_to_crack[j] == '.':
                break

        power = time_to_crack[i+1:]
        base = time_to_crack[:j+3]

        crack_time = base + " × 10 to the power " + power
        pass_entry = [password, crack_time, time_to_crack1]
        generated_passwords.append(pass_entry)

    def initiate():
        object = input('%s Name a thing that you like: ' % question).lower()
        generated_passwords.clear()

        print('')
        print(' %s+------------------------------------------------------------------+---------------------------+%s' % (green, end))
        print(' %s|                            Password                              |   Time to Crack (Years)   |%s' % (green, end))
        print(' %s+------------------------------------------------------------------+---------------------------+%s' % (green, end))
        for y in range(0, 10):
            generate(name, object+"s")
        generated_passwords.sort(key=lambda x: x[2], reverse=True)
        for password in generated_passwords:
            print(' %s|%s %-65s%s|%s %-26s%s|%s' %
                  (green, end, password[0], green, end, password[1], green, end))
            print(' %s+----------------------------------------------------------------------------------------------+%s' % (green, end))
        choice = input(
            '\n%s Do you wish to generate more passwords? [y/N] ' % question).lower()
        if choice == 'y':
            initiate()
        else:
            quit()

    initiate()


print('''\n\n%sWELCOME TO EASY LOCKER ! %s\n''' % (green, end))
print('''%s\nMENU:%s\n''' % (yellow, end))
print('''%s1. Check the Strength of your Password %s\n''' % (yellow, end))
print('''%s2. Generate an Easy to Remember Password %s\n''' % (yellow, end))
print('''%s3. Quit%s\n\n''' % (yellow, end))
menu_choice = int(input('%s Enter your Choice: ' % question).lower())

if menu_choice == 1:
    password = input('%s Enter your Password: ' % question)
    broken = False
    with open('English.dic', 'r') as file:
        for line in file:
            if password in line.split():
                broken = True

    with open('0...9999999.dic', 'r') as file:
        for line in file:
            if password in line.split():
                broken = True

    if(broken):
        print(
            '''\n%s Your password would be cracked Instantly !!! %s\n''' % (red, end))
    else:
        pool_size = 0
        caps = 0
        smalls = 0
        nums = 0
        spec_chars = 0

        for char in password:
            if char.isupper():
                if caps == 0:
                    pool_size += 26
                    caps = 1
            elif char.islower():
                if smalls == 0:
                    pool_size += 26
                    smalls = 1
            elif char.isdigit():
                if nums == 0:
                    pool_size += 10
                    nums = 1
            else:
                pool_size += 32
                spec_chars = 1

        #entropy = (log(pool_size)/log(2)) * len(password)
        months_in_one_year = 12
        weeks_in_one_month = 4
        days_in_one_week = 7
        hours_in_one_day = 24
        minutes_in_one_hour = 60
        seconds_in_one_minute = 60
        time_to_crack = ((pool_size**len(password)) /
                         (highest_speed))

        time = time_to_crack
        time_unit = "seconds"

        if int(time/seconds_in_one_minute) != 0:
            time = time/seconds_in_one_minute
            time_unit = "minutes"

        if int(time/minutes_in_one_hour) != 0:
            time = time/minutes_in_one_hour
            time_unit = "hours"

        if int(time/hours_in_one_day) != 0:
            time = time/hours_in_one_day
            time_unit = "days"

        if int(time/days_in_one_week) != 0:
            time = time/days_in_one_week
            time_unit = "weeks"

        if int(time/weeks_in_one_month) != 0:
            time = time/weeks_in_one_month
            time_unit = "months"

        if int(time/months_in_one_year) != 0:
            time = time/months_in_one_year
            time_unit = "years"

        crack_time = "It would take a computer about " + \
            str(time) + " " + time_unit + " to crack your password"
        print(crack_time)

elif menu_choice == 2:
    easy_to_rem_pass()

elif menu_choice != 3:
    print('''\n%s WRONG CHOICE !!! %s\n''' % (red, end))
