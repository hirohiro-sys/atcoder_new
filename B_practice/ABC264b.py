n,b = map(int,input().split())
li = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
      [1,2,1,1,1,1,1,1,1,1,1,1,1,2,1],
      [1,2,1,2,2,2,2,2,2,2,2,2,1,2,1],
      [1,2,1,2,1,1,1,1,1,1,1,2,1,2,1],
      [1,2,1,2,1,2,2,2,2,2,1,2,1,2,1],
      [1,2,1,2,1,2,1,1,1,2,1,2,1,2,1],
      [1,2,1,2,1,2,1,2,1,2,1,2,1,2,1], #真ん中
      [1,2,1,2,1,2,1,1,1,2,1,2,1,2,1],
      [1,2,1,2,1,2,2,2,2,2,1,2,1,2,1],
      [1,2,1,2,1,1,1,1,1,1,1,2,1,2,1],
      [1,2,1,2,2,2,2,2,2,2,2,2,1,2,1],
      [1,2,1,1,1,1,1,1,1,1,1,1,1,2,1],
      [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
print("black" if li[n-1][b-1]==1 else "white")