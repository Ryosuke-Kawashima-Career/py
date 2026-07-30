import numpy as np
US_TO_INR = 75
def solution1():
    flower_to_month = np.array([
        [50, 60, 25],
        [10, 13, 5],
        [40, 70, 52],
    ])
    flower_prices = np.array(
        [20, 30, 15]
    ).reshape((3, 1))
    month_prices = flower_to_month.transpose().dot(flower_prices)
    print("Total sales in every month: ", month_prices * US_TO_INR)

if __name__ == '__main__':
    solution1()
