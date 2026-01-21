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