# pip install dash
# pip install dash-core-components
# pip install dash-html-components

import dash
import dash_core_components as dcc
import dash_html_components as html


# create a dash application
app = dash.Dash(__name__)


# define the layout of the dashboard
app.layout = html.Div(
    children = [
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'Data':[
                    {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'Bar chart'},
                    {'x':[1,2,3], 'y':[2,4,5], 'type':'line', 'name':'Line chart'},
                    ],
                'layout':{
                    'title': 'Graph title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'}
                    }
                }
            )
        ]
    )


# run the application
if __name__=='__main__':
    app.run_server(debug=True)
