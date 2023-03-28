"""
Given two lists, both having String elements, write a python program using
python lists to create a new string as per the rule given below:
The first element in list1 should merged with last element in list2, second element
in list1 should be merged with second last element in list2 and so on. If an element
in list1/list2 is None, then the corresponding element in the other list should
be kept as it is in the merged list.
Sample Input
list1=['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']

list2=['y', 'tor', 'e', 'eps', 'ay', 'None' 'le', 'n']

Sample Output
"An apple a day keeps the doctor away"
"""
list1 = ['A','app','a','d','ke','th','doc','awa']
list2 = ['y','tor','e','eps','ay',None,'le','n']
list2rev = list2[::-1]

for i in range(len(list1)):
    if(list2rev[i] == None):
        print(list1[i] + '',end=" ")
    else:
        
        print(list1[i]+list2rev[i],end = " ")
