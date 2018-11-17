t = np.arange(0.0, 5.0, 0.1)
a = np.exp(-t) * np.cos(2*np.pi*t)

fig, ax = plt.subplots()
# change here
ax.plot(t, a, )
plt.show()
