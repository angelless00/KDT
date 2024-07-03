ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
diff=0
for i in range(1,4):
    diff=diff+ohlc[i][3]-ohlc[i][0]
print(diff)





















