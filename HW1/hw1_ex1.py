import numpy as np
import matplotlib.pyplot as plt
f1 = lambda n: n ** np.sqrt(np.log(n))
f2 = lambda n: 7 * n - 2
f3 = lambda n: 100 * np.sqrt(n) + 2 * n ** (0.25) - 100
f4 = lambda n: 2 ** (np.log(n) ** 2)
f5 = lambda n: 2 ** (2 * np.log(n)) + n ** 1.1
f6 = lambda n: 3 ** n
f7 = lambda n: n * np.log(n)

func_list = [f1, f2, f3, f4, f5, f7]
x = np.arange(1, 1e3, 1)

for i, f in enumerate(func_list):
    y = np.log10(f(x))
    plt.plot(x, y, label='f{0}'.format(i + 1))
plt.legend()
plt.show()
import IPython; IPython.embed()
