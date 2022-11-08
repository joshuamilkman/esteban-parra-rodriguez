# Name: Kanu Shetkar
# Professor: Professor Parra Rodriquez
# Assignment: Assignment 1
# Course: CSC-3400-01
# Date: 9/9/22

# Description:
# This project asks the user to input the expected total flight time in
# minutes and the actual total flight time in minutes.
# If a user inputs a number less than one prints an error message to the console.
# Calculates the acceptable deviation based on the expected time.
# Then prints if your flight time deviated too far or not.

print("----------------------------------------------------------------------")
print("Welcome to Moose and Squirrel AirlinesFlight Time Calculation Program")
print("----------------------------------------------------------------------")

print("Please enter the expected total flight time in minutes: ")
expectedTime = int(input())

print("Please enter the actual total flight time in minutes: ")
actualTime = int(input())

acceptableDeviationInMin = 0;
if expectedTime < 1 or actualTime < 1:
    print("flight time cannot be less than 1 minute")
else:
    if expectedTime >= 1 and expectedTime <= 32:
        acceptableDeviationInMin = 1
    elif expectedTime >=33 and expectedTime <= 45:
        acceptableDeviationInMin = 2
    elif expectedTime >=46 and expectedTime <= 63:
        acceptableDeviationInMin = 3
    elif expectedTime >= 64 and expectedTime <= 90:
        acceptableDeviationInMin = 4
    elif expectedTime >= 91 and expectedTime <= 115:
        acceptableDeviationInMin = 6
    elif expectedTime >= 116 and expectedTime <= 180:
        acceptableDeviationInMin = 8
    elif expectedTime >= 181 and expectedTime <= 242:
        acceptableDeviationInMin = 13
    elif expectedTime >= 243 and expectedTime <= 359:
        acceptableDeviationInMin = 17
    elif expectedTime >= 360:
        acceptableDeviationInMin = 20

    maxAcceptableTime = expectedTime + acceptableDeviationInMin
    minAcceptableTime = expectedTime - acceptableDeviationInMin

    if ((actualTime <= maxAcceptableTime) and (actualTime >= minAcceptableTime)):
         print("That flight time is ACCEPTABLE")
    else:
         print("This flight time is NOT ACCEPTABLE")

