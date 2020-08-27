#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :extract_err.py
# @Time      :2020/8/3 10:10
# @Author    :herriswang


"""
五天的真实情况取平均，然后预估误差

"""



import re
import numpy as np
import pandas as pd

# global variable
LogFilePath = "input/20190405.txt"
GTFilePath = "input/20190410.txt"

ERRFilePath = "output/20190405-5.csv"

# if __name__ == "__main__":
#     array = np.zeros((100, 11), dtype=np.float32)
#
#     run_code = 0
#     line_extract_rule = r"\[(\d+)\|(.+)\|"
#     re_pattern = re.compile(line_extract_rule)
#
#     with open(ERRFilePath) as in_file:
#         rt = "".join(in_file.readlines())
#
#     row_pos = 0
#     iter = re_pattern.finditer(rt, )
#     for match in iter:
#         column_pos = int(match.group(1))
#         array[row_pos, column_pos] = float(match.group(2))
#         if column_pos == 1:
#             row_pos += 1
#
#     # print(array)
#
#     array = np.abs(array)
#     ret_err = array.mean(axis=0)
#     print(ret_err[1], ret_err[2], ret_err[3], ret_err[4], ret_err[10])
#     run_code = 1


def my_print(array):
    for count, line in enumerate(array):
        # print('site {}, pv: {:.5%}, uv: {:.5%}, clkpv: {:.5%}, ctr: {:.5%},  impratio: {:.5%}'.format(count, line[0], line[1], line[2], line[3], line[4]))
        print('site {}, {:.2%}, {:.2%}, {:.2%}, {:.2%}'.format(count, line[0], line[1], line[3], line[4]))



if __name__ == "__main__":
    run_code = 0

    # output_file = open(ERRFilePath, 'a')
    # output_file.writelines(['imppv, impuv, ctr, impratio'])
    colnames = ['imppv', 'impuv', 'clkpv', 'ctr', 'impratio']
    ret_err = np.zeros((5, 100, 5, 5), np.float32)



    start_date = '20190405'
    end_date = '20190410'
    basic_day = int(start_date[-2:])
    basic_file_path = "input/" + "201904{:0>2d}.txt"
    days = int(end_date[-2:]) - int(start_date[-2:])  # : int

    line_extract_rule_list = []
    line_extract_rule_list.append(r"\| +1\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +2\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +3\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +4\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +10\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")

    with open(LogFilePath) as in_file:
        rt_lines = "".join(in_file.readlines())
    rt_array = np.zeros((100, 5, 5), dtype=np.float32)
    for i in range(5):
        re_pattern = re.compile(line_extract_rule_list[i])

        row_pos = 0
        iter = re_pattern.finditer(rt_lines, )
        for match in iter:
            rt_array[row_pos, i, 0] = int(match.group(1))
            rt_array[row_pos, i, 1] = int(match.group(2))
            rt_array[row_pos, i, 2] = int(match.group(3))
            rt_array[row_pos, i, 3] = float(match.group(4))
            rt_array[row_pos, i, 4] = float(match.group(5))
            row_pos += 1
    rt_array = rt_array.mean(0)
    print(rt_array.shape)


    for day in range(days):
        for i in range(5):
            file2_contents = "".join(open(basic_file_path.format(basic_day + day + 1)).readlines())
            # ret_err = np.zeros((100, 5, 5), dtype=np.float32)
            re_pattern = re.compile(line_extract_rule_list[i])
    
            # row_pos = 0
            # iter = re_pattern.finditer(rt_lines, )
            # for match in iter:
            #     rt_array[row_pos, 0] = int(match.group(1))
            #     rt_array[row_pos, 1] = int(match.group(2))
            #     rt_array[row_pos, 2] = int(match.group(3))
            #     rt_array[row_pos, 3] = float(match.group(4))
            #     rt_array[row_pos, 4] = float(match.group(5))
            #     row_pos += 1
    
            row_pos = 0
            iter = re_pattern.finditer(file2_contents, )
            for match in iter:
                ret_err[day, row_pos, i, 0] = int(match.group(1))
                ret_err[day, row_pos, i, 1] = int(match.group(2))
                ret_err[day, row_pos, i, 2] = int(match.group(3))
                ret_err[day, row_pos, i, 3] = float(match.group(4))
                ret_err[day, row_pos, i, 4] = float(match.group(5))
                row_pos += 1
    print(ret_err.shape)
    ret_err = ret_err.mean(axis=(0, 1))
    print(ret_err.shape)

    rt = np.abs(rt_array - ret_err) / ret_err
    my_print(rt)
    run_code = 1
