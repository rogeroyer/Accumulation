# -*- coding:utf-8 -*-

'''
Author : Roger
Date : 2018.06.24
Class ： Ants
'''

import random

ADAPTION = -1


class Ant(object):
    def __init__(self, ant_count):
        self.origin = random.randint(0, ant_count-1)
        self.path = [self.origin]
        self.score = ADAPTION

