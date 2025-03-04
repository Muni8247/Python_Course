set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3={7,8,9,10,11}

print(type(set1))
print(type(set2))
print(type(set3))

print(set1)
print(set2)

#UNION
print(set1.union(set2))

print(set1 | set2)

print(set1 | set2 | set3)

#INTERSECTON
print(set1.intersection(set2))
print(set1.intersection(set3))
print(set2.intersection(set3))

print(set1.intersection(set2,set3))

#DIFFERENCE
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.difference(set3))
print(set2.difference(set3))
print(set1.difference(set2,set3))

#DIFFERENCE UPDATE
print("##############DIFFERENCE UPDATE###################")
set1.difference_update(set2)
print(set1)
set2.difference_update(set3)
print(set2)


#SYMMETRIC DIFFERENCE
print("*****************SYMMETRIC DIFFERENCE********************")
set4={"Muni","Swarna","Dileep","Lokesh"}
set5={"Swarna","Yash","Yakshith"}
print(set4.symmetric_difference(set5))