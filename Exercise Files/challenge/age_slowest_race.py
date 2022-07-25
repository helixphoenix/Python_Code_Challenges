# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
from time import strptime
from calendar import monthrange

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content


    
    
def get_event_time(lines):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
       
    jens_races = {}
    birthdate=""
    max=0
    max_time=0
    for line in lines:
        if line[14:29]== "Jennifer Rhines":
            if int(line[3:5]+line[6:8])>max:
               max=int(line[3:5]+line[6:8])  
               jens_races[line[0:12].replace("   ","").replace(" ","")]=line[56:68].replace(" ","")
               birthdate=line[74:85]
              
    for time in jens_races.keys():
        if int(time[0:2])+ int(time[3:5])/100>max_time:
            max_time=int(time[0:2])+ int(time[3:5])/100
    max_time_date= jens_races[str(max_time).replace(".",":")] 
    return max_time_date, birthdate,str(max_time)           
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
       
    lines= get_data()
    max_date, birthdate,max_time= get_event_time(lines)
    max_day=int(max_date[0:2])
    birth_day=int(birthdate[0:2])
    birth_month=strptime(birthdate[2:5],'%b').tm_mon
    max_month= int(strptime(max_date[2:5],'%b').tm_mon)
    max_year=int(max_date[-4:])
    birth_year=int(birthdate[-5:])
    age_year=max_year-birth_year    
    
    for i in range(1,max_month):
        max_day+=int(monthrange(max_year,i)[1])
    for i in range(1,birth_month):
        birth_day+=int(monthrange(birth_year,i)[1])   
        
    if max_day>birth_day:
        age_day=max_day-birth_day
    elif max_day<birth_day:
        age_day=365-(birth_day-max_day)
        age_year-=1
                   
    return (f"{age_year}y{age_day}d", max_time.replace(".",":"))        

get_age_slowest_times()