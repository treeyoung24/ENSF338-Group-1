import json
import matplotlib.pyplot as plt

f = open('internetdata.json')
data = json.load(f)

def sort_by_income(data):
    low_income = []
    high_income = []

    for country in data:
        if country['incomeperperson'] is None:
            pass
        elif country['incomeperperson'] < 10000:
            low_income.append(country)
        else:
            high_income.append(country)
    return low_income, high_income

def internet_usage(low_income, high_income):
    low_usage = []
    high_usage = []
    for usage in low_income:
        if usage['internetuserate'] is None:
            pass
        else:
            low_usage.append(usage['internetuserate'])
    for usage in high_income:
        if usage['internetuserate'] is None:
            pass
        else:
            high_usage.append(usage['internetuserate'])
    return low_usage, high_usage

def histogram_low(low_usage):
    plt.figure()
    plt.hist(low_usage, bins=20, edgecolor='black')
    plt.title('Internet Usage in Low Income Countries')
    plt.xlabel('Internet Usage')
    plt.ylabel('Number of Countries')
    plt.savefig('hist1.png')

def histogram_high(high_usage):
    plt.figure()
    plt.hist(high_usage, bins=20, edgecolor='black')
    plt.title('Internet Usage in High Income Countries')
    plt.xlabel('Internet Usage')
    plt.ylabel('Number of Countries')
    plt.savefig('hist2.png')

def main():
    low_income, high_income = sort_by_income(data)
    low_usage, high_usage = internet_usage(low_income, high_income)
    histogram_low(low_usage)
    histogram_high(high_usage)
    

if __name__ == "__main__":
    main()