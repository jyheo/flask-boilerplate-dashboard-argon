import dash
import dash_html_components as html

def register_dash(server, _):
    app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dashapp/app1/'
    )

    app.layout = html.Div(_("My Dash app"))
