import dash
from data import load_data
from layout import create_layout
from callbacks import register_callbacks

app = dash.Dash(
    __name__, 
    external_stylesheets=['https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css']
)

df = load_data()
app.layout = create_layout(df)
register_callbacks(app, df)

if __name__ == '__main__':
    app.run_server(debug=True)
