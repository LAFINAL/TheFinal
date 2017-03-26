
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn import svm

data = pandas.read_csv("trainDATA.csv")

trainArr = pandas.DataFrame(data, columns = ['bone_length','rotting_flesh'])
targetArr = pandas.DataFrame(data, columns = ['type'])

h = .01  # step size in the mesh
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(trainArr, targetArr)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(trainArr, targetArr)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(trainArr, targetArr)
lin_svc = svm.LinearSVC(C=C).fit(trainArr, targetArr)

# create a mesh to plot in
x_min, x_max = trainArr.iloc[:, 0].min() , trainArr.iloc[:, 0].max()
y_min, y_max = trainArr.iloc[:, 1].min() , trainArr.iloc[:, 1].max()
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# title for the plots
titles = ['SVC with linear kernel',
          'LinearSVC (linear kernel )',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel']


for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

    # Plot also the training points
    plt.scatter(trainArr.iloc[:, 0], trainArr.iloc[:, 1], c=targetArr, cmap=plt.cm.coolwarm)
    plt.xlabel('bone_length')
    plt.ylabel('rotting_flesh')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()
