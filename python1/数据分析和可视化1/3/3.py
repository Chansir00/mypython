import os
from matplotlib import dates
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 任务一
def dataRead():
    while True:
        file = input('请输入要打开的文件名 pollution_us_5city_2006_2010_O3.csv:')
        try:
            # 读入文件
            df = pd.read_csv(file, encoding='utf-8')
            # 读取前五行和末两行
            print(df.head(5))
            print(df.tail(2))
            print("任务1执行成功!读取前五行，后两行数据")
            break
        except:
            print("任务1执行失败，文件不存在，重新操作！")
# 任务二
def dataPreprocessing():
    while True:
        file = input('请输入要打开的文件名 pollution_us_5city_2006_2010_O3.csv：')
        try:
            df = pd.read_csv(file)
            # 删除指定列
            df = df[(df['Date Local'] >= '2007/01/01')&(df['Date Local'] <= '2009/12/31')]
            # 保存文件
            df.to_csv('pollution_us_5city_2007_2009_O3.csv', index=False)
            print("任务2执行成功，处理后的数据保存到'pollution_us_5city_2007_2009_O3.csv'文件")
            break
        except:
            print('任务2执行失败，文件不存在，重新操作！')
# 任务三
def dateGroup():
    while True:
        file = input('请输入要打开的文件名pollution_us_5city_2007_2009_O3.csv：')
        # 输入城市选择
        temp = input('请输入城市(数字）：\n1.Houston\n2.NewYork\n3.Washington\n')
        try:
            df = pd.read_csv(file)
            # 判断选择的不同的城市，存入对应文件
            if temp == '1':
                df_new = df[df['City'] == 'Houston']
                filename = input('请输入要保存的文件名pollution_us_Houston_2007_2009_O3.txt：')
                try:
                    df_new.to_csv(filename,index=False, sep=',')
                    print("任务执行成功!")
                except:
                    print("保存失败")
                break
            elif temp == '2':
                df_new = df[df['City'] == 'New York']
                filename = input('请输入要保存的文件名pollution_us_NewYork_2007_2009_O3.txt：')
                try:
                    df_new.to_csv(filename,index=False, sep=',')
                    print("任务执行成功!")
                except:
                    print("保存失败")
                break
            elif temp == '3':
                df_new = df[df['City'] == 'Washington']
                filename = input('请输入要保存的文件名pollution_us_Washington_2007_2009_O3.txt：')
                try:
                    df_new.to_csv(filename,index=False, sep=',')
                    print("任务执行成功!")
                except:
                    print("保存失败")
                break
            else:
                print('输入有误')
        except:
            print('任务3执行失败，文件不存在，重新操作！')
# 任务四
def dataConservation():
    while True:
        file = input(
            '请输入要打开的文件名pollution_us_Houston_2007_2009_O3.txt\npollution_us_NewYork_2007_2009_O3.txt\npollution_us_Washington_2007_2009_O3.txt:'
            )
        try:
            # 根据输入的文件保存对应的新文件
            if file == 'pollution_us_Houston_2007_2009_O3.txt':
                df = pd.read_csv(file)
                try:
                    df.to_excel('pollution_us_Houston_2007_2009_O3.xlsx')
                    print("任务执行成功!")
                except:
                    print('任务执行失败')
                break
            elif file == 'pollution_us_NewYork_2007_2009_O3.txt':
                df = pd.read_csv(file)
                try:
                    df.to_excel('pollution_us_NewYork_2007_2009_O3.xlsx')
                    print("任务执行成功!")
                except:
                    print('任务执行失败')
                break
            elif file == 'pollution_us_Washington_2007_2009_O3.txt':
                df = pd.read_csv(file)
                try:
                    df.to_excel('pollution_us_Washington_2007_2009_O3.xlsx')
                    print("任务执行成功!")
                except:
                    print('任务执行失败')
                break
            else:
                print('输入有误')
            # 文件转存为excel
            print("任务4执行成功")
        except:
            print('任务4执行失败，文件不存在，重新操作！')
