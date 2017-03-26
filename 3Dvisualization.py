from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas

trainArr_data = pandas.read_csv("train.csv")

trainArr = pandas.DataFrame(trainArr_data, columns= ['bone_length', 'rotting_flesh', 'hair_length'])
typeArr = pandas.DataFrame(trainArr_data, columns=['type'])

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

X = trainArr['bone_length']
Y = trainArr['rotting_flesh']
Z = trainArr['hair_length']

ax.scatter(X,Y,Z, c='red', marker='o')
ax.scatter(X,Y,Z, c='green')
ax.scatter(X,Y,Z, c='white')
ax.set_xlabel('x axis')
ax.set_xlabel('y axis')
ax.set_xlabel('z axis')

plt.show()
