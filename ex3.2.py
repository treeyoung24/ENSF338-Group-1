import json
import timeit
from matplotlib import pyplot as plt
import numpy as np


f = open('large-file.json', 'r', encoding='utf-8')
data = json.load(f)

def change_size(n):
    i = 0
    while i < n:
        for record in data:
                if 'size' in record['payload']:
                    record['payload']['size'] = 42
                    i += 1
    return 0

def change():
    avgtimes = []
    listlengths = [1000, 2000, 5000, 10000]
    for listlength in listlengths:
        rez = []
        tm = timeit.timeit(lambda: change_size(listlength), number=100)
        rez.append(tm/100)
        avg = sum(rez) / len(rez)
        avgtimes.append(avg)
        print("Average time for list of length %d: %f" % (listlength, avg))
    return listlengths, avgtimes

def linear_regression(listlengths, avgtimes):
    slope, intercept = np.polyfit(listlengths, avgtimes, 1)
    plt.scatter(listlengths, avgtimes)
    linevalues = [slope * x + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'r')
    print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
    return 0

def main():
    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
    listlengths, avgtimes = change()
    linear_regression(listlengths, avgtimes)

if __name__ == "__main__":
    main()