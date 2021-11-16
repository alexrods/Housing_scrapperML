from flask import Flask
import pandas as pd
from model import ideal_houses


app = Flask(__name__)


@app.route("/ideal_house", methods=['GET'])
def ideal_house():
	df = pd.read_csv('data_houses.csv')
	options = {}
	for i in range(5):
		options[i+1] = {"Score": houses[i][0], "URL": df['URl'][houses[i][1]]}
	
	return options


if __name__ == '__main__':	
    #scrap_houses()    
    houses = ideal_houses(1,1,1,1,1)
    app.run(debug=True, port=8080)




