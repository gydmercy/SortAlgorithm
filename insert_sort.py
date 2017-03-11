#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def insert_sort(array):
    """
    直接插入排序
    """
    for i in range(1, len(array)):
        value = array[i]  # 复制当前元素，用来比较
        j = i - 1
        # 一边寻找插入位置，一边移动
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]  # 当前比较元素比准备插入的元素大，则当前元素后移
            j -= 1
        array[j + 1] = value  # 找到插入位置
