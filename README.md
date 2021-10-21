# Housing_scrapperML

## The objective of this project is collect rents housing information in my city, and returns a list of the five best rent choices according to a list of defined characteristics.

In this project i make a [web scraping](https://github.com/alexrods/Housing_scrapperML/blob/main/scrapper.py) to the rents housing information of my city from [MercadoLibre](https://www.mercadolibre.com.mx/c/inmuebles). Later [clean data](https://github.com/alexrods/Housing_scrapperML/blob/main/data_engineering.py) and prepare for evaluate the model [Ideal house rent](https://github.com/alexrods/Housing_scrapperML/blob/main/model.py).

### Instructions

* Download or clone the repository
![](https://drive.google.com/uc?id=1LW3XUCQK8kBI4YEKnnx3o7d0XkJ-BUc3)

* Create virtual environment, in the root of project
		
		python -m venv venv
		
* Activate virtual environment 
		
		# Windows
		.\venv\Scripts\activate
		
		#Linux
		source venv/bin/activate
		
* Install requirements.txt
		pip install -r requirements.txt
* If you want make scraping to other ubication modify the line 42 of [scraper](https://github.com/alexrods/Housing_scrapperML/blob/main/scrapper.py) HOME_URL variable:
![](https://drive.google.com/uc?id=1KqsiGep4Ckvh2KEWaLkOEcYQMCCBWnkk)

* Run main.py
		python main.py
		# Results
![](https://drive.google.com/uc?id=1cJIaePs_YfGRGyJ6rlNs8yIv_JL0dzYw)

