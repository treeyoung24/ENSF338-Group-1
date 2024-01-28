import json

with open('large-file.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def change_size(data):
    for record in data:
        if 'size' in record:
            record['size'] = 42
    return 0

def main():
    change_size(data)
    data.reverse()
    with open('output.2.3.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()