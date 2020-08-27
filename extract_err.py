#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :extract_err.py
# @Time      :2020/8/3 10:10
# @Author    :herriswang


"""
人群页详情，从log文件中提取100个人群包的 click error rate


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


if __name__ == "__main__":
    run_code = 0

    # output_file = open(ERRFilePath, 'a')
    # output_file.writelines(['imppv, impuv, ctr, impratio'])
    colnames = ['imppv', 'impuv', 'clkpv', 'ctr', 'impratio']
    ret_err = np.zeros((5, 5), np.float32)

    with open(LogFilePath) as in_file:
        rt_lines = "".join(in_file.readlines())

    with open(GTFilePath) as gt_file:
        gt_lines = "".join(gt_file.readlines())

    line_extract_rule_list = []
    line_extract_rule_list.append(r"\| +1\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +2\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +3\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +4\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +10\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")

    for i in range(5):
        rt_array = np.zeros((100, 5), dtype=np.float32)
        gt_array = np.zeros((100, 5), dtype=np.float32)
        re_pattern = re.compile(line_extract_rule_list[i])

        row_pos = 0
        iter = re_pattern.finditer(rt_lines, )
        for match in iter:
            rt_array[row_pos, 0] = int(match.group(1))
            rt_array[row_pos, 1] = int(match.group(2))
            rt_array[row_pos, 2] = int(match.group(3))
            rt_array[row_pos, 3] = float(match.group(4))
            rt_array[row_pos, 4] = float(match.group(5))
            row_pos += 1

        row_pos = 0
        iter = re_pattern.finditer(gt_lines, )
        for match in iter:
            gt_array[row_pos, 0] = int(match.group(1))
            gt_array[row_pos, 1] = int(match.group(2))
            gt_array[row_pos, 2] = int(match.group(3))
            gt_array[row_pos, 3] = float(match.group(4))
            gt_array[row_pos, 4] = float(match.group(5))
            row_pos += 1

        rt_array = np.abs(rt_array - gt_array) / gt_array
        ret_err[i, :] = rt_array.mean(axis=0)

        print('site {}, pv: {:.5%}, uv: {:.5%}, ctr: {:.5%}, impratio: {:.5%}'.format(i, ret_err[i, 0], ret_err[i, 1], ret_err[i, 3], ret_err[i, 4]))
        # np.savetxt(output_file, ret_err, delimiter=",")

    print(ret_err.shape)
    ret_pd = pd.DataFrame(ret_err, columns=colnames)
    ret_pd.to_csv(ERRFilePath, index=False)

    run_code = 1
