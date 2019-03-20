s= [16, 19, 11, 15, 10, 12, 14]


for j in range(len(s)):
    
    swapped = False
    i = 0
    while i<len(s)-1:
        
        if s[i]>s[i+1]:
            
            s[i],s[i+1] = s[i+1],s[i]
            
            swapped = True
        i = i+1
    
    
    if swapped == False:
        break
print (s)
