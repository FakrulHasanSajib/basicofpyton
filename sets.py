mysets= {1,"false","string" "1"}
print(mysets)
print(type(mysets))
print(len(mysets))
#access the set item
for i in mysets:
    print(i)
#remove set items
mysets ={1,2,3,4,5,6}
mysets.remove(4)
print(mysets)
set1 = {"a","b","c"}
set2 ={ 1,2,3}
print(set1.union(set2))