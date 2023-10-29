import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def dataPreprocessing():
    while True:
        file_name = 'studentScore.csv'
        try:
            df = pd.read_csv(file_name, encoding='cp936')
            df = df.dropna()
            df.to_csv('studentScoreP.csv', encoding='cp936', index=False)
            print(df.tail(2))
            print(df.head(3))
            print("任务一执行成功")
            break
        except:
            print("任务一执行失败")
    


def dataSelection():
    while True:
        file_name = 'studentScore.csv'
        try:
            df = pd.read_csv("studentScoreP.csv",encoding='cp936')
            df_new = df.loc[:, ['姓名', '考号', '班级', '数学', '语文', '英语']]
            try:
                df_new.to_csv('studentScoreP_new.csv',encoding='cp936', index=False)
                df_new = pd.read_csv('studentScoreP_new.csv', encoding='cp936')
                df_newGood = df_new[df_new['语文'] >= 100]
                df_newGood = df_newGood[df_new['语文'] <= 150]
                df_newGood = df_newGood[df_new['数学'] >= 100]
                df_newGood = df_newGood[df_new['数学'] <= 150]
                df_newGood = df_newGood[df_new['英语'] >= 100]
                df_newGood = df_newGood[df_new['英语'] <= 150]
                print("任务2执行成功")
                break
            except:
                    print('文件导出失败')
        except:
            print("任务二执行失败")


def dataGroup():
    while True:
        file_name = 'studentScoreP_new.csv'
        try:
            df_new = pd.read_csv(file_name, encoding='cp936')
            df_new = df_new.loc[:,['班级', '语文', '数学', '英语']]
            df_new_groupby = df_new.groupby(['班级'], as_index=False).mean()
            print(df_new_groupby)
            df_new_groupby.to_csv("studentScoreP_newGroup.txt", encoding='cp936', index=False)
            print("任务三执行成功")
            break
        except:
            print('任务三执行失败')


def dataCalculate():
    while True:
        file_name = 'studentScoreP_new.csv'
        try:
            df_new = pd.read_csv(file_name, encoding='cp936')
            df_new['均值'] = (df_new['语文'] + df_new['数学']+df_new['英语'])/3.0
            df_new.sort_values(by='均值', ascending=False)
            df_new.to_excel('studentScoreP_Mean.xlsx', index=False)
            print('任务4执行成功')
            break
        except:
            print('任务四执行失败')


def dataDescribeVisualization():
    while True:
        fileName = 'studentScoreP_Mean.xlsx'
        df_mean = pd.read_excel(fileName)
        df_mean_describe = df_mean.describe()
        print(type(df_mean_describe))
        print(df_mean_describe)
        maxValue = df_mean_describe.at['max', '均值']
        threeQuartersValue = df_mean_describe.at['75%','均值']
        medianValue = df_mean_describe.at['50%','均值']
        quarterValue = df_mean_describe.at['25%','均值']
        minValue = df_mean_describe.at['min','均值']
        category = [minValue, quarterValue,
            medianValue, threeQuartersValue, maxValue]
        labels = ['Poor', 'Moderate', 'Good', 'Excellent']
        mean_cut = pd.cut(df_mean['均值'], category,
                            right=False, labels=labels)
        print(mean_cut)
        print(type(mean_cut))
        mean_cut_counts = mean_cut.value_counts()
        print(mean_cut_counts)
        print(type(mean_cut_counts))
        # 柱状固
        plt.figure()
        mean_cut_counts.plot(kind='bar', figsize=(8, 12))
        plt.xticks(rotation=0,fontsize=16)
        # plt.yticks(fontsize=16)
        plt.title('平均成绩离散化统计柱状图')
        plt.savefig('studentScoreP Mean bar.png', dpi=400)
        plt.show()
        break
        


def dataVisualization():
    while True:
        fileName = 'studentScoreP_Mean.xlsx'
        try:
            df_mean = pd.read_excel(fileName)
            df_mean = df_mean.loc[:, ['姓名', '均值']]
            plt.figure(figsize=(8, 12))
            plt.plot(df_mean['姓名'], df_mean['均值'], label='均值', color='red')
            plt.xlabel('姓名', fontsize=12)
            xlength = len(df_mean)
            print('xlength=', xlength)
            xticksloc = [i for i in range(xlength)if i % 5 == 0]
            print('xticksloc=', xticksloc)
            xtickslabels = df_mean['姓名'].values[:: 5]
            print(' xtickslabels ', xtickslabels)
            plt.xticks(xticksloc, xtickslabels, rotation=30)
            plt.ylabel('平均分', fontsize=12)
            plt.legend(fontsize='medium')
            plt.title('学生平均成绩', fontsize=16)
            plt.savefig('studentScoreP_Mean.png', dpi=400)
            plt.show()
            print('任务6 执行成功！')
            break
        except:
            print('任务6 执行失败')


def task():
        root = tk.Tk()
        root.geometry('600x600')
        root.title('成绩分析系统')
        bt1 = tk.Button(root,text = '退出')
        bt2 = tk.Button(root,text = '数据读取及预处理。',command=dataPreprocessing)
        bt3 = tk.Button(root,text = '数据选择及导出。',command=dataSelection)
        bt4 = tk.Button(root,text = '数据分类汇总。',command=dataGroup)
        bt5 = tk.Button(root,text = '数据计算及排序。',command=dataCalculate)
        bt6 = tk.Button(root,text = '数据统计。',command= dataDescribeVisualization)
        bt7 = tk.Button(root,text = '数据可视化。',command = dataVisualization)
        bt1.pack()
        bt2.pack()
        bt3.pack()
        bt4.pack()
        bt5.pack()
        bt6.pack()
        bt7.pack()
        root.mainloop()

# def menu():
#     print("【任务选择】\n"
#         '一一学生成绩数据分析及可视化系统－－－－－－一一\n'
#         ' | 0、退出。                         \n'
#         ' |1、数据读取及预处理。                        \n'
#         ' | 2、数据选择及导出。                        \n'
#         ' | 3、数据分类汇总。                        \n'
#         ' |4、数据计算及排序。                        \n'
#         ' |S、数据统计。                        \n'
#         ' |6 、数据可视化。                        \n'
#         '+-----------------------------+')


# def task():
#     while True:
#         menu()
#         num = input("请输入任务选项")
#         if num == '1':
#             dataPreprocessing()
#         elif num == '2':
#             if os.path.exists('studentScoreP.csv'):
#                 dataSelection()
#             else:
#                 print("未能执行当前选项，请执行先前选项")
#         elif num =='3':
#             if os.path.exists('studentScoreP_new.csv'):
#                 dataGroup()
#             else:
#                 print("未能执行当前选项，请执行先前选项")
#         elif num =='4':
#             if os.path.exists('studentScoreP_new.csv'):
#                 dataCalculate()
#             else:
#                 print("未能执行当前选项，请执行先前选项")
#         elif num =='5':
#             if os.path.exists('studentScoreP_Mean.xlsx'):
#                 dataDescribeVisualization()
#             else:
#                 print("未能执行当前选项，请执行先前选项")
#         elif num == '6':
#             if os.path.exists('studentScoreP.csv'):
#                 dataVisualization()
#             else:
#                 print("未能执行当前选项，请执行先前选项")
#         elif num == '0':
#             print('程序结束')
#             break
#         else:
#             print('输入程序有误')
#         input('回车显示菜单')

if __name__ == '__main__':
    task()


