#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def bubble_sort(array):
    """
    冒泡排序
    """
    for i in range(len(array)):
        swaped = False
        # 从后往前冒泡，小的元素浮到前面
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
                swaped = True
        if swaped is False:  # 最后一趟没有交换任何元素，则表明数组已经有序
            break
