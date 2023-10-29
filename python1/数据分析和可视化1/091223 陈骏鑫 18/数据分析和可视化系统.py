from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image

# 防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 人工输入框读取文件名函数

def get_file1(file):
    return str(file)


# 数据预览模块
def dataProcessing():

    # 数据处理函数
    def get_file():
        file_name = get_file1(en.get())
        window = tk.Toplevel()
        window.title('数据预览')
        window.geometry('500x500')
        try:
            # 读入文件
            df = pd.read_csv(file_name, encoding='utf-8')
            # 丢失缺失值
            df = df.dropna()
            # 保存文件
            df.to_csv('18.tmdb_5000_movies1.csv',
                      encoding='utf-8', index=False)
            # 提示信息
            label1 = tk.Label(window, text='前三列', bg='white')
            mess1 = tk.Message(window, text=df.head(3), anchor='n')
            label2 = tk.Label(window, text='末三列', bg='white')
            mess2 = tk.Message(window, text=df.tail(3), anchor='center')
            mess3 = tk.Label(window, text='任务执行完毕!',
                             anchor='s', bg='red', font=10)

            label1.pack()
            mess1.pack()
            label2.pack()
            mess2.pack()
            mess3.pack()
            # 异常处理
        except FileNotFoundError:
            label4 = tk.Message(window, text='任务执行失败', bg='red', font=20)
            label4.pack()

        window.mainloop()
    # 函数主界面
    window = tk.Toplevel()
    window.title('文件处理')
    window.geometry('400x400')
    # 提示人工输入文件名
    lab = tk.Label(window, text='请输入文件\n18.tmdb_5000_movies.csv：',
                   anchor='s', bg='red', font=10)
    lab.pack()
    # 输入框
    en = ttk.Entry(window, width=20, style="Custom.TButton")
    en.pack(side=tk.TOP, padx=10, pady=15)

    button = ttk.Button(window, text="确定", command=get_file)
    button.pack()


# 数据筛选模块
def dataSelection():

    # 数据处理函数
    def get_file():
        file_name = get_file1(en.get())
        window = tk.Toplevel()
        window.title('数据筛选')
        window.geometry('500x500')
        try:
            df = pd.read_csv(file_name, encoding='utf-8')
            # 选中列名
            df_new = df.loc[:, ['id', 'release_date',
                                'title', 'vote_average', 'vote_count']]
            try:
                # 存至新文件
                df_new.to_csv('18.tmdb_5000_movies_vote.csv',
                              encoding='utf-8', index=False)
                df_new = pd.read_csv(
                    '18.tmdb_5000_movies_vote.csv', encoding='utf-8')
                lable = tk.Label(
                    window, text='任务执行成功！\n 已将筛选后的数据保存至\n18.tmdb_5000_movies_vote.csv', font=20, bg='white')
                lable.pack()
            except FileNotFoundError:
                lable2 = tk.Label(window, text='文件导出失败！', font=20, bg='red')
                lable2.pack()
        except FileNotFoundError:
            lable3 = tk.Label(window, text='任务执行失败！', font=20, bg='red')
            lable3.pack()
    # 函数主界面
    window = tk.Toplevel()
    window.title('文件处理')
    window.geometry('400x400')

    lab = tk.Label(window, text='请输入文件\n18.tmdb_5000_movies1.csv：',
                   anchor='s', bg='red', font=10)
    lab.pack()

    en = ttk.Entry(window, width=20, style="Custom.TButton")
    en.pack(side=tk.TOP, padx=10, pady=15)

    button = ttk.Button(window, text="确定", command=get_file)
    button.pack()
    window.mainloop


