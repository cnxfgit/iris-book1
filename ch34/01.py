import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a0 = 1
n = 10
d = 2
a_array = np.arange(a0, a0 + n * d, d)
print("打印等差数列")
print(a_array)

fig = plt.figure(figsize=(8, 8))
plt.scatter(np.arange(n), a_array)
plt.title('Arithmetic Progression')
plt.xlabel('Index, $n$')
plt.ylabel('Value, $a_n$')
plt.show()

x1_array = np.linspace(-3, 3, 301)
x2_array = x1_array
xx1, xx2 = np.meshgrid(x1_array, x2_array)
ff = xx1 * np.exp(-xx1 ** 2 - xx2 ** 2)

fig2 = plt.figure(figsize=(8, 8))
ax = fig2.add_subplot(projection='3d')
ax.plot_wireframe(xx1, xx2, ff, rstride=10, cstride=10)
plt.show()

iris_df = sns.load_dataset('iris')
print('打印鸢尾花数据前5行')
print(iris_df.head())

fig3 = plt.subplots(figsize=(8, 8))
ax = sns.scatterplot(data=iris_df, x="sepal_length",
                     y="sepal_width", hue="species")
ax.set_xlabel('Sepal length (cm)')
ax.set_ylabel('Sepal width (cm)')
ax.set_xticks(np.arange(4, 8 + 1, step=1))
ax.set_yticks(np.arange(1, 5 + 1, step=1))
ax.axis('scaled')
ax.grid(linestyle='--', linewidth=0.25,
        color=[0.7, 0.7, 0.7])
ax.set_xbound(lower=4, upper=8)
ax.set_ybound(lower=1, upper=5)

plt.show()
