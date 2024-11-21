import matplotlib.pyplot as plt

x = [ 1,2,3,4,5]
y = [2,4,9,16,25]

plt.plot(x,y,label="crecimento")

plt.title('grafico simples')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend()

plt.show()