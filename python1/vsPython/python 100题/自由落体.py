x = 100
height = []
for i in range(0,10):
    high = x / 2**i
    if i != 0:
        height.append(2*high)
    else:
        height.append(high)
print("总共走了{}".format(sum(height)))
print("最后一次{}".format(100/2**10))