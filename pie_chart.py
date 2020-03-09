 import matplotlib.pyplot as plt

labels = ['car emissions', 'trans emissions', 'beef emissions', 'computer emissions', 'light emissions', 'excess power emissions']
sizes = [38.4, 40.6, 20.7, 10.3, 23, 34]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'green', 'pink']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
