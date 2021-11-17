from flask import Flask
from flask import request
from model import ideal_houses
import pandas as pd


app = Flask(__name__)


@app.route("/ideal_house", methods=['GET', 'POST'])
def ideal_house():
	# take requests from browser
	surface = int(request.args.get('surface'))
	bathrooms = int(request.args.get('bathrooms'))
	bedrooms = int(request.args.get('bedrooms'))
	parking = int(request.args.get('parking'))
	price = int(request.args.get('price'))
	scrap = str(request.args.get('scrap'))
	# Option to web scraping
	if scrap == "true":
		scrap_houses() 
	
	# read data
	df = pd.read_csv('data_houses.csv')
	# feed the model function 
	houses = ideal_houses(surface, bathrooms, bedrooms, parking, price)
	# compile results
	options = {}
	for i in range(5):
		options[i+1] = {"Score": houses[i][0], "URL": df['URl'][houses[i][1]]}
	
	return options


if __name__ == '__main__':

    app.run(debug=True, port=8080)




