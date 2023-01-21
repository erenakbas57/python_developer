import matplotlib.pyplot as plt
import numpy as np

"""örnek 1"""

# x = [1,2,3,4]
# y = [1,4,9,16]
# plt.plot(x,y,"o--g")
# plt.axis([0,5,0,17]) # [x min,x max,y min,y max]

# plt.title("Sayı Kareleri")
# plt.xlabel("sayı")
# plt.ylabel("karesi")

# plt.show()

"""örnek 2"""

# x = np.linspace(0,2,100)
# plt.plot(x, x, label="linear", color="red")
# plt.plot(x, x**2, label="kare", color="green")
# plt.plot(x, x**3, label="küp", color="blue")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.legend()
# plt.show()

"""örnek 3"""

# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2)

# axs[0].plot(x,x**2, color="red")
# axs[1].plot(x,x+3, color="green")

# plt.show()

"""örnek 4"""

# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2)
# fig.suptitle("grafik başlığı")

# axs[0,0].plot(x,x**2, color="red")
# axs[0,1].plot(x,x**3, color="green")
# axs[1,0].plot(x,x**4, color="blue")
# axs[1,1].plot(x,x**5, color="yellow")


# plt.show()


"""örnek 5 - Dosyadan veri görselleştirme"""

import pandas as pd

df = pd.read_csv("znba.csv")

df = df.drop(["Number"], axis=1).groupby("Team").mean()

df.plot(subplots=True)
plt.legend()
plt.show()