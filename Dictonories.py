studentinfo ={
    "sajib" :{
        "Location" :"Tangail",
        "Study": "University",
        "StudentId": 201902103,
        "Number": 1798585333

    },
    "Hasan": {
        "Location": "Tangail",
        "Study": "University",
        "StudentId": 201902103,
        "Number": 1798585333

    }

}
print(studentinfo)
print(studentinfo["sajib"]["Location"])


#Accesing item
x = studentinfo.get("sajib")
print(x)
k= studentinfo.keys()

y = studentinfo.items()
print(y)
print(k)
# loop in dictonary
for x  in studentinfo:
    print(x)
    for a in studentinfo.values():
        print(a)