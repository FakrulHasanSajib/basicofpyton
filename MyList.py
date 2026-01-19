li = [1,2,3,4,5,6,7,8,9,]
print(li)
print(type(li))
li[1] = 10
print(li)
lis=["sajib","hasan"]
print(lis)
list=['true','false','true',]
print(type(list))
#Access list item
sajib= ["chanel name ","website","group","pages"]

print(sajib[1])
#append
sajib.append("google")
sajib.append(12)
print(sajib)
sajib.insert(2,"python ")
print(sajib)
#The remove method() remove the specific item.
sajib.remove("website")
print(sajib)
#the pop method remove the specific index
sajib.pop(0)
print(sajib)
#pop er parenthesis er vitore jodi kono index number na dei tahole last theke remove korbe
#The dell keyword also remove the specific keyword
del sajib[3]
print(sajib)
#clear the list
sajib.clear()
print(sajib)