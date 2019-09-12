# Kristi Luu CIS41B -- Partner: Amir Alaj 
# A program that works with a list of countries of the world. 
# The program reads each country data from a file and lets the user search for countries based on their data.
from country import Country
import csv
from collections import defaultdict

def getData(fname="lab1in.csv"):
    '''Function that each line from the input file and create a Country object, storing that in a list'''
    try: 
        with open(fname) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            listOfCountries = [Country(*line) for line in readCSV]
            print("Read in", len(listOfCountries), "countries")
    except IOError: 
        print("The file is invalid. Please try again. Program will end.")
        raise SystemExit
    return listOfCountries

def printAll(objList):
    '''Print a counting number and the name of each Country object on one line.'''
    for i in range(len(objList)):
        print(i + 1, objList[i])

def getChoice():
    '''Prints menu and keep prompting the user until there is a valid choice and then return the choice.'''
    print("\nl. literacy rate\nd. population density\nq. quit\n")
    choice = input("Enter your choice: ").lower()
    while not choice in 'l d q'.split():
        print("Invalid choice")
        choice = input("Enter your choice: ").lower()
    return choice

def run(g, list):
    '''Runs the user choice'''
    tasks = {'l': litFunct, 'd': popDen}
    choice = getChoice()
    while choice != 'q':
        tasks[choice](g, list)
        choice = getChoice()

def retVal(popDen): #when copying from lab1 and replace the name popDen with f ; this is a general purpose function
    '''A decorator that adds paranetheses to the print'''
    def wrapper(*args, **kwargs):
        result = popDen(*args, **kwargs)
        (highest, lowest) = result
        print ("(" + str(highest) + ", " + str(lowest) + ")")
        return result
    return wrapper

@retVal
def popDen(g, objList):
    '''Calculates the population density of each part of the world'''
    continentSet = {items.getContinent() for items in objList}
    popDenDict = defaultdict(list)
    total = 0
    highest = 0.0
    lowest = 1.0
    for continent in continentSet:
        for items in objList:
            if items.getContinent() == continent:
                popDenDict[continent].append(items.getPopDensity())
                if items.getPopDensity() > highest:
                    highest = round(items.getPopDensity(),1)
                if items.getPopDensity() < lowest:
                    lowest = round(items.getPopDensity(),1)       

    for key in sorted(popDenDict):
        total = round(sum(popDenDict[key])/len(popDenDict[key]), 1)
        print(key + ":", total)
    return (highest, lowest)

def litFunct(g, objList):
    '''Loops to let the user press the Enter key to get a list of countries within a descending literacy rate'''
    count = 0
    user = input("Press Enter to see countries and literacy rates, anything else to quit: ")
    
    while user == "":
        try: 
            for i in next(g):
                if i <= 10: raise ValueError
                print(sorted(objList, reverse = True)[count], str(i) + "%")
                count += 1
            user = input("Press Enter to see countries and literacy rates, anything else to quit: ")
        except ValueError:
            user = "exit"
            print("You've reached the end of the data.")

def my_gen(objList):
    '''Yield one list of Country objects at a time, in descending range of literacy rate'''
    maxRange = 90
    rangeList = []
    for items in sorted(objList, reverse=True):
        if items.getLitRate() > maxRange:
            rangeList.append(items.getLitRate())
        else:
            yield rangeList
            maxRange -= 10
            del rangeList[:]
            rangeList.append(items.getLitRate())

def main():
    newList = getData()
    printAll(newList) 
    g = my_gen(newList)
    run(g, newList)

main()