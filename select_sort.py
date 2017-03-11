#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def select_sort(array):
    """
    简单选择排序
    """
    for i in range(len(array)):
        min_index = i
        # 从无序数列中找出最小的元素的索引
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # 将最小元素与无序数列的第一个元素交换位置
        array[i], array[min_index] = array[min_index], array[i]
