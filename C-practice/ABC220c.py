n = int(input())  # 入力: 数列の要素数
a = list(map(int, input().split()))  # 入力: 数列の要素
x = int(input())  # 入力: 目標値

sum_val = sum(a)  # 数列の要素の合計を計算
P = x // sum_val  # 数列の合計値を何回足し合わせることで目標値Xに近づけることができるかの値
sumb = P * sum_val  # 数列の合計値を何回足し合わせるかの値
ans = P * n  # 初期値

for val in a:
    sumb += val  # 数列の要素を順番に sumb に足し合わせる
    ans += 1  # 回答数をインクリメント

    if sumb > x:  # sumb が目標値 x を超えた場合
        print(ans)  # 現在の回答数を出力
        break  # ループを終了
