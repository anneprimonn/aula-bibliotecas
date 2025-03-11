import matplotlib.pyplot as plt

# a = (1,2,3,4,5)
# b = (1,2,3,4,5)

# plt.plot(a,b)
#plt.plot((1,2,3,4),(1,4,9,16),'ro')  #para deixar com bolinha a cada encontro
#plt.plot((1,2,3,4),(1,4,9,16),'mD:') #estilo
#plt.axis((0,6,0,20)) #limita ate que numero quer no eixo x e y
#plt.grid(True) #grade ao fundo
#plt.subplot(1,2,1) #(linha,coluna,indice)
#plt.plot(a,b)
# plt.ylabel(u'eixo y') #legenda
# plt.xlabel(u'eixo x')
# plt.title('meu grafico') #titulo
# plt.show()


# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.scatter(a,b)
# plt.show()


# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.bar(a,b) #em barras
# plt.show()


# a = (1,2,3,4,5,6)
# b = (2,4,6,8,10,12)
# plt.hist(a,b) #junta as colunas
# plt.show()


a = (10,20,30)
explode = (0.1,0,0) #efeito explosao da fatia
labels = ["HB20","Gol","Fusca"]
plt.pie(a, explode=explode, labels=labels, autopct="%.2f%%", shadow=True) #redondo
plt.title('Grafico')
plt.grid(True)
plt.show()


