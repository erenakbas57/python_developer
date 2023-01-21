import matplotlib.pyplot as plt

yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]

#Stackplot
"""
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3") 

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,color=["y","r","b"])
plt.legend()
 
plt.show()
"""


""" pasta grafik
goal_types = 'Penaltı','Şut','Serbest Vuruş'
goals = [12,35,7]
colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors, autopct="%1.1f%%", explode=(0.1,0.1,0.1))
plt.show()
"""

"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[15,23,80,34,12],label="BMW")
plt.bar([0.75,1.75,2.75,3.75,4.75],[26,5,42,55,88],label="Audi")

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç bilgileri")

plt.show()
"""

yaslar = [14,34,56,23,83,74,92,13,56,24,28,64,12,42,82,37,45,27,42,44,76,120,75,82,46]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.legend()

plt.show()