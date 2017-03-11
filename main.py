#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'

import sys


if __name__ == '__main__':

    # 输入
    input_line = sys.stdin.readline().strip()
    array = map(int, input_line.split())

# 插入类排序

    print '直接插入排序'
    from insert_sort import insert_sort
    insert_sort(array)

    # print '折半插入排序'
    # from BInsert_sort import BInsert_sort
    # BInsert_sort(array)

    # print '希尔排序'
    # from shell_sort import shell_sort
    # shell_sort(array)

# 交换类排序

    # print '冒泡排序'
    # from bubble_sort import bubble_sort
    # bubble_sort(array)

    # print '快速排序'
    # from quick_sort import quick_sort
    # quick_sort(array)

# 选择类排序

    # print '简单选择排序'
    # from select_sort import select_sort
    # select_sort(array)

    # print '堆排序'
    # from heap_sort import heap_sort
    # heap_sort(array)

# 归并类排序

    # print '归并排序'
    # from merge_sort import merge_sort
    # merge_sort(array)

    # 输出
    print array
