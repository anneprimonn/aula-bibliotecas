import matplotlib.pyplot as plt

salario = (151,180,200,240,260,300,350,380,415,465,510,540,545,622,648,724,788,880,937,954,998,1039,1045,1100,1212,1300,1320,1412)
ano = (2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025)
plt.plot(salario)

plt.xlabel('Anos') 
plt.ylabel('Salarios')
plt.title('Evolução dos Salários ao Longo dos Anos')
plt.grid(True)
plt.show()