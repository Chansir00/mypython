import os
import pandas as pd
import matplotlib.pyplot as plt

# 防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据预览
def dataRead():
    while True:
        fileName = input('请输入要打开的文件名 PRSA_data_2010.1.1-2014.12.31.csv:')
        try:
            # 读入文件
            df = pd.read_csv(fileName, encoding='utf-8')
            # 读取前三行和末两行
            print(df.head(3))
            print(df.tail(2))
            print("任务1执行成功!读取前三行，后两行数据")
            break
        except:
            print("任务1执行失败，文件不存在，重新操作！")


# 数据预处理
def dataPreprocessing():
    while True:
        fileName = input('请输入要打开的文件名 PRSA_data_2010.1.1-2014.12.31.csv：')
        try:
            df = pd.read_csv(fileName)
            # 丢弃废弃值
            df = df.dropna()
            # 删除指定列
            df = df.drop(['DEWP', 'TEMP', 'PRES', 'cbwd',
                         'Iws', 'Is', 'Ir'], axis=1)
            # 保存文件
            df.to_csv('pm25_data_2010.1.1-2014.12.31.csv', index=False)
            print("任务2执行成功，处理后的数据保存到'pm25_data_2010.1.1-2014.12.31.csv'文件")
            break
        except:
            print('任务2执行失败，文件不存在，重新操作！')
# 数据筛选


def dateScreening():
    while True:
        fileName = input('请输入要打开的文件名 pm25_data_2010.1.1-2014.12.31.csv：')
        try:
            df = pd.read_csv(fileName)
            # 选择PM2.5>300的列
            hazardous_date = df[df['pm2.5'] > 300]
            # 存至新文件
            hazardous_date.to_csv('pm25_hazardous_data_2010.1.1-2014.12.31.txt',
                                    index=False, sep=',')
            print("任务3执行成功，处理后数据保存在'pm25_hazardous_data_2010.1.1-2014.12.31.txt'")
            break
        except:
            print('任务3执行失败，文件不存在，重新操作！')


# 数据转存
def dataConservation():
    while True:
        fileName = input(
            '请输入要打开的文件名 pm25_hazardous_data_2010.1.1-2014.12.31.txt ：')
        try:
            # 文件转存为excel
            hazardous_date = pd.read_csv(fileName)
            hazardous_date.to_excel(
                'pm25_hazardous_data_2010.1.1-2014.12.31.xlsx', index=False)
            print("任务4执行成功，转存为xlsx文件到'pm25_hazardous_data_2010.1.1-2014.12.31.xlsx'")
            break
        except:
            print('任务4执行失败，文件不存在，重新操作！')


# 数据汇总和可视化
def dateDrawing():
    while True:
        fileName = input(
            '请输入要打开的文件名 pm25_hazardous_data_2010.1.1-2014.12.31.xlsx:')
        try:
            hazardous_date = pd.read_excel(fileName)
            # 选择month列计算出现的次数
            month_count = hazardous_date['month'].value_counts()
            print('出现最多的月为{}月，共出现{}次'.format(
                month_count.index[0], month_count.values[0]))
            # 选择day列计算出现的次数
            day_count = hazardous_date['day'].value_counts()
            print('出现最多的天为{}号，共出现{}次'.format(
                day_count.index[0], day_count.values[0]))
            # 选择hour列计算出现的次数
            hour_count = hazardous_date['hour'].value_counts()
            print('出现最多的小时为{}点，共出现{}次'.format(
                hour_count.index[0], hour_count.values[0]))
            # 月份柱状图
            plt.bar(month_count.index, month_count.values,
                    color=['red', 'green', 'blue'])
            plt.title('PM2.5 Hazardous Month Count')
            plt.xlabel('Month')
            plt.ylabel('count')
            plt.legend('n')
            plt.savefig('pm25_hazardous_month.png', dpi=400)
            plt.show()
            # 日期柱状图
            plt.bar(day_count.index, day_count.values,
                    color=['red', 'green', 'blue'])
            plt.title('PM2.5 Hazardous Day Count')
            plt.xlabel('Day')
            plt.ylabel('count')
            plt.legend('n')
            plt.savefig('pm25_hazardous_day.png', dpi=400)
            plt.show()
            # 小时柱状图
            plt.bar(hour_count.index, hour_count.values,
                    color=['red', 'green', 'blue'])
            plt.title('PM2.5 Hazardous Hour Count')
            plt.xlabel('Hour')
            plt.ylabel('count')
            plt.legend('n')
            plt.savefig('pm25_hazardous_hour.png', dpi=400)
            plt.show()
            break
        except:
            print('任务5执行失败，文件不存在，重新操作！')


def menu():
    print('【任务选择】\n'
          '|***---------2010-2014 年北京市 PM2.5 数据分析-----------***|\n'
          '|0、退出。\n'
          '|1、数据前三行后两行读取\n'
          '|2、数据缺失值丢弃，删除特定列处理。\n'
          '|3、数据按pm2.5进行筛选\n'
          '|4、数据转存。\n'
          '|5、数据汇总处理与可视化。\n'
          '||*******************************************************||')
    

# 打印菜单
def task():
    while True:
        menu()  # 打印菜单
        num = input("请输入任务选项：")  # 进行任务选择
        if num == '1':
            dataRead()
        elif num == '2':
            dataPreprocessing()
        elif num == '3':
            if os.path.exists('pm25_data_2010.1.1-2014.12.31.csv'):  # 判断文件是否存在，不存在将提示执行前部操作
                dateScreening()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('pm25_hazardous_data_2010.1.1-2014.12.31.txt'):
                dataConservation()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('pm25_hazardous_data_2010.1.1-2014.12.31.xlsx'):
                dateDrawing()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '0':
            print('程序结束！')
            break  # 结束程序出口
        else:
            print('输入选项有误')
        input("回车显示菜单")


# 主函数
if __name__ == '__main__':
    task()
