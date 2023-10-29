import sys
x,y,z = map(int,sys.stdin.readline().split())

if x>y:
    if y>z:
        large = x
        meddle = y
        small =z
    else:
        small = y
        if x>z:
            large = x
            meddle = z
        else:
            large = z
            meddle = x
else:
      if y<z:
            large = z
            meddle = y
            small = x
      else:
            large = y
            if x>z:
                meddle = x
                small = z
            else:
                meddle = z
                small = x
print(large,meddle,small)
