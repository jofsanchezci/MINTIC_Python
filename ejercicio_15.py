def gdc_1(m,n):
  vecm=set([])
  vecn=set([])
  for i in range(1,m+1):
    if m%i==0:
      vecm.add(i)
  for j in range(1,n+1):
    if n%j==0:
      vecn.add(j)
  return max((vecm & vecn))

gdc_1(48,60) 
