from calendar import c
from collections import namedtuple
import re

with open('specifications.txt', 'rt') as file:
    specifications = file.readlines()

specs = namedtuple('specs',['rang','reg'])
#specs range builtin module
#specs regex from re.compile
# email a-zA-Z 0-9 @ a-zA-Z 0-9 . (com, org, net) 5-50
# email=specs((5:50),re.compile())
# url a-zA-Z 0-9 3-100

# feature: custom_url
#     requirements: between 3 and 100 characters
#     permitted characters: a-z A-Z 0-9

# feature: login
#     requirements: between 5 and 50 characters
#     login characters:  a-z A-Z 0-9 . _ -


def get_linkedin_dict():
    '''Convert specifications into a dict where:
       keys: feature
       values: specs namedtuple'''
    linkedin_dict={} 
    features=[]
    specis=[]  
    i=0
    for line in specifications:

        if 'feature:' in line:
           features.append(line.replace('\n','').split(': ')[1])
        elif 'requirements:' or 'characters:' in line:
            line=line.replace('\n','').replace("between ","").replace(" characters","").replace(" and ",',')
            if len(line.split(': '))==2:
                specis.append(line.split(': ')[1])      
    for feature in features:
        ranger=specis[i].split(',')
        pattern=f"[{specis[i+1]}]+"
        linkedin_dict[feature]= specs(range(int(ranger[0]),int(ranger[1])),re.compile(pattern))
        i+=2
    return linkedin_dict

def check_linkedin_feature(feature_text, url_or_login):
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
       
    requirements= get_linkedin_dict()
    if url_or_login=='custom_url':
        req=requirements['custom_url']
        if len(feature_text) not in req.rang:
             return False
        else:
            if req.reg.fullmatch(feature_text):
                return True
            else:
                return False    
            
    elif url_or_login=='login':
        req=requirements['login']        
        if len(feature_text) not in req.rang:
            
            return False
        else:
            if req.reg.match(feature_text) and '@' in feature_text and feature_text[-3:] in ['com', 'org', 'net']:
                return True
            else:
                return False    
            
    else :
        raise ValueError
        