#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :extract_err.py
# @Time      :2020/8/3 10:10
# @Author    :herriswang


"""
统计除了误差之外的更详细指标
"""

import re
import numpy as np
import pandas as pd
import datetime



def statistic(start_date: str, end_date: str, site: int, indicator: str = 'imppv',):
    """
    :param indicator: 指标  ['imppv', 'impuv', 'clkpv', 'ctr', 'impratio']
    :param site:  站点 [0-4] 微信 QQ 视频 移动联盟 和 全站
    :param start_date:  e.g. 20190405
    :param end_date:  e.g. 20190406
    :return:
    """

    posi = ['imppv', 'impuv', 'clkpv', 'ctr', 'impratio'].index(indicator)
    basic_file_path = "input/" + "201904{:0>2d}.txt"
    basic_day = int(start_date[-2:])
    file1_contents = "".join(open(basic_file_path.format(basic_day)).readlines())

    days = int(end_date[-2:]) - int(start_date[-2:]) # : int

    line_extract_rule_list = []
    line_extract_rule_list.append(r"\| +1\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +2\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +3\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +4\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")
    line_extract_rule_list.append(r"\| +10\|(.+)\|(.+)\|(.+)\|\s*(\d+\.\d+).{0,3}\|\s*(\d+\.\d+).{0,3}\|")

    all_err_array = np.zeros((days, 100, 5), np.float32)
    for day in range(days):
        file2_contents = "".join(open(basic_file_path.format(basic_day + day + 1)).readlines())

        # for i in range(5):
        i = site     # 指定站点
        rt_array = np.zeros((100, 5), dtype=np.float32)
        gt_array = np.zeros((100, 5), dtype=np.float32)
        re_pattern = re.compile(line_extract_rule_list[i])

        row_pos = 0
        iter = re_pattern.finditer(file1_contents, )
        for match in iter:
            rt_array[row_pos, 0] = int(match.group(1))
            rt_array[row_pos, 1] = int(match.group(2))
            rt_array[row_pos, 2] = int(match.group(3))
            rt_array[row_pos, 3] = float(match.group(4))
            rt_array[row_pos, 4] = float(match.group(5))
            row_pos += 1

        row_pos = 0
        iter = re_pattern.finditer(file2_contents, )
        for match in iter:
            gt_array[row_pos, 0] = int(match.group(1))
            gt_array[row_pos, 1] = int(match.group(2))
            gt_array[row_pos, 2] = int(match.group(3))
            gt_array[row_pos, 3] = float(match.group(4))
            gt_array[row_pos, 4] = float(match.group(5))
            row_pos += 1

        err_array = np.abs(rt_array - gt_array)  # (100, 5)
        all_err_array[day, :, :] = err_array
    # print(all_err_array)
    # return all_err_array[:, :, posi]
    return all_err_array, rt_array    # rt理解为是基数


if __name__ == "__main__":
    run_code = 0
    all_ret, base = statistic(start_date='20190405', end_date='20190406', site=0, )


"""
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
"""