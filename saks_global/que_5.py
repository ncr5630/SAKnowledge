# need to install  Matplotlib library to plotting the graph 
import matplotlib.pyplot as plt
y = [10, 20, 25, 30]
x = [1, 2, 3, 4]
# Assign color for diagram
plt.plot(x, y, color='orange')
# Data X lable
plt.xlabel('X Data')
# Data Y lable
plt.ylabel('Y Data')
# title of the graph
plt.title('Linear diagram')
# display gui plotting graph with above data
plt.show()