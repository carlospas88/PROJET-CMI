import time
def tempsExecution(f):
  debut = time.time()
  f() #appelle de la fonction
  print(time.time() - debut) # donne le temps en secondes
