from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import json

# Initialize the Dash app
app = Dash(__name__)

# Load your JSON data
with open('eve.json', 'r') as file:
    data = [json.loads(line) for line in file]

# Normalize JSON data
df = pd.json_normalize(data)

# Convert timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create figures
fig1 = px.line(df, x='timestamp', y='flow_id', title='Events Over Time')
fig2 = px.bar(df, x='src_ip', y='flow_id', title='Source IP Address Distribution')
fig3 = px.histogram(df, x='alert.severity', title='Alert Severity Distribution')

# Apply dark theme
for fig in [fig1, fig2, fig3]:
    fig.update_layout(template='plotly_dark')

# Define layout
app.layout = html.Div(style={'backgroundColor': '#303030', 'color': 'white'}, children=[
    html.H1("Network Alert Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(id='line-graph', figure=fig1),
    dcc.Graph(id='bar-graph', figure=fig2),
    dcc.Graph(id='histogram-graph', figure=fig3),
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
