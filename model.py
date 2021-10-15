"""
Here use a subtraction of vectors for calculate distance between ideal house and all options in the list
the order is
[surface, number bathrooms, bedrooms, number parking, price]
"""
import numpy as np
from data_engineering import clean_data


def ideal_houses():
    try:
        ideal_house = np.array([2, 2, 1, 1, 3])
        list_options = clean_data()

        results = []
        for i, option in enumerate(list_options):
            distance = [np.linalg.norm(ideal_house - option), i]
            results.append(distance)

        results.sort()

        return results

    except Exception as e:
        print(e)
