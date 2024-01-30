import json
import timeit


f = open('large-file.json', 'r', encoding='utf-8')
data = json.load(f)

def change_size(data):
    for record in data:
        if 'size' in record:
            record['size'] = 42
    return 0

def main():
    # Timing the modification of size value 10 times
    time = timeit.timeit(lambda: change_size(data), number=10)
    average_time = time / 10
    print(f"Average time to modify size value 10 times: {average_time} seconds")
    change_size(data)
    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()