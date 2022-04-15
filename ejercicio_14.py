def factores(n):
  vecf=[]
  fac=2
  while fac <= n:
    if not (n % fac != 0):
      vecf.append(fac)
      n/=fac
    else:
      fac+=1
  return vecf

factores(100)
