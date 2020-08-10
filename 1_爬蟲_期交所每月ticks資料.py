import time
import zipfile
import requests

# 獲取今天的字符串
today_y = time.strftime("%Y", time.localtime(time.time()))
today_m = time.strftime("%m", time.localtime(time.time()))
today_d = time.strftime("%d", time.localtime(time.time()))
print(today_y)
print(today_m)
print(today_d)

if today_m == "01":
    today_y = str(int(today_y) - 1)

for i in range(31, 0, -1):
    if today_m != "01":
        today_m1 = int(today_m) - 1
        today_m1 = "{:0>2d}".format(today_m1)
    else:
        today_m1 = "12"

    url_a = 'https://www.taifex.com.tw/file/taifex/Dailydownload/DailydownloadCSV/Daily_' + today_y + '_' + today_m1 + '_' + "{:0>2d}".format(
        i) + '.zip'
    zip_name = 'Daily_' + today_y + '_' + today_m1 + '_' + "{:0>2d}".format(i) + '.zip'
    csv_name = 'Daily_' + today_y + '_' + today_m1 + '_' + "{:0>2d}".format(i) + '.csv'

    try:
        # 根據url，直接下載zip檔
        url = url_a
        r = requests.get(url)
        with open(r"C:\D\期交所資料\\" + zip_name, "wb") as code:  # 儲存程自訂的檔名
            code.write(r.content)

        # 以下解壓縮
        with zipfile.ZipFile(r"C:\D\期交所資料\\" + zip_name, 'r') as myzip:  # 你要解壓縮哪個檔
            myzip.extract(csv_name)  # 解壓縮裡面的檔案是甚麼?

    except zipfile.BadZipFile:
        print("今日沒有抓取數據")
