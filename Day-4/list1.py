l1=[1,4,8,10,12,14]
l2=["Muni","Naga","Reddy","Kati"]
l3=[10,"Muni",10.5,True]

print(l1)
print(l2)
print(l3)
# Adding Elements
print("******After Adding********")
l1.append(20)
l2.append("Swarna")
l3.append(False)
print(l1)
print(l2)
print(l3)

l1.insert(1,100)
l2.insert(1,False)
print(l1)
print(l2)

l1.extend([1000,900])
print(l1)

# Removing Elements

l1.remove(1000)
print(l1)

l1.pop()
print(l1)
#l1.clear()
print(l1)

# Finding Elements
print(l2.index("Muni"))
print(l2.index("Kati"))

print(l1.count(4))
l1.append(10)
print(l1.count(10))

# Sorting & Reversing
print(l1.reverse())
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
print(l1)

# Copying
l1.copy()
print(l1)