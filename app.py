from dash import Dash, html, dcc
from dash.dependencies import Input, Output

app = Dash(__name__)
server = app.server  # useful for deployment

app.layout = html.Div(
    className="container",
    children=[
        html.H1("My First Dash App"),
        html.P("Simple Dash application structure"),

        dcc.Input(
            id="name-input",
            type="text",
            placeholder="Enter your name"
        ),

        html.Br(),
        html.Br(),

        html.Div(id="output-text")
    ]
)

@app.callback(
    Output("output-text", "children"),
    Input("name-input", "value")
)
def update_output(name):
    if name:
        return f"Hello, {name} 👋"
    return "Please enter your name"

if __name__ == "__main__":
    app.run_server(debug=True)
