k=0
for b1 in ('abcd'):
  for b2 in ('abcd'):
     for b3 in ('abcd'):
         for b4 in ('abcd'):
             for b5 in ('abcd'):
                 for b6 in ('abcd'):
                     for b7 in ('abcd'):
                       for b8 in ('abcd'):
                         for b9 in ('abcd'):
                           for b10 in ('abcd'):
                             for b11 in ('abcd'):
                               for b12 in ('abcd'):
                                 for b13 in ('abcd'):
                                   for b14 in ('abcd'):
                                     for b15 in ('abcd'):
                                       for b16 in ('abcd'):
                                         s=b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16
                                         k1=s.count('a')
                                         k2=s.count('aa')
                                         if k1==0 or k1==4 or k==5 or((k1==3 or k1==2) and k2>0):
                                                                      k=k+1
                                                                      if k==10000:
                                                                          print(0)
                                                                      if k==20000:
                                                                          print(1)
                                                                      if k==50000:
                                                                          print(2)
                                                                      if k==100000:
                                                                          print(3)
                                                                      if k==1000000:
                                                                          print(4)
                                                                      if k==10000000:
                                                                          print(5)
                                                                      if k==20000000:
                                                                          print(6)
                                                                      if k==30000000:
                                                                          print(7)
                                                                      if k==40000000:
                                                                          print(k)
                                                                      if k==50000000:
                                                                          print(k)
                                                                      if k==60000000:
                                                                          print(k)
print(k)
