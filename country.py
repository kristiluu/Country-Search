#Kristi Luu; Partner: Amir Alaj -- Country.py reads in each line of csv file and updates the continents
import csv
import string

class Country:
    '''Contains the Country class, which holds information for one country'''
    def __init__(self, *args):
        '''Constructor that accepts one line of the input file, parses (separates) 
        the line into 4 data values and stores them in 4 instance variables.'''
        continent = args[1].rstrip().title()
        try:
            self._litrate = float(args[3].rstrip())
        except ValueError:
            self._litrate = -1.0
        self._country = args[0].rstrip().replace(",",";")
        self.updateCont(continent)
        self._popdensity = float(args[2])

    def __str__(self):
        '''Converts an object to a string, allows for print(countryObj) to work'''
        return self._country

    def updateCont(self, continent):
        '''Replaces all segments of a continent to one general continent'''
        if 'Africa' in continent:
            self._continent = 'Africa'
        elif 'Europe' in continent:
            self._continent = 'Europe'
        elif 'Latin' in continent:
            self._continent = 'South America'
        elif 'America' in continent:
            self._continent = 'North America'
        else:
            self._continent = continent

    def getPopDensity(self):
        '''Getter for population density'''
        return self._popdensity
    
    def getContinent(self):
        '''Getter for continent'''
        return self._continent

    def getLitRate(self):
        '''Getter for literacy rate'''
        return self._litrate

    def __lt__(self, rhs):
        '''Overloads less-than sign to compare literacy rates'''
        return self._litrate < rhs._litrate