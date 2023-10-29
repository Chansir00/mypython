pro = [100000,200000,400000,600000,1000000]
sal = [0.1,0.75,0.05,0.03,0.15,0.01]
ward = 0
temp = int(input("请输入利润"))
for i in pro:
    if temp > pro[0]:
        ward += pro[0]*sal[0]
    if temp > pro[1]:
        ward += (temp - pro[0]) * pro[1]
    if temp > pro[2]:
        ward += (temp - pro[1]) * pro[2]
    if temp > pro[3]:
        ward += (temp - pro[2]) * pro[3]
    if temp > pro[4]:
        ward += (temp - pro[3]) * pro[4]
print(ward)

