temp = input("请输入字符串：")
if 'm' in temp:
    temp.replace('m','male')
elif 'f' in temp:
    temp.replace('f','female')
temp.replace(temp[-11:],temp[:11:-1])
print(temp)
