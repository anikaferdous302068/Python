setx={"apple", "banana", "cherry", "blue"}
sety={"banana", "blue", "grape", "orange"}
print("Original set elements:")
print("Set x:", setx)
print("Set y:", sety)
print("Intersection of two said sets:")
setz=setx.intersection(sety)
print("Set z:", setz)

print("Union of two said sets:")
setu=setx.union(sety)
print("Set u:", setu)

seta=setu-setz
print("Difference of two said sets:")
print(seta)
