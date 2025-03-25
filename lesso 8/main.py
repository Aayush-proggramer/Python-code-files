t1=(1,2,3,4 )
t2=(1,2,3,5,6,("hi", "hello"))
t3=()
print(t1)
print(t2)
print(t3)
print(t1 [2])
print(t1 [1:3])
print(t2 [5][0])
for i in t1:
    print(i)

#sets
A = {1,1,2,2,3,4,5}
B = {5,5,6,7,8,8,9}
A.add(10)
print(A)
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.symmetric_difference(B))