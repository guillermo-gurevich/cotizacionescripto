import requests
from flask import Flask, render_template, request

app = Flask(__name__)

SYMBOLS = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC', 'SOL', 'LUNA', 'XRP', 'ADA', 'UST', 'BUSD', 'DOGE', 'DOT', 'AVAX', 'SHIB']

@app.route('/')
def index():
    
    return render_template('index.html', symbols=SYMBOLS)

@app.route('/select', methods=['GET', 'POST'])
def select():
    select = request.form.get('comp_select')
    url='https://api.coincap.io/v2/assets'
    response = requests.get(url)
    data = response.json().get('data')
    ind = (SYMBOLS.index(select))
    priceUsd = float(data[ind].get('priceUsd'))
    name = data[ind].get('name')
    if priceUsd >= 1:
        priceUsd = round(priceUsd, 2)
    else:
        priceUsd= round(priceUsd, 4)  
    change = round(float(data[ind].get('changePercent24Hr')), 2)
    return render_template('select.html', name=name, priceUsd=priceUsd, change=change) 

if __name__=='__main__':
    app.run(debug=True)