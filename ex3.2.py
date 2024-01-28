import json
import timeit


f = open('large-file.json', 'r', encoding='utf-8')
data = json.load(f)

def change_size1k(data):
    i=0
    while(i < 1000):
        for record in data:
            if 'size' in record['payload']:
                record['payload']['size'] = 42
                i += 1
    return 0

def change_size2k(data):
    i=0
    while(i < 2000):
        for record in data:
            if 'size' in record['payload']:
                record['payload']['size'] = 42
                i += 1
    return 0

def change_size5k(data):
    i=0
    while(i < 5000):
        for record in data:
            if 'size' in record['payload']:
                record['payload']['size'] = 42
                i += 1
    return 0

def change_size10k(data):
    i=0
    while(i < 10000):
        for record in data:
            if 'size' in record['payload']:
                record['payload']['size'] = 42
                i += 1
    return 0

def main():
    # Timing the modification of size value 10 times
    time1000 = timeit.timeit(lambda: change_size1k(data), number=100)
    time2000 = timeit.timeit(lambda: change_size2k(data), number=100)
    time5000 = timeit.timeit(lambda: change_size5k(data), number=100)
    time10000 = timeit.timeit(lambda: change_size10k(data), number=100)
    
    timeall = [time1000, time2000, time5000, time10000]

    average_time1k = time1000 / 100
    average_time2k = time2000 / 100
    average_time5k = time5000 / 100
    average_time10k = time10000 / 100

    print(f"Average time to modify size value 1000 times: {average_time1k} seconds")
    print(f"Average time to modify size value 2000 times: {average_time2k} seconds")
    print(f"Average time to modify size value 5000 times: {average_time5k} seconds")
    print(f"Average time to modify size value 10000 times: {average_time10k} seconds")
    
    change_size1k(data)
    change_size2k(data)
    change_size5k(data)
    change_size10k(data)

    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
