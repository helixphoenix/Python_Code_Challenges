from textwrap import fill
import sys
def small_offset(sequence, fillvalue, offset):
    tups=[]

    for i in range(0,(len(sequence)+ (offset))):
        if i<offset:
          tups.append((sequence[i],fillvalue))
        elif i>=len(sequence):
            tups.append((fillvalue,sequence[i-offset]))
        else:
             tups.append((sequence[i],sequence[i-offset]))  
             
    return tups         
         
         
def big_offset(sequence, fillvalue, offset):
    tups=[]

    for i in range (0,len(sequence)): 
        tups.append((sequence[i], fillvalue))
    for i in range (len(sequence), offset): 
        tups.append((fillvalue, fillvalue))    
    for i in range (offset, len(sequence)+offset): 
        tups.append((fillvalue, sequence[i-offset]))  
    return tups         
        

       
       
        
    
def pairwise_offset(sequence, fillvalue="*", offset=0):
    if 0<=offset<len(sequence): 
       tups= small_offset(sequence, fillvalue, offset)                             
    elif offset>len(sequence): 
       tups=  big_offset(sequence, fillvalue, offset)
    return print(tups)   

pairwise_offset(['a','b','c'],"*",5)