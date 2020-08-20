import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
# filename = 'data/sitka_weather_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 各項目のインデックスを取得する
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # ファイルから日付と最高気温、最低気温を取得する
    dates, highs, lows = [], [], []
    for row in reader:
        # 観測所の名前が設定されていない場合は、名前を取得する
        if not place_name:
            place_name = row[name_index]
            # print(place_name)

        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 最高気温と最低気温をグラフに描画する
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# グラフにフォーマットを指定する
title = f"Daily high and low temperatures - 2018\n{place_name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# plt.savefig('5_4_auto_indexes.png')
plt.show()
