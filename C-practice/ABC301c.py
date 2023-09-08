# collectionsモジュールからdefaultdictをインポート
from collections import defaultdict

# 2つの文字列SとTを入力
S = input()
T = input()

# SとT内の各文字の出現回数を格納するデフォルトディクショナリScntとTcntを作成
Scnt = defaultdict(int)
Tcnt = defaultdict(int)

# 文字列S内の各文字の出現回数を計算し、Scntに格納
for c in S:
    Scnt[c] += 1

# 文字列T内の各文字の出現回数を計算し、Tcntに格納
for c in T:
    Tcnt[c] += 1

# 'atcoder'という文字列内の各文字に対して処理を実行
for c in "atcoder":
    # Mは、Scnt[c]とTcnt[c]のうちの大きい方の値を取得
    M = max(Scnt[c], Tcnt[c])
    
    # '@'の出現回数がM-Scnt[c]よりも少ない場合、または
    # '@'の出現回数がM-Tcnt[c]よりも少ない場合、"No"を出力してプログラム終了
    if Scnt['@'] < M - Scnt[c] or Tcnt['@'] < M - Tcnt[c]:
        print("No")
        exit()
    
    # '@'の出現回数からM-Scnt[c]を引き、Scnt[c]にMを代入
    Scnt['@'] -= M - Scnt[c]
    Scnt[c] = M
    
    # 同様に、Tcnt[c]にもMを代入して不足する文字を補充
    Tcnt['@'] -= M - Tcnt[c]
    Tcnt[c] = M

# ループが終了した後、ScntとTcntが等しい場合、"Yes"を出力
# そうでない場合、"No"を出力
print("Yes" if Scnt == Tcnt else "No")