# 任务五
def dateVisialization():
    while True:
        choice = input('请输入要对比的数据O3Mean\O3AQI\O31stMaxHour：')
        try:
            # 读取Excel文件
            houston = pd.read_excel('pollution_us_Houston_2007_2009_O3.xlsx')
            new_york = pd.read_excel('pollution_us_NewYork_2007_2009_O3.xlsx')
            washington = pd.read_excel('pollution_us_Washington_2007_2009_O3.xlsx')
            if choice == 'O3Mean':
            # 可视化O3 Mean
            # 绘制三条折线
                plt.plot(houston['Date Local'], houston['O3 Mean'], color='red', label='Houston')
                plt.plot(new_york['Date Local'], new_york['O3 Mean'], color='green', label='New York')
                plt.plot(washington['Date Local'], washington['O3 Mean'], color='blue', label='Washington')
                # 设置图例
                plt.legend()
                # X轴和Y轴标签
                plt.xlabel('Year')
                plt.ylabel('O3 Mean')
                # 保存图片
                plt.savefig('Houston_NewYork_Washington_2007_2009_O3Mean.png')
                plt.show()
                print("任务执行成功!")
            elif choice == 'O3AQI':
            # 可视化O3 AQI
                plt.plot(houston['Date Local'], houston['O3 AQI'], color='red', label='Houston')
                plt.plot(new_york['Date Local'], new_york['O3 AQI'], color='green', label='New York')
                plt.plot(washington['Date Local'], washington['O3 AQI'], color='blue', label='Washington')
                plt.legend()
                plt.xlabel('Year')
                plt.ylabel('O3 AQI')
                plt.savefig('Houston_NewYork_Washington_2007_2009_O3AQI.png')
                plt.show()
                print("任务执行成功!")
            elif choice == 'O31stMaxHour':
            # 可视化O3 1st Max Hour
                plt.figure(figsize=(8,8))
                plt.plot(houston['Date Local'], houston['O3 1st Max Hour'], color='red', label='Houston')
                plt.plot(new_york['Date Local'], new_york['O3 1st Max Hour'], color='green', label='New York')
                plt.plot(washington['Date Local'], washington['O3 1st Max Hour'], color='blue', label='Washington')
                plt.legend()
                plt.xlabel('Year')
                plt.ylabel('O3 1st Max Hour')
                plt.savefig('Houston_NewYork_Washington_2007_2009_O31stMaxHour.png')
                plt.show()
                print("任务执行成功!")
                break
            else:
                print('输入有误，请重新输入：')
        except:
            print('任务5执行失败，文件不存在，重新操作！')

# 菜单
def menu():
    print('【任务选择】\n'
          '|***---------2006_2010年美国五个著名城市纽约O3数据分析-----------***|\n'
          '|0、退出。\n'
          '|1、数据预览\n'
          '|2、数据特定年份导出。\n'
          '|3、数据特定城市筛选\n'
          '|4、数据转存。\n'
          '|5、数据可视化对比。\n'
          '||*******************************************************||')
# 功能函数
def task():
    while True:
        menu()  # 打印菜单
        num = input("请输入任务选项：")  # 进行任务选择
        if num == '1':
            dataRead()
        elif num == '2':
            dataPreprocessing()
        elif num == '3':
            if os.path.exists('pollution_us_5city_2007_2009_O3.csv'):  # 判断文件是否存在，不存在将提示执行前部操作
                dateGroup()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '4':
            if os.path.exists('pollution_us_Houston_2007_2009_O3.txt'):
                dataConservation()
            else:
                print('未能执行当前选项，请先执行前面的选项！')
        elif num == '5':
            if os.path.exists('pollution_us_Houston_2007_2009_O3.xlsx'):
                dateVisialization()
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