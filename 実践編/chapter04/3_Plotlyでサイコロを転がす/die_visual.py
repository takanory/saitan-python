from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# D6を作成する
die = Die()

# サイコロを転がし、結果をリストに格納する
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 結果を分析する
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 結果を可視化する
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '結果'}
y_axis_config = {'title': '発生した回数'}
my_layout = Layout(title='6面のサイコロを1000回転がした結果',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
