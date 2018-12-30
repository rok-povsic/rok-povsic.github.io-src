import matplotlib.pyplot as plt
import matplotlib as mpl

#plt.plot([0, 0], 'k', linewidth=2.0)

plt.axhline(0, color='black')
line = plt.plot([150, 160, 170], [-5, -5, 10], linewidth=2.0)

plt.xlabel('TSLA price on ')
plt.ylabel('Your profit')

ax = plt.gca()
ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('${x:,.0f}'))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('${x:,.0f}'))

plt.show()

