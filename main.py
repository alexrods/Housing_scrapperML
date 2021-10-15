import pandas as pd
from model import ideal_houses
from scrapper import scrap_houses

# Show the most close top 5 houses from ideal house
if __name__ == '__main__':
    scrap_houses()
    df = pd.read_csv('data_houses.csv')
    houses = ideal_houses()
    print('TOP 5 best options: ')
    for i in range(5):
        print(f'[{i +1}] ', 'Score: ', houses[i][0], '\nURL: ', df['URl'][houses[i][1]])
