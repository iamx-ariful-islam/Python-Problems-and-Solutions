# pip install pandas
# pip install plotly

import plotly.express as px


# sample data
data = {
    'id': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'parent': ['', 'A', 'A', 'B', 'B', 'C', 'D'],
    'value': [10, 15, 7, 8, 12, 6, 5]
}

# create a sunburst chart
fig = px.sunburst(data, names='id', parents='parent', values='value')

# set the chart title
fig.update_layout(title_text='Sunburst Chart')

# show the chart
fig.show()