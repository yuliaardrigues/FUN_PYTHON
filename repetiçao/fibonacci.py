contador = 0
n = int(input())
f1 = 1 
f2 = 1 
print(f1)
print(f2)
while contador <= n:
  fn = f1 + f2

  print(fn)
  f2 = f1
  f1 = fn 

  contador += 1