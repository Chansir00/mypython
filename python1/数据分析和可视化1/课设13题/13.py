import os
import matplotlib.pyplot as pd
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def dataPreprocessing():
    file_name = input('请输入文件名nino4.long.anom.data.csv:')
    file_name0 = input('请输入要保存的文件名nino4_dropnan.txt:')
    try:
        df = pd.read_csv(file_name)      #读入文件
        #将'Year'列转为datatime类型
        df['Data'] = pd.to_datetime(df['Year'], format='%Y')  
        #创建新的数据框，列名为'Data'和'Nino4'
        result_df = pd.DataFrame(columns=['Data', 'Nino4']) 
        # 遍历df中每一行并获取年份和月份
        for _, row in df.iterrows():   
            year = row['Year']
            for month in range(1, 13):
                nino = row[month]
                if pd.notnull(nino):
                    #则将该值和对应的日期（格式为'年份-月份-01'）存储到result_df中。
                    result_df= pd.concat([result_df, pd.DataFrame({'Data': f'{year}-{month:02d}-01', 'Nino4': nino}, index=[0])], ignore_index=True)     
        #将新的数据存在新文件中 
        result_df.to_csv(file_name0, index=False,  sep=',', float_format='%.2f', date_format='%Y-%m-%d')
        print(f"数据处理成功，已导出到{file_name0}文件。")
    except FileNotFoundError:
        print("文件不存在！")




def dataSelection():
    file_name = input('请输入文件名nino4_dropnan.txt:')
    try:
        data = pd.read_csv(file_name,
                         encoding='utf-8')
        nino4 = data['Nino4']   #选取Nino4这一列
        max_value = nino4.max()   #获取最大值
        min_value = nino4.min()   #获取最小值
        mean_value = nino4.mean()   #获取平均值
        print(f"最大值：{max_value}")
        print(f"最小值：{min_value}")
        print(f"平均值：{mean_value}")
    except FileNotFoundError:
        print("文件不存在！")

def dataGroup():
    file_name = input('请输入文件名nino4_dropnan.txt:')
    file_name0 = input('请输入要保存的文件名nino4_dropnan_result.csv:')
    file_name1 = input('请输入要保存的图像名nino4_pie.png:')
    try:
        data = pd.read_csv(file_name,
                         encoding='utf-8')
        max_value = data['Nino4'].max()
        min_value = data['Nino4'].min()
        # 创建一个包含分类阈值的列表
        category = [min_value, -0.5, 0, 0.5, max_value]       
        labels = ['LaNinaTemp', 'Cold', 'Warm', 'NinoTemp']
        # 用pd.cut方法将列表中的值按阈值分类，并存储道label列中
        data['Label'] = pd.cut(data['Nino4'], bins=category, labels=labels)
        # 保存文件，并指定列头
        data.to_csv(file_name0, index=False, header=['Date', 'Nino4', 'Label'])
        print(f"数据处理成功，已导出到{file_name0}文件。")
        
        # 绘制饼状图
        pie_data = data['Label'].value_counts()   
        plt.figure(dpi=300) 
        #  绘制饼图
        pie_data.plot(kind='pie', autopct='%1.1f%%') 
        # 设置坐标轴属性
        plt.axis('equal')  
        plt.savefig(file_name1)
        plt.close()
        print(f"饼状图已保存为{file_name1}文件。")
    except FileNotFoundError:
        print("文件不存在！")

def dataCalculate():
    file_name = input('请输入文件名nino4_dropnan_result.csv:')
    file_name0 = input('请输入要保存Lanina的文件名LaNinaStartDate.txt:')
    file_name1 = input('请输入要保存Nino的文件名NinoStartDate.txt:')
    try:
        data = pd.read_csv(file_name,
                         encoding='utf-8')
        # 定义几个初始变量
        la_nina_count = 0
        nino_count = 0
        la_nina_list = []
        nino_list = []
        
        # 遍历列表数据，将数据进行分类并计数
        for index, row in data.iterrows():
            if row['Label'] == 'LaNinaTemp':
                la_nina_count += 1
                if la_nina_count == 5:
                    la_nina_list.append(row['Date'])
            else:
                la_nina_count = 0

            if row['Label'] == 'NinoTemp':
                nino_count += 1
                if nino_count == 5:
                    nino_list.append(row['Date'])
            else:
                nino_count = 0
        
        # 保存至新文件中
        with open(file_name0, 'w') as file:
            for date in la_nina_list:
                file.write(str(date) + '\n')
        print(f"LaNina事件开始时间已保存到{file_name0}文件。")
        
        with open(file_name1, 'w') as file:
            for date in nino_list:
                file.write(str(date) + '\n')
        print(f"Nino事件开始时间已保存到{file_name1}文件。")
    except FileNotFoundError:
        print("文件不存在！")




def menu():
    print("【任务选择】\n"
        '一一学生成绩数据分析及可视化系统－－－－－－一一\n'
        ' | 0、退出。                         \n'
        ' |1、数据预处理。                        \n'
        ' | 2、数据选择及导出。                        \n'
        ' | 3、数据分类汇总。                        \n'
        ' |4、数据统计。                        \n'
        '+-----------------------------+')


def task():
    while True:
        menu()
        num = input("请输入任务选项")
        if num == '1':
            dataPreprocessing()
        elif num == '2':
            if os.path.exists('nino4_dropnan.txt'):
                dataSelection()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num =='3':
            if os.path.exists('nino4_dropnan.txt'):
                dataGroup()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num =='4':
            if os.path.exists('nino4_dropnan_result.csv'):
                dataCalculate()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num == '0':
            print('程序结束')
            break
        else:
            print('输入程序有误')
        input('回车显示菜单')

if __name__ == '__main__':
    task()