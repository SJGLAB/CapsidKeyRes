# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:40:26 2022

@author: hp
"""

# -*- coding: utf-8 -*-
import numpy
    

def rotationmatrix(lamda0=None,mu=None,nu=None,phi=None):#,*args,**kwargs):

    R = numpy.array([[numpy.cos(phi) + numpy.dot(numpy.dot(lamda0,lamda0),(1 - numpy.cos(phi))),numpy.dot(numpy.dot(lamda0,mu),(1 - numpy.cos(phi))) - numpy.dot(nu,numpy.sin(phi)),numpy.dot(numpy.dot(lamda0,nu),(1 - numpy.cos(phi))) + numpy.dot(mu,numpy.sin(phi))],[numpy.dot(numpy.dot(mu,lamda0),(1 - numpy.cos(phi))) + numpy.dot(nu,numpy.sin(phi)),numpy.cos(phi) + numpy.dot(numpy.dot(mu,mu),(1 - numpy.cos(phi))),numpy.dot(numpy.dot(mu,nu),(1 - numpy.cos(phi))) - numpy.dot(lamda0,numpy.sin(phi))],[numpy.dot(numpy.dot(nu,lamda0),(1 - numpy.cos(phi))) - numpy.dot(mu,numpy.sin(phi)),numpy.dot(numpy.dot(nu,mu),(1 - numpy.cos(phi))) + numpy.dot(lamda0,numpy.sin(phi)),numpy.cos(phi) + numpy.dot(numpy.dot(nu,nu),(1 - numpy.cos(phi)))]])
    return R