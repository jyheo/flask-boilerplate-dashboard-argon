import dash
import dash_core_components as dcc
import dash_html_components as html


def register_dash(server, _):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dashapp/app2/',
        external_stylesheets=external_stylesheets
    )

    app.layout = html.Div(children=[
        html.H1(children=_('Hello Dash')),

        html.Div(children=_('''
            Dash: A web application framework for Python.
        ''')),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': _('SF')},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': _(u'Montréal')},
                ],
                'layout': {
                    'title': _('Dash Data Visualization')
                }
            }
        )
    ])
