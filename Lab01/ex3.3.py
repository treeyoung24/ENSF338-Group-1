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
    listlengths = [1000]
    for listlength in listlengths:
        rez = timeit.repeat(lambda: change_size(listlength), repeat=1000, number=1)
    return rez

def histogram(rez):
    plt.hist(rez, bins=1000)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency')
    plt.title('Histogram of processing times')
    plt.savefig('output.3.3.png')

def main():
    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
    rez = change()
    histogram(rez)

if __name__ == "__main__":
    main()