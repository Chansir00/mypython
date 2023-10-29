members = {'张三':['人力部',5500],
            '李四':['后勤部',4500],
            '王三':['市场部',6500],
            '赵六':['开发部',8500]
           }
sal_dep = {}
for key in members:
    print('{}的工资是:{}, 部门是{}'.format(key, members[key][1], members[key][0]))
    sal_dep[members[key][1]] = members[key][0]
max_val = max(sal_dep)
max_name = sal_dep[max_val]
print('工资最高的部门是:{},该部门工资是:{}'.format(max_name,max_val))