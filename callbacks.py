from dash.dependencies import Input, Output
import plotly.express as px
from dash import html

def update_line_chart(selected_metric, month_range, df):
    filtered_df = df.iloc[month_range[0]:month_range[1]+1]
    fig = px.line(
        filtered_df,
        x='Month',
        y=selected_metric,
        markers=True,
        title=f'Monthly {selected_metric}'
    )
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title=selected_metric,
        template='plotly_white'
    )
    return fig

def update_bar_chart(month_range, df):
    filtered_df = df.iloc[month_range[0]:month_range[1]+1]
    avg_data = {
        'Metric': ['Sales', 'Expenses', 'Customers'],
        'Average': [
            filtered_df['Sales'].mean(),
            filtered_df['Expenses'].mean(),
            filtered_df['Customers'].mean() * 10  # Scaling for better visualization
        ]
    }
    fig = px.bar(
        avg_data,
        x='Metric',
        y='Average',
        title='Average Metrics',
        color='Metric'
    )
    fig.update_layout(template='plotly_white')
    return fig

def update_metrics(selected_metric, month_range, df):
    filtered_df = df.iloc[month_range[0]:month_range[1]+1]
    total = filtered_df[selected_metric].sum()
    avg = filtered_df[selected_metric].mean()

    # Calculate growth rate
    first = filtered_df[selected_metric].iloc[0]
    last = filtered_df[selected_metric].iloc[-1]
    growth = ((last - first) / first) * 10 if first > 0 else 0

    return [
        html.Div([
            html.H3(f"${total:,.0f}" if selected_metric != 'Customers' else f"{total:,.0f}"),
            html.P(f"Total {selected_metric}")
        ]),
        html.Div([
            html.H3(f"${avg:,.0f}" if selected_metric != 'Customers' else f"{avg:,.0f}"),
            html.P(f"Avg {selected_metric}")
        ]),
        html.Div([
            html.H3(f"{growth:+.1f}%"),
            html.P("Growth Rate")
        ])
    ]

def register_callbacks(app, df):
    @app.callback(
        Output('line-chart', 'figure'),
        [Input('metric-dropdown', 'value'),
         Input('month-slider', 'value')]
    )
    def line_chart_callback(selected_metric, month_range):
        return update_line_chart(selected_metric, month_range, df)

    @app.callback(
        Output('bar-chart', 'figure'),
        [Input('month-slider', 'value')]
    )
    def bar_chart_callback(month_range):
        return update_bar_chart(month_range, df)

    @app.callback(
        [Output('total-sales', 'children'),
         Output('avg-monthly', 'children'),
         Output('growth-rate', 'children')],
        [Input('metric-dropdown', 'value'),
         Input('month-slider', 'value')]
    )
    def metrics_callback(selected_metric, month_range):
        return update_metrics(selected_metric, month_range, df)