# 数据排序模块
def datarange():

    # 数据处理函数
    def get_file():
        file_name = get_file1(en.get())
        window = tk.Toplevel()
        window.title('评分排序')
        window.geometry('500x500')
        try:
            df = pd.read_csv(file_name, encoding='utf-8')
            # 根据“vote_average”排序
            df = df.sort_values(by='vote_average', ascending=False)
            df.to_csv('18.tmdb_5000_movies_vote_descending.txt', index=False)
            label = tk.Label(
                window, text='任务执行成功！\n已将排序结果保存至\n18.tmdb_5000_movies_vote_descending.txt', bg='white', font=20)
            label.pack()
        except FileNotFoundError:
            label = tk.Label(window, text='任务执行失败', bg='red', font=20)
            label.pack()
    # 函数主界面
    window = tk.Toplevel()
    window.title('文件处理')
    window.geometry('400x400')

    lab = tk.Label(window, text='请输入文件\n18.tmdb_5000_movies_vote.csv：',
                   anchor='s', bg='red', font=10)
    lab.pack()

    en = ttk.Entry(window, width=20, style="Custom.TButton")
    en.pack(side=tk.TOP, padx=10, pady=15)

    button = ttk.Button(window, text="确定", command=get_file)
    button.pack()
    window.mainloop()


# 数据计算模块
def datacalculate():
    # 数据处理函数
    def get_file():
        file_name = get_file1(en.get())
        window = tk.Toplevel()
        window.title('数据计算')
        window.geometry('500x500')
        try:
            df = pd.read_csv(
                file_name, encoding='utf-8')
            # 计算最大值、最小值、平均值
            maxvalue = df['vote_average'].max()
            minValue = df['vote_average'].min()
            meanValue = df['vote_average'].mean()
            messege = [('最大值：', maxvalue), ('最小值:', minValue),
                       ('平均值:', meanValue)]
            # for循环语句逐个输出为标签
            for i, (mes, val) in enumerate(messege):
                label = tk.Label(window, text=mes, font=20)
                label1 = tk.Label(window, text=val, font=20)
                label.grid(row=0+i*2, column=1, sticky='N')
                label1.grid(row=0+i*2, column=2, sticky='N')
                label4 = tk.Label(
                    window, text="任务执行成功！\n成功统计最大值。最小值，平均值", bg='white', font=20)
                label4.grid(row=8, column=2, sticky='N')
        except FileNotFoundError:
            lable1 = tk.Label(window, text='任务执行失败', font=20, bg='red')
            lable1.pack()

    # 函数主界面
    window = tk.Toplevel()
    window.title('文件处理')
    window.geometry('400x400')

    lab = tk.Label(window, text='请输入文件\n18.tmdb_5000_movies_vote_descending.txt：',
                   anchor='s', bg='red', font=10)
    lab.pack()

    en = ttk.Entry(window, width=20, style="Custom.TButton")
    en.pack(side=tk.TOP, padx=10, pady=15)

    button = ttk.Button(window, text="确定", command=get_file)
    button.pack()
    window.mainloop()


