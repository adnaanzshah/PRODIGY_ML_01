l1=[1,2,3]
l2=[2,4,6]
l3=[]
i=0
# print(321+642)
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
    i=i+1
    print(f"i is {i} , l3[i] is {l3[i-1]}")