from textwrap import fill
import sys
def small_offset(sequence, fillvalue, offset):
    tups=[]
    # expected = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')]

    for i in range(0,(len(sequence)+ (offset))):
        if i<offset:
            tups.append(tuple([sequence[i], fillvalue]))
        elif i>=len(sequence):
            tups.append(tuple([fillvalue, sequence[i-offset]]))
        else:
            tups.append(tuple([sequence[i], sequence[i-offset]]))
             
    return tups         
         
         
def big_offset(sequence, fillvalue, offset):
    tups=[]

    for i in range (0,len(sequence)): 
        tups.append(tuple([sequence[i], fillvalue]))
    for i in range (len(sequence), offset): 
        tups.append(tuple([fillvalue,fillvalue])  )  
    for i in range (offset, len(sequence)+offset): 
        tups.append(tuple([fillvalue,sequence[i-offset]]) ) 
    return tups      
        

       
       
        
    
def pairwise_offset(sequence, fillvalue='*', offset=0):
    if 0<=offset<len(sequence): 
       tups= small_offset(sequence, fillvalue, offset)                             
    elif offset>len(sequence): 
       tups=  big_offset(sequence, fillvalue, offset)
    return tups

