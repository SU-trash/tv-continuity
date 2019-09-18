#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly # Plotly 3.4.1 appears to be the last stable release
import plotly.graph_objs as go

app = dash.Dash()

# Points at (0,0) and (1,1)
node_trace = go.Scatter(x=(0, 1), y=(0, 1),
        hoverinfo='none',
        showlegend=False,
        mode='markers',
        marker=dict(
            color=[],
            size=5,
            line=dict(width=1)),
        visible=True) # The thickness of the node's border line

# Single edge connecting the points
edge_trace = go.Scatter(x=[0, 1, None], y=[0, 1, None],
                        mode='lines',
                        name='Plot Threads',
                        line=dict(width=0.5, color='black'),
                        hoverinfo='none',
                        visible=True) #='legendonly')

fig_layout = go.Layout(
    title=f'<br><b>Dash test</b>',
    titlefont=dict(size=16),
    showlegend=True,
    legend=dict(x=0.9, y=0.95),
    # If hovermode is set to 'closest', it picks any node close enough to the mouse's position
    # If set to e.g. 'x', picks the node (any distance away) which is closest to the mouse's x
    # position.
    hovermode='closest',
    dragmode='pan', # Default mouse mode
    margin=dict(b=5, l=5, r=5, t=40, pad=0),
    annotations=[ dict(
        text="Click on legend items to show/hide them.",
        showarrow=False,
        xref="paper", yref="paper",
        x=1.0, y=1.0) ],
    # Maintain the x-y ratio so the plot is a semicircle regardless of screen size
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
               scaleanchor='x', scaleratio=1, range=[-0.05, 1.05]))

app.layout = html.Div([
    html.Div(
        [dcc.Graph(
            id='the-graph',
            figure={'data': [node_trace, edge_trace],
                    'layout': fig_layout},
            hoverData=None,
            clear_on_unhover=True)
        ])
        #style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'})
])


if __name__ == '__main__':

    @app.callback(dash.dependencies.Output('the-graph', 'figure'),
                  [dash.dependencies.Input('the-graph', 'hoverData')],
                  [dash.dependencies.State('the-graph', 'figure')])
    def update_graph(hover_data, cur_figure):
        # Hover data is formatted as e.g.:
        # {"points": [{
        #  "curveNumber": 0,
        #  "customdata": "c.a",
        #  "pointIndex": 0,
        #  "pointNumber": 0,
        #  "text": "a",
        #  "y": 4,
        #  "x": 1}] }
        #{'curveNumber': 0, 'pointNumber': 0, 'pointIndex': 0, 'x': 0, 'y': 0}
        # {'curveNumber': 0, 'pointNumber': 1, 'pointIndex': 1, 'x': 1, 'y': 1}
        # {"points": [{'curveNumber': 0, 'pointNumber': 1, 'pointIndex': 1, 'x': 1, 'y': 1}]}

        # Hide the graph's edge while any point is being hovered over
        if hover_data is not None:
            point = hover_data['points'][0]
            print(point)
            if point['pointIndex'] == 0:
                cur_figure['data'][1]['x']=(0, 1, None)
                cur_figure['data'][1]['y']=(0, 1, None)
            else:
                cur_figure['data'][1]['x']=()
                cur_figure['data'][1]['y']=()

            print("Updating data:")
            print(cur_figure['data'][1])

        return cur_figure

    app.run_server(debug=True)
