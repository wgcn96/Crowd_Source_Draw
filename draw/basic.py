#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :err.py
# @Time      :2020/8/11 11:33
# @Author    :herriswang


"""
enter for what use from here

"""

import matplotlib.pyplot as plt
import numpy as np


def my_plot(sour_list, line_num, name_list):
    for i in range(line_num):
        plt.plot(sour_list[i], linewidth=3.0, markersize=8, label=name_list[i])

    plt.legend()
    # plt.xticks(np.arange(0, 21), fontsize=12)
    # plt.yticks(np.arange(0, 0.7, 0.1), fontsize=12)
    # plt.xlabel('The number of automatic tags', fontsize=12)
    # plt.ylabel('HR', fontsize=12)
    # plt.savefig('component_HR')
    plt.show()


"""
if __name__ == '__main__':
    TagRec = [0.142, 0.241, 0.303, 0.343, 0.38, 0.406, 0.43, 0.449, 0.476, 0.489, 0.499, 0.515, 0.529, 0.541, 0.552,
              0.565, 0.577, 0.584, 0.594, 0.607]
    WTreview = [0.124, 0.204, 0.266, 0.302, 0.344, 0.376, 0.398, 0.422, 0.442, 0.461, 0.474, 0.488, 0.504, 0.517, 0.522,
                0.534, 0.547, 0.557, 0.568, 0.576]
    WTc = [0.067, 0.115, 0.151, 0.178, 0.199, 0.222, 0.237, 0.248, 0.263, 0.285, 0.298, 0.31, 0.324, 0.333, 0.346, 0.35,
           0.362, 0.367, 0.373, 0.38]
    WTy = [0.141, 0.236, 0.294, 0.332, 0.368, 0.392, 0.414, 0.435, 0.45, 0.47, 0.482, 0.497, 0.511, 0.519, 0.534, 0.547,
           0.556, 0.57, 0.579, 0.589]
    length = len(TagRec)
    X = np.arange(1, 21)
    # fig = plt.figure(1)
    plt.plot(X, TagRec[::], color='red', linewidth=3.0, marker='^', markersize=8, label='TagRec')
    plt.plot(X, WTreview[::], color='green', linewidth=3.0, marker='o', markersize=8, label='TagRecRaw')
    plt.plot(X, WTc[::], color='magenta', linewidth=3.0, marker='s', markersize=8, label='TagRecWTc')
    plt.plot(X, WTy[::], color='blue', linewidth=3.0, marker='*', markersize=8, label='TagRecWTy')
    plt.legend(loc='upper left')
    plt.xticks(np.arange(0, 21), fontsize=12)
    plt.yticks(np.arange(0, 0.7, 0.1), fontsize=12)
    plt.xlabel('The number of automatic tags', fontsize=12)
    plt.ylabel('HR', fontsize=12)
    # plt.savefig('component_HR')
    plt.show()
    pass
"""





if __name__ == '__main__':
    my_plot()