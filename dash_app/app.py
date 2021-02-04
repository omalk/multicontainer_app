import sys
import time

import dash
import dash_html_components as html

from elasticsearch import Elasticsearch, exceptions

es = Elasticsearch(host='es')


def test_connection(retry=3):
    """ connect to ES with retry """
    if not retry:
        print("Out of retries. Bailing out...")
        sys.exit(1)
    try:
        status = es.indices.exists("test_index")
        return status
    except exceptions.ConnectionError as e:
        print("Unable to connect to ES. Retrying in 5 secs...")
        time.sleep(5)
        test_connection(retry - 1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[html.H1(children='Hello Dash')])

if __name__ == '__main__':
    test_connection()
    app.run_server(host="0.0.0.0", debug=True)