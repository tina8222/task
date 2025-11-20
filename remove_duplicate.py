list = [1,1,2,3,3]
duplicate = {x for x in list if list.count(x) > 1}
newlist = [x for x in list if x not in duplicate]
        
print(newlist)

        
 
 
 
 
 
 
 