#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def merge_sort(array):
    """
    归并排序
    """
    msort(array, 0, len(array) - 1)


def msort(array, left, right):
    """
    递归二分原数组
    """
    if left < right:  # left == right 的时候，原数组已经划分为单个元素了
        mid = (left + right) / 2
        msort(array, left, mid)  # 左半部分继续二分
        msort(array, mid + 1, right)  # 右半部分继续二分
        merge(array, left, mid, right)  # 两两合并 left ~ mid, mid + 1 ~ right


def merge(array, left, mid, right):
    """
    归并
    """
    tmp = []  # 临时数组
    i = left
    j = mid + 1
    while i <= mid and j <= right:  # 两个数组按顺序合并
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    # 其中一个数组合并完了，就把另一个数组的剩余部分拼接上去
    while i <= mid:
        tmp.append(array[i])
        i += 1
    while j <= right:
        tmp.append(array[j])
        j += 1
    # 将合并好的临时数组替换到原数组上
    for k in range(len(tmp)):
        array[left + k] = tmp[k]
