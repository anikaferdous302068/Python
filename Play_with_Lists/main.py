L =[4,5,1,2,9,7,10,8]
print("Original List: ",L)
count=0
for i in L:
    count+=1
ave=count/len(L)
print("Sum of the list: ",count)
print("Average of the list: ",ave)
L.sort()
print("Smallest element in the list: ",L[0])
print("Largest element in the list: ",L[-1])