from textwrap import fill


def pairwise_offset(sequence, fillvalue, offset):
    tups=[]
    
    if offset==None or type(offset)==str:
            print("Please enter a valid offset value")
    elif 0<=offset<len(sequence): 
        
        for i in range(0,(len(sequence)+ (offset))):
            if i<offset:
                tups.append((sequence[i],fillvalue))
                print(tups)
            elif i>=len(sequence):
                print("here",i-offset)
                tups.append((fillvalue,sequence[i-offset]))
                print(sequence[i-offset])

            else:
                print(i)
                print("here I am ",sequence[i-offset])

                tups.append((sequence[i],sequence[i-offset]))       

                print(tups)
                    
    elif offset>len(sequence):
        for i in range (0,len(sequence)): 
            tups.append((sequence[i],fillvalue))
        for i in range (len(sequence),offset): 
            tups.append((fillvalue,fillvalue))    
        for i in range (offset,len(sequence)+offset): 
            tups.append((fillvalue,sequence[i-offset]))  
               
            



    return print(tups)    

pairwise_offset(['a','b','c'],"*",10)