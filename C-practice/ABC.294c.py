n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = sorted(A+B)

get_index = {c: i+1 for i, c in enumerate(C)}

#print(get_index)

for i in A:
    print(get_index[i],end=" ")

print()

for i in B:
    print(get_index[i],end=" ")