# 数据离散化可视化模块
def dataDescribeVisualization():
    # 数据处理函数
    def get_file():
        file_name = get_file1(en.get())
        window = tk.Toplevel()
        window.title('离散化数据分析')
        window.geometry('500x500')
        try:
            df_mean = pd.read_csv(file_name)
            # 调用discribe方法统计信息
            df_mean_describe = df_mean.describe()
            # print(type(df_mean_describe))
            # print(df_mean_describe)
            # 获取“vote_average”中最大值和最小值
            maxValue = df_mean_describe.at['max', 'vote_average']
            minValue = df_mean_describe.at['min', 'vote_average']
            # 创建一个阈值列表
            category = sorted([minValue, 5,
                        7, 9, maxValue])
            labels = ['bad', 'ok', 'Good', 'Excellent']
            # 根据不同值划分等级，并存在“vote_rank”当中
            df_mean['vote_rank'] = pd.cut(df_mean['vote_average'], category,
                                          right=False, labels=labels)
            # 统计出现次数
            mean_cut_counts = df_mean['vote_rank'].value_counts()
            label2 = tk.Label(window,text='描述性信息',font=20,bg='white')
            label2.pack()
            label0 = tk.Label(window,text=df_mean_describe)
            label0.pack()
            label01 = tk.Label(window,text='数据统计',font=20,bg='white')
            label01.pack()
            print(type(df_mean))
            label3 = tk.Label(window, text=mean_cut_counts, font=20)
            label3.pack()
            label1 = tk.Label(window, text='任务执行完毕\n已将结果保存至\n18.tmdb_5000_movies_vote_descending_result.csv', font=20,bg='red')
            label1.pack()
            print(type(mean_cut_counts))
            df_mean.to_csv(
                '18.tmdb_5000_movies_vote_descending_result.csv', index=False)

        # 绘制饼状图
            plt.figure()
            mean_cut_counts.plot(kind='pie', figsize=(12, 8))

            # 标题、x坐标轴称、y坐标轴称
            plt.title('电影评分离散化饼状图')
            plt.xlabel('评分区间')
            plt.ylabel('电影数量')
            plt.savefig(
                '18.tmdb_5000_movies_vote_descending_result_pie.png', dpi=400)
            plt.show()

        except FileNotFoundError:
            lable1 = tk.Label(window, text='任务执行失败', font=20, bg='red')
            lable1.pack()

    # 主函数界面
    window = tk.Toplevel()
    window.title('文件处理')
    window.geometry('400x400')

    lab = tk.Label(window, text='请输入文件\n18.tmdb_5000_movies_vote_descending.txt：',
                   anchor='s', bg='red', font=10)
    lab.pack()

    en = ttk.Entry(window, width=20, style="Custom.TButton")
    en.pack(side=tk.TOP, padx=10, pady=15)

    button = ttk.Button(window, text="确定", command=get_file)
    button.pack()
    window.mainloop()


# 作品信息模块
def workinfo():
    window = tk.Toplevel()
    window.title('作品信息')
    window.geometry('500x500')
    info = ["课设题目：2000-2015 年电影评分数据分析", "姓名：陈骏鑫", "班级：091223",
            "学号：20221002329", "指导老师：刘远兴", "时间：2023/5/19"]
    for i in info:
        label = tk.Label(window, text=i, font=20, bg='white')
        label.pack(side=tk.TOP, padx=10, pady=15)
    window.mainloop()


def main():
    # 主菜单
    root = tk.Tk()
    root.title("数据分析与可视化系统")
    root.geometry('700x525')
    # 设置标签样式
    style = ttk.Style()
    style.configure("Custom.TButton", padding=6, relief="flat",
                    background="#4CAF50", foreground="black")
    # 背景图片
    Photo = tk.PhotoImage(file='giphy.gif')
    label = tk.Label(root, image=Photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    # canva = tk.Canvas(root)
    # canva.create_image(file_name = 'giphy.gif')
    # canva.pack()

    label0 = ttk.Label(root, text='数据分析与可视化系统', style="Custom.TButton",
                       background='blue', foreground='blue')
    label0.pack(side=tk.TOP,  padx=10, pady=15)
    file_name = '18.tmdb_5000_movies.csv'
    # en = ttk.Entry(root, width=10, style="Custom.TButton")
    # en.pack(side=tk.TOP, padx=10, pady=15)
    # button = ttk.Button(root, text="确定", command=get_file)
    # button.pack()

    # 按钮菜单
    buttons = [
        ("数据预览", dataProcessing),
        ("数据筛选", dataSelection),
        ("评分排序", datarange),
        ("数据计算", datacalculate),
        ("数据离散化统计", dataDescribeVisualization),
        ("退出", exit)
    ]
    for i, (text, command) in enumerate(buttons):
        button = ttk.Button(root, text=text, command=command,
                            width=50, style="Custom.TButton")
        button.pack(side=tk.TOP, padx=10, pady=10)
    button1 = tk.Button(root, text='作品信息', command=workinfo, bg='pink')
    button1.pack(side=tk.TOP, anchor=tk.NW)
    root.mainloop()


# 主函数
if __name__ == '__main__':
    main()
