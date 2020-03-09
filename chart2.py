import matplotlib.pyplot as plt
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
x = [1, 2, 4]
y = [2, 4, 4.5]

plt.plot(x, y)
plt.savefig("plot.png")
