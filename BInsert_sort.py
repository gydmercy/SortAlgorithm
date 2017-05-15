#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def BInsert_sort(array):
    """
    折半插入排序
    """
    for i in range(1, len(array)):
        value = array[i]
        left = 0
        right = i - 1
        # 先寻找插入位置
        while left <= right:
            mid = (left + right) / 2
            if array[mid] > value:  # 插入点在低半区
                right = mid - 1
            else:  # 插入点在高半区
                left = mid + 1
        # 上述循环结束之时，一定是 right + 1 == left，该 left 的位置即为插入点
        # 插入点及之后的元素位置后移
        for j in range(i, left, -1):
            array[j] = array[j - 1]
        array[left] = value
