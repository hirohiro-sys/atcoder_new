#入力
h,w = map(int,input().split())
li = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        #8方向
        for x,y in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
            #文字が一致 & 盤面の範囲内かをチェック
            if all(0<=i+n*x<h and 0<=j+n*y<w and li[i+n*x][j+n*y]==s for n,s in enumerate("snuke")):
              　　　　#出力
                for n in range(5):
                    print(i+n*x+1,j+n*y+1)
                exit()
