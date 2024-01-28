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
    listlengths = 1000
    time1000 = []
    time = timeit.repeat(lambda: change_size(listlengths), number=1000)
    time1000.append(time)

    return time1000

def main():
    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    time1000 = change()
    plt.hist(time1000, bins=100, edgecolor='black')
    plt.title('Distribution of Measured Lines')
    plt.xlabel('Processing time of first 1000 records 1000 times')
    plt.ylabel('Y axis')
    plt.savefig('output.3.3.png')
    print(time1000)

if __name__ == "__main__":
    main()

