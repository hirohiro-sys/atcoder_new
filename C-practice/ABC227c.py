N = int(input())  # ユーザーから整数Nを入力
ans = 0  # 答えを格納する変数を初期化

# aとbをループで増やしながら計算
for a in range(1, N+1):  # aを1からNまでの範囲で変化させる
    if a * a * a > N:  # a^3 が N より大きい場合、内側のループを終了
        break
    for b in range(a, N+1):  # bをaからNまでの範囲で変化させる
        if a * b * b > N:  # a * b^2 が N より大きい場合、内側のループを終了
            break
        ans += N // a // b - b + 1  # ans に N / (a * b) - b + 1 の値を加算

print(ans)  # 答えを出力
