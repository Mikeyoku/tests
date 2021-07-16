import matplotlib.pyplot as plt
import numpy as np
print('Введите x:')
a = float(input())
print('Введите y:')
b = float(input())
print('Введите z:')
c = float(input())

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_aspect("auto")

# Сфера
# Массив для сферы
u, v = np.mgrid[0:10.67:10j, 0:10.67:10j]
# операция для скругления линий
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")


# Линия
x1 = np.linspace(a, 9, 10)
y1 = np.linspace(b, 9, 10)
z1 = np.linspace(c, 9, 10)
ax.plot(x1, y1, z1)
x.tolist()
x1.tolist()

if x.all() != x1.all() and y.all() != y1.all() and z.all() != z1.all():
    print('Коллизий не найдено')
else:
    if x in x1:
        print('x', end=' ')
        print(x.tolist())

    if y in y1:
        print('y', end=' ')
        print(y.tolist())

    if z in z1:
        print('z', end=' ')
        print(z.tolist())


plt.show()
