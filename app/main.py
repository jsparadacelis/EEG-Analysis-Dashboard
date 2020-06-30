import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from invoker import Invoker


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(id='my-div'),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': u'Regresión Logística', 'value': 'RL'},
            {'label': 'Redes Neuronales', 'value': 'NN'},
            {'label': u'Máquinas de Soporte Vectorial', 'value': 'SVM'}
        ],
        id='model-type',
        value='NN'
    ),

    html.Label('Slider'),
    dcc.Slider(
        min=200,
        max=800,
        marks={i: str(i) for i in range(200, 801, 100)},
        value=400,
        id='exams-qt'
    ),
], style={'columnCount': 1})


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [
        Input(component_id='exams-qt', component_property='value'),
        Input(component_id='model-type', component_property='value'),

    ]
)
def update_output_div(exams_quantity, model_type):
    model = Invoker.get_model(model_type)
    model.train()
    return "Holiii"


if __name__ == '__main__':
    app.run_server(debug=True)
