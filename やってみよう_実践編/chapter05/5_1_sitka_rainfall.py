import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # ファイルから日付と降水量を取得する
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)

# 降水量をグラフに描画する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

# グラフにフォーマットを設定する
plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# plt.savefig('5_1_sitka_rainfall.png')
plt.show()
