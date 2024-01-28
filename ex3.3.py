import matplotlib.pyplot as plt

plt.hist(time1000, bins=20, edgecolor='black')
plt.title('Internet Usage in Low Income Countries')
plt.xlabel('Internet Usage')
plt.ylabel('Number of Countries')
plt.savefig('hist1.png')