from collections import namedtuple
from re import A

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.readlines()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples
for line in olympics:
        med=line.replace('\n', '').split(';')
        med=medal(City=med[0],Edition=med[1],Sport=med[2], Discipline=med[3],Athlete=med[4], NOC=med[5],Gender=med[6],Event=med[7],Event_gender=med[8],Medal=med[9])
        medals.append(med)
# print(medals)    
def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    filt_medals=[]
    print(kwargs)
    for medal in medals:
        filt=0
        for var in kwargs.values():
            if var in medal: 
                print(medal)
                filt+=1
        if len(kwargs.values())==filt:
            filt_medals.append(medal)
            
    return filt_medals        
                    
                
                

    

# get_medals(Edition='1924', Sport='Athletics', Discipline='Athletics',)