import gc
gc.collect()
a=gc.mem_free()
import ti_system
gc.collect()
b=gc.mem_free()
import ti_graphics
gc.collect()
c=gc.mem_free()
s=""
for i in range(20):
  s+="def f%d(a,b):\n c=a*b+%d\n return [c,a-b]\n"%(i,i)
g={}
gc.collect()
d=gc.mem_free()
exec(s,g)
s=0
gc.collect()
e=gc.mem_free()
lo=0
hi=e
while hi-lo>64:
  m=(lo+hi)//2
  try:
    x=bytearray(m)
    lo=m
  except MemoryError:
    hi=m
  x=0
  gc.collect()
print("EASY CHEM MEMORY TEST")
print("A start",a)
print("B system",a-b)
print("C graphics",b-c)
print("D code",d-e)
print("E biggest",lo)
try:
  import sys
  print("F",sys.implementation[1])
except:
  print("F ?")
