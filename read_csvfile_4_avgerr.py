#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :read_csvfile_4_avgerr.py
# @Time      :2020/8/11 11:35
# @Author    :herriswang


"""
从csv中读取每天的误差，并绘图
"""

import numpy as np
import pandas as pd
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

# from draw.err import *

Err_File_Path_Prefix = 'output/20190405-{posi}.csv'


def my_print(array):
    for count, line in enumerate(array):
        # print('site {}, pv: {:.2%}, uv: {:.2%}, ctr: {:.2%}, impratio: {:.2%}'.format(count, line[0], line[1], line[3], line[4]))
        print('site {}, {:.2%}, {:.2%}, {:.2%}, {:.2%}'.format(count, line[0], line[1], line[3], line[4]))


def my_plot(sour_list, line_num, name_list):
    for i in range(line_num):
        plt.plot([1, 2, 3, 4, 5], sour_list[i], linewidth=3.0, color='red', label=name_list[i])

    # plt.legend()
    # formatter = FuncFormatter(to_percent)
    # plt.gca().yaxis.set_majot_formatter(matplotlib.ticker.FormatStrFormatter('%.2f%%'))
    # plt.xticks(np.arange(0, 5), fontsize=12)
    plt.xticks([1, 2, 3, 4, 5], fontsize=12) #
    plt.yticks(np.arange(0, 0.25, 0.025), fontsize=12)
    # plt.xlabel('预测天数', fontsize=12)
    plt.xlabel('不同站点', fontsize=12)
    plt.ylabel('误差率', fontsize=12)
    plt.savefig('draw/点击率误差.jpg')
    plt.show()


if __name__ == "__main__":
    run_code = 0

    all_array = []
    for i in range(1, 6, 1):
        path = Err_File_Path_Prefix.format(posi=i)
        all_array.append(pd.read_csv(path).values)
    all_array = np.array(all_array)
    my_print(all_array.mean(axis=0))

    # all_array 维度含义：天数 站点 指标
    # 持续5天，联盟上的点击率误差情况
    # for i in [0, 3, 4]:
    #     print(all_array[:, i, 3])
    #     my_plot([all_array[:, 3, 3], ], 1, ['联盟', ])

    # 在0 3 4天，点击率在各个站点的误差情况
    for i in [0, 3, 4]:
        print(all_array[i, :, 3])
        my_plot([all_array[i, :, 3], ], 1, ['点击率抖动', ])

    # i = 1
    # path = Err_File_Path_Prefix.format(posi=i)
    # my_print(pd.read_csv(path).values)