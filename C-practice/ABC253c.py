import heapq  # heapqモジュールをインポート
from collections import defaultdict  # defaultdictモジュールをインポート

mx = []  # 最大ヒープ（マイナスの値で表現される）を表すリスト
mn = []  # 最小ヒープを表すリスト
cnt = defaultdict(int)  # 値とその出現回数を記録するデフォルト辞書
q = int(input())  # クエリの数を受け取る変数

# クエリの処理をループで実行
for _ in range(q):
    query = list(map(int, input().split()))  # スペース区切りの整数からなるクエリをリストに変換

    # クエリの種類を識別する
    if query[0] == 1:  # クエリタイプ1
        x = query[1]
        cnt[x] += 1  # 出現回数を増やす
        heapq.heappush(mx, -x)  # 最大ヒープに要素を追加
        heapq.heappush(mn, x)  # 最小ヒープに要素を追加

    if query[0] == 2:  # クエリタイプ2
        x, c = query[1:]
        cnt[x] = max(0, cnt[x] - c)  # 出現回数を減少させる

    if query[0] == 3:  # クエリタイプ3
        while cnt[-mx[0]] == 0:
            heapq.heappop(mx)  # 最大ヒープから要素を取り出す
        while cnt[mn[0]] == 0:
            heapq.heappop(mn)  # 最小ヒープから要素を取り出す
        print(-mx[0] - mn[0])  # 最大値と最小値を合計して出力
