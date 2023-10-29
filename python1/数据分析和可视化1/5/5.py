import matplotlib.pyplot as pd
import pandas as pd
import matplotlib.pyplot as plt
import os

# 防止绘图时中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def dataPreprocessing():
    while True:
        file_name = input('请输入文件名5.pollution_us_5city_2006_2010_CO.csv:')
        try:
            df = pd.read_csv(file_name,encoding='utf-8')
            # 丢弃废弃值
            df.dropna()
            print("前五行")
            # 前五行
            print(df.head(5))
            # 末两行
            print('末两行')
            print(df.tail(2))
            break
        except:
            print("程序执行失败")


def dataSelection():
    while True:
        try:
            file_name = input('请输入文件名5.pollution_us_5city_2006_2010_CO.csv：')
            file_name0 = input('请输入要保存的文件名pollution_us_NewYork_2006_2010_COMean.txt:')
            df = pd.read_csv(file_name,encoding='utf-8')
            # 选择‘City’=20的列以及其他列
            df_new = df.loc[df['City']=='New York',['Date Local','CO Mean','CO 1st Max Hour']]
            df_new.to_csv(file_name0,encoding='utf-8',index=None)
            print('任务执行成功！')
            break
        except:
            print('任务执行失败')


def dataplot():
    while True:
        try:
            file_name = input('请输入文件名pollution_us_NewYork_2006_2010_COMean.txt:')
            df = pd.read_csv(file_name,encoding='utf-8')
            # 行选择 CO 1st Max Hour=20 的行。
            df_new = df[df['CO 1st Max Hour'] == 20]
            df_new['Date Local'] = pd.to_datetime(df_new['Date Local'])
            # 将 Date Local 列的数据类型转换为日期类型，以便后续按年份进行分组
            df_grouped = df_new.groupby(df_new['Date Local'].dt.year)['CO Mean'].mean()
            # plt.figure(figsize=('10x10'))
            #绘制折线图
            plt.title('CO 1st Max Hour',fontsize = 16)
            plt.xlabel('Date Local')
            plt.ylabel('CO Mean')
            plt.plot(df_grouped.index, df_grouped.values, color='red', label='CO Mean')
            # x轴用年份表示
            plt.xticks(df_grouped.index, rotation=45)
            # 设置图例
            plt.legend()
            plt.show()
            print('任务执行成功！')
            break
        except:
            print('任务执行失败')


def datarank():
    while True:
        try:
            file_name = input('请输入文件名5.pollution_us_5city_2006_2010_CO.csv：')
            file_name0 = input('请输入要保存的文件名pollution_us_NewYork_2006_2010_COAQI.xlsx：')
            df = pd.read_csv(file_name,encoding='utf-8')
            # 筛选 City == 'New York'，并选择 Date Local 和 CO AQI 两列。
            df_new = df.loc[df['City']=='New York',['Date Local','CO AQI']]
            # 按照 CO AQI 列的降序进行排序。
            df_new = df_new.sort_values(by='CO AQI',ascending= False)
            df_new.to_excel(file_name0,index=False)
            print('任务执行成功')
            break
        except:
            print('任务执行失败')


def dataDescribeVisualization():
    while True:
        try:
            file_name = input('请输入文件名pollution_us_NewYork_2006_2010_COAQI.xlsx：')
            df = pd.read_excel(file_name)
            # 将 CO AQI 列离散化
            category = [0, 5, 10, 15, 20, 25, 30]
            labels = ['Good', 'Moderate', 'SubUnhealthy', 'Unhealthy', 'VeryUnhealthy', 'Hazardous']
            df['CO AQI Category'] = pd.cut(df['CO AQI'], bins=category, labels=labels)
            # 统计每个离散化类别的数量
            counts = df['CO AQI Category'].value_counts()
            # 绘制饼状图
            plt.figure(figsize=(6,8))
            plt.pie(counts.values, labels=None)
            plt.title('dataDescribeVisualization')
            # 添加图例，防止文字重叠
            plt.legend(counts.index, loc=2)
            plt.savefig('CO_AQI_pie.png',dpi = 300)
            plt.show()
            print('任务执行成功')
            break
        except:
            print('任务执行失败')


def menu():
    print("【任务选择】\n"
        '一一美国五个著名城市空气中一氧化碳污染情况分析及可视化系统－－－－－－一一\n'
        ' |0、退出。                         \n'
        ' |1、数据预处理及预览。                        \n'
        ' |2、数据选择及导出。                        \n'
        ' |3、数据折线图。                        \n'
        ' |4、数据排序及导出。                        \n'
        ' |5、数据分析和可视化                   \n'
        '+-----------------------------+')


def task():
    while True:
        menu()
        num = input("请输入任务选项")
        if num == '1':
            dataPreprocessing()
        elif num == '2':
            if os.path.exists('5.pollution_us_5city_2006_2010_CO.csv'):
                dataSelection()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num =='3':
            if os.path.exists('pollution_us_NewYork_2006_2010_COMean.txt'):
                dataplot()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num =='4':
            if os.path.exists('pollution_us_NewYork_2006_2010_COMean.txt'):
                datarank()
            else:
                print("未能执行当前选项，请执行先前选项")
        elif num == '5':
            if os.path.exists('pollution_us_NewYork_2006_2010_COAQI.xlsx'):
                dataDescribeVisualization()
            else:
                print('未能执行当前选项，请执行之前的选项')
        elif num == '0':
            print('程序结束')
            break
        else:
            print('输入程序有误')
        input('回车显示菜单')

if __name__ == '__main__':
    task()
