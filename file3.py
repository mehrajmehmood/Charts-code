import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  
plt.pie(sizes, explode=explode, labels=labels, 
autopct='%1.1f%%', startangle=140)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')

plt.title('Donut Chart with Exploded Slices')
plt.show()