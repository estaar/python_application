from flask import Flask
import pandas as pd
# import requests

app = Flask(__name__)


def get_data():
    df = pd.read_csv('Populationincounty.csv', thousands=',')
    return df


@app.route('/')
def county():
    get_data()
    df3 = get_data()
    df4 = df3.query('Total_Population19 >= 1500000').copy()
    return df4.to_html()


if __name__ == '__main__':
    app.run()
