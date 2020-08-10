import os

# 先判斷202007.txt檔案是否存在, 若存在就先刪除
if os.path.exists(r"C:\D\期交所資料\202007.txt"):
    os.remove(r"C:\D\期交所資料\202007.txt")

# 再跑迴圈遍歷一次
for root, dirs, files in os.walk(r"C:\D\期交所資料\\"):
    for i in range(0, len(files)):
        # 開啓檔案與逐行串接到c中
        f = open(r"C:\D\期交所資料\\" + files[i], "r")
        c = f.read()

        # 寫入202007.txt檔案中
        fw = open(r"C:\D\期交所資料\202007.txt", "a")
        fw.write(c + "\n")  # 設計1個換行符號

print("合併完成")
f.close()
fw.close()