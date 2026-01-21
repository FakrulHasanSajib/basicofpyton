tuples = (1,2,3,4,5,6,7,8,9)
print(type(tuples))
print(tuples[-1])
print(tuples[:2])
print(tuples[-5])
#rnage of index
print(tuples[5:9])
#update tuples
thistuple =("orange","banana","mango","apple")
a = list(thistuple)
a.append("qiki")
thistuple = tuple(a)
print(thistuple)
# unpack tuple
fruits = ["apple","banana","mango"]
(a,b,c) = fruits
print(a)
print(b)
print(c)
#tuple loop
for x in fruits: print(x)
for i in range(len(fruits)):print(i)
f = ["apple","banana","mango"]
i=1
while i<len(f):
    print(f[i])
    i=i+1

fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(len(fruits))


