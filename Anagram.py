'''
Write a python function, check_anagram() which accepts two 
strings and returns True, if one string is an anagram of 
another string. 
Otherwise returns False.
The two strings are considered to be an anagram if they
 contain repeating characters but none of the characters repeat at the same position.
The length of the strings should be the same.
'''

def check_anagram(data1,data2):
    
    a1=data1.lower()
    a2=data2.lower()
    if len(data1)!=len(data2): 
        return False   
    list1=[]
    list2=[]
    for i in a1:  
        list1.append(i)
    for i in a2:
        list2.append(i)        
    flag=1 
    for i in range(0,len(data1)):  
        if list1[i]==list2[i]:
            flag=0 
            break       
    if flag==0:
        return False    
    list1.sort()
    list2.sort()    
    if list1==list2:  
        return True 
    else:
        return False
print(check_anagram("eat","ate"))
print(check_anagram("tie","ate"))
