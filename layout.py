from dash import html, dcc

def create_header():
    return html.Div([
        html.H3("Business Analytics Dashboard", className="text-center m-4")
    ], className="container-fluid bg-light")

def create_filters(df):
    return html.Div([
        html.H4("Filters", className="card-header"),
        html.Div([
            html.Label("Select Metric:"),
            dcc.Dropdown(
                id='metric-dropdown',
                options=[
                    {'label': 'Sales', 'value': 'Sales'},
                    {'label': 'Expenses', 'value': 'Expenses'},
                    {'label': 'Customers', 'value': 'Customers'}
                ],
                value='Sales',
                className="mb-3"
            ),
            
            html.Label("Date Range:"),
            dcc.RangeSlider(
                id='month-slider',
                min=0,
                max=11,
                step=1,
                marks={i: df['Month'][i] for i in range(len(df['Month']))},
                value=[0, 11],
                className="mb-3"
            )
        ], className="card-body")
    ], className="card mb-4")

def create_key_metrics():
    return html.Div([
        html.H4("Key Metrics", className="card-header"),
        html.Div([
            html.Div([
                html.Div(id='total-sales', className="text-center p-3"),
                html.Div(id='avg-monthly', className="text-center p-3"),
                html.Div(id='growth-rate', className="text-center p-3")
            ], className="d-flex justify-content-around")
        ], className="card-body")
    ], className="card mb-4")

def create_charts():
    return html.Div([
        html.Div([
            html.Div([
                html.H4("Monthly Trend", className="card-header"),
                dcc.Graph(id='line-chart')
            ], className="card mb-4")
        ], className="col-md-8"),
        
        html.Div([
            html.Div([
                html.H4("Comparison", className="card-header"),
                dcc.Graph(id='bar-chart')
            ], className="card mb-4")
        ], className="col-md-4")
    ], className="row container mx-auto")

def create_layout(df):
    return html.Div([
        create_header(),
        create_filters(df),
        create_key_metrics(),
        create_charts()
    ], className="container")
