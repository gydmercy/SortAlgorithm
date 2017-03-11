#!/usr/local/env python
# -*- coding: utf-8 -*-
__author__ = 'Mercy'
__date__ = '2017-03-10'


def heap_sort(array):
    """
    堆排序
    """
    # 建初始堆
    build_heap(array)
    # 开始排序
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]  # 将堆顶记录与无序子序列的最后一个元素交换位置
        adjust_heap(array, 0, i - 1)  # 继续排列剩余的无序子序列


def build_heap(array):
    """
    建初始堆
    """
    first_node = len(array) / 2 - 1  # 从第一个非叶子节点开始，从下往上，调整元素建堆
    for i in range(first_node, -1, -1):
        adjust_heap(array, i, len(array) - 1)


def adjust_heap(array, head, tail):
    """
    假设 array 数组中，从 head - 1 到 tail 的元素均满足堆的定义，现调整 head 对应元素使之成为大顶堆
    """
    while True:
        left_child = 2 * head + 1
        right_child = 2 * head + 2
        # 当前 head 节点已经没有子节点，则表明已到达最下层，调整堆完成
        if left_child > tail:
            break
        # 寻找两个孩子节点中较大的节点
        max_child = left_child
        if left_child < tail and array[left_child] < array[right_child]:
            max_child = right_child
        # 如果较大的孩子节点比父节点大，则与父节点交换位置
        if array[max_child] > array[head]:
            array[max_child], array[head] = array[head], array[max_child]
        # 如果父节点比子节点大，则不需要调整，说明后续都满足堆定义，直接完成
        else:
            break
        # 以刚才调整的孩子节点作为父节点，继续向下调整
        head = max_child
