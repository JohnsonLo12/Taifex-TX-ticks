import sqlite3

conn = sqlite3.connect("ticks.db")  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 先判斷member01存在與否,若存在先DROP掉
sqlstr = "DROP TABLE IF EXISTS ticks"
cursor.execute(sqlstr)

# 建立一個資料表 member01
sqlstr = "CREATE TABLE IF NOT EXISTS ticks ('Date' DATETIME,'ID' TEXT,'Month' TEXT,'Time' TEXT,'Price' INTEGER,'VOL' INTEGER)"
cursor.execute(sqlstr)

f = open(r"C:\D\期交所資料\202007.txt", "r")
list1 = f.readlines()

# print(list1)
for i in range(10, len(list1)):
    list2 = list1[i].split(",")
    if len(list2) >= 6 and list2[4] != "成交價格":
        sqlstr = "INSERT INTO ticks VALUES('{}','{}','{}','{}',{},{})".format(list2[0], list2[1].strip(),
                                                                              list2[2].strip(), list2[3], list2[4],
                                                                              list2[5])
        # print(sqlstr)
        cursor.execute(sqlstr)

sqlstr1 = "SELECT * FROM ticks"
m = cursor.execute(sqlstr1)
conn.commit()  # 主動更新
# print(list(m))
conn.close()  # 關閉資料庫連
print("寫入成功!!!")
