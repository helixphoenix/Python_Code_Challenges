# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    jens_races = []
    for line in races:
        if line[14:29]== "Jennifer Rhines":
            jens_races.append(line[0:12])
    return jens_races

def get_average():
    racetimes = get_rhines_times()
    races= len(racetimes)
    total = datetime.timedelta() 
    
    for race in racetimes:
        if race[8]==".":
         total += datetime.timedelta(minutes=int(race[3:5]), seconds=int(race[6:8]), milliseconds=int(race[9:12]))
        else:                             
         total += datetime.timedelta(minutes=int(race[3:5]), seconds=int(race[6:8]))
 
    avg_time= f"{total/races}"[2:-5]

     
    return  print(avg_time) 
        
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where the solutions format was not matching the requested format, i have followed the way he does as mm:ss.M :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    pass

get_average()