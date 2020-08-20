import csv
from datetime import datetime

from plotly.graph_objs import Layout
from plotly import offline

num_rows = 10_000

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 明るさ、緯度と経度、日付を取得する
    dates, brightnesses = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{date:%Y年%m月%d日} - {brightness}"

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)

        row_num += 1
        if row_num == num_rows:
            break

# 火事の地図を作成する
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': '明るさ'},
    },
}]

my_layout = Layout(title='世界の火事')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='5_9_world_fires.html')
