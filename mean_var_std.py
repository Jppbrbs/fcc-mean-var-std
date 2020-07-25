#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
# Created by: Joao Pedro Peters Barbosa #
#                                       #
# github: https://github.com/Jppbrbs    #
# email: jpptrs@gmail.com               #
#                                       #
# Date: Jul/2020                        #
#########################################


"""
freeCodeCamp Project1 - Data Analysis with Python Course
"""



import numpy as np
import math
import sys


def calculate(list):
    if len(list) == 9:
        matrix = np.array(list).reshape(3, 3)
        rw = np.size(matrix, 0)
        cl = np.size(matrix, 1)
        total_elements = np.size(matrix)

        mean = [
            matrix[:, 0].sum() / cl, matrix[:, 1].sum() / cl,
            matrix[:, 2].sum() / cl, matrix[0, :].sum() / rw,
            matrix[1, :].sum() / rw, matrix[2, :].sum() / rw,
            matrix.sum() / total_elements
        ]
        # print(mean)

        variance = [((matrix[:, 0] - mean[0])**2).sum() / cl,
                    ((matrix[:, 1] - mean[1])**2).sum() / cl,
                    ((matrix[:, 2] - mean[2])**2).sum() / cl,
                    ((matrix[0, :] - mean[3])**2).sum() / rw,
                    ((matrix[1, :] - mean[4])**2).sum() / rw,
                    ((matrix[2, :] - mean[5])**2).sum() / rw,
                    ((matrix - mean[6])**2).sum() / total_elements]
        # print(variance)

        std_dev = []
        for i in variance:
            std_dev.append(math.sqrt(i))
        # print(std_dev)

        max_ = [
            matrix[:, 0].max(), matrix[:, 1].max(), matrix[:, 2].max(),
            matrix[0, :].max(), matrix[1, :].max(), matrix[2, :].max(),
            matrix.max()
        ]
        # print(max_)

        min_ = [
            matrix[:, 0].min(), matrix[:, 1].min(), matrix[:, 2].min(),
            matrix[0, :].min(), matrix[1, :].min(), matrix[2, :].min(),
            matrix.min()
        ]
        # print(min_)

        sum_ = [
            matrix[:, 0].sum(), matrix[:, 1].sum(), matrix[:, 2].sum(),
            matrix[0, :].sum(), matrix[1, :].sum(), matrix[2, :].sum(),
            matrix.sum()
        ]
        # print(sum_)

        calculations = {
            'mean': [mean[:3], mean[3:6], mean[6]],
            'variance': [variance[:3], variance[3:6], variance[6]],
            'standard deviation': [std_dev[:3], std_dev[3:6], std_dev[6]],
            'max': [max_[:3], max_[3:6], max_[6]],
            'min': [min_[:3], min_[3:6], min_[6]],
            'sum': [sum_[:3], sum_[3:6], sum_[6]]
        }
        print(calculations)

        return calculations

    else:
        # sys.exit()
        raise ValueError("List must contain nine numbers.")
