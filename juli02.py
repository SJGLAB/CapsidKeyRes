# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:23:08 2022

@author: hp
"""

# -*- coding: utf-8 -*-
import numpy


def juli(x1=None,x2=None):#,*args,**kwargs):
    jul = numpy.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2 + (x1[2] - x2[2])**2)
    return jul