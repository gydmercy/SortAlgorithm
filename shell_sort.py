#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def shell_sort(array):
    """
    希尔排序
    """
    gap = len(array) / 2  # 步长，初始取数组长度整除2，之后一直整除2，直到为0
    while gap > 0:
        # 以下排序方法与直接插入排序相同，区别就是步长从 1 变为了每次不同的 gap，最后一次步长必定为 1，就变成了普通的直接插入排序
        for i in range(gap, len(array)):
            value = array[i]
            j = i - gap
            while j >= 0 and array[j] > value:
                array[j + gap] = array[j]
                j -= gap
            array[j + gap] = value
        gap = gap / 2  # 修改步长
