import matplotlib.pyplot as plt
labels = ['Category A', 'Category B', 'Category C']
sizes = [30, 45, 25]
colors = ['skyblue', 'lightpink', 'lightyellow']  
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()



