import random 

for i in range(2):
  texto    = input('Digite o número da matrícula: ')
  num      = int(texto)

  random.seed(num)             
  x = int(random.random()*20) + 20  
  y = int(random.random()*80) + 30
  w = int(random.random()*160) + 80
  z = int(random.random()*5) + 1


  print(" x = ",x)
  print(" y = ",y)
  print(" w = ",w)
  print(" z = ",z)