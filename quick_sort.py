#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def quick_sort(array):
    """
    快速排序
    """
    qsort(array, 0, len(array) - 1)


def qsort(array, left, right):
    """
    递归排列子序列
    """
    if left < right:
        pivot = partition(array, left, right)  # 将数组划分为左右两部分，并找到枢轴
        qsort(array, left, pivot - 1)
        qsort(array, pivot + 1, right)


def partition(array, left, right):
    """
    将数组序列分为左右两部分，找到枢轴元素，枢轴元素的左边都不大于枢轴的值，右边的元素都不小于枢轴的值
    枢轴元素当前所在的位置都是它在最终有序序列中的位置
    返回枢轴索引
    """
    pivot = left  # 起始枢轴设为最左边的元素的索引
    pivot_value = array[left]
    for i in range(left + 1, right + 1):
        # 如果当前元素比枢轴元素小，就将枢轴往右移动一格，然后与该元素互换位置
        if array[i] < pivot_value:
            pivot += 1
            if pivot != i:
                array[pivot], array[i] = array[i], array[pivot]
    # 将枢轴元素交换到正确的位置上
    array[left], array[pivot] = array[pivot], array[left]
    return pivot
