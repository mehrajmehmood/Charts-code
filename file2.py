import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
plt.figure(figsize=(8, 5))
plt.plot(categories, values, marker='o', linestyle='-', 
color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Sample Line Graph')
plt.show()
