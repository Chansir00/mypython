sum_grade_point = 0
sum_credit = 0
print("注：一行只能填一科成绩，成绩和学分间用英文逗号隔开，输入一科后回车继续输入")
while True:
    a = input("输入成绩和学分（逗号(,)隔开，回车换行,如需结束请回车: ")
    if not a:
        break

    try:
        grade, credit = map(float, a.split(","))
        sum_grade_point += grade * credit
        sum_credit += credit
    except ValueError:
        print("输入错误.")

if sum_credit == 0:
    print("未检测到输入.")
else:
    weighted_average = sum_grade_point / sum_credit
    print("你的成绩是: {:.2f}".format(weighted_average))

input("任意键结束运行")