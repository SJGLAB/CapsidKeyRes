# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:21:18 2022

@author: hp
"""

# -*- coding: utf-8 -*-
import numpy
from numpy import *
import scipy
from scipy import linalg
import juli02,transformMatrix03,pdbread02
    

def groupanm(pdbfile):

    filename = pdbfile
    pi = 3.1415926
#matlablines:2
    postall,resall,rname,pdb_store,chain_id = pdbread02.pdbread(filename)
#matlablines:6
    n2 = int(len(resall))
    print('n2',n2)
#matlablines:7
    resn_mon = n2 //60
    print('resn_mon',resn_mon)
#matlablines:8
    postall_c = numpy.zeros([60,3],float)
#matlablines:9
    for i in range(0,60):
        postall_c[i,:] = numpy.sum(postall[i*resn_mon:(i+1)*resn_mon,:],axis=0) / resn_mon#sum(postall[numpy.arange((numpy.dot(i,resn_mon)),numpy.dot((i+1),resn_mon)),:]) / resn_mon
#matlablines:11
    ave_point1 = numpy.sum(postall_c[numpy.arange(40,45),:],axis=0) / 5.0
#matlablines:22
    ave_point2 = numpy.sum(postall_c[numpy.arange(55,60),:],axis=0) / 5.0
#matlablines:23
    r2 = juli02.juli(ave_point1,ave_point2)
#matlablines:24
    vector_native = numpy.array([[(ave_point1[0] - ave_point2[0]) / r2,(ave_point1[1] - ave_point2[1]) / r2,(ave_point1[2] - ave_point2[2]) / r2]]).T
    #print('vector_native',vector_native)
#matlablines:25
    vector_trans = numpy.array([[numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
#matlablines:26
    ave_point1_2 = numpy.sum(postall_c[numpy.arange(45,50),:],axis=0) / 5.0
#matlablines:28
    ave_point2_2 = numpy.sum(postall_c[numpy.arange(50,55),:],axis=0) / 5.0
#matlablines:29
    r2_2 = juli02.juli(ave_point1_2,ave_point2_2)
#matlablines:30
    vector_native_2 = numpy.array([[(ave_point1_2[0] - ave_point2_2[0]) / r2_2,(ave_point1_2[1] - ave_point2_2[1]) / r2_2,(ave_point1_2[2] - ave_point2_2[2]) / r2_2]]).T
#matlablines:31
    vector_trans_2 = numpy.array([[numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
#matlablines:32
    ave_point1_3 = numpy.sum(postall_c[numpy.arange(5,10),:],axis=0) / 5.0
#matlablines:34
    ave_point2_3 = numpy.sum(postall_c[numpy.arange(10,15),:],axis=0) / 5.0
#matlablines:35
    r2_3 = juli02.juli(ave_point1_3,ave_point2_3)
#matlablines:36
    vector_native_3 = numpy.array([[(ave_point1_3[0] - ave_point2_3[0]) / r2_3,(ave_point1_3[1] - ave_point2_3[1]) / r2_3,(ave_point1_3[2] - ave_point2_3[2]) / r2_3]]).T
#matlablines:37
    vector_trans_3 = numpy.array([[numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
#matlablines:38
    X = numpy.hstack((numpy.hstack((vector_native,vector_native_2)),vector_native_3))
#matlablines:42
    X_trans = numpy.hstack((numpy.hstack((vector_trans,vector_trans_2)),vector_trans_3))
#matlablines:43
    rotation_matrix = numpy.dot(X_trans,(numpy.linalg.inv(X)))#X.I)
    #numpy.save('rotation_matrixdat.npy',rotation_matrix)
    postall_trans = (numpy.dot(rotation_matrix,(postall.T))).T
#matlablines:51
    postall = numpy.copy(postall_trans)
    numpy.save('postall2dat.npy',postall)
    cutoff=12.0
    Am,T1,T2,G,H,T,P,R,op = transformMatrix03.transformMatrix()#,normAm_u,normT1_u,normT2_u,normG_u,normH_u
    Digmatrix = numpy.eye(resn_mon)
#matlablines:71
    grouphessianAm = numpy.zeros((3*resn_mon,3*resn_mon))
#matlablines:75
    
    normAm = 0
#matlablines:76
    grouphessianT1 = numpy.zeros((3*3*resn_mon,3*3*resn_mon))
#matlablines:77
    
    normT1 = 0
#matlablines:78
    grouphessianT2 = numpy.zeros((3*3*resn_mon,3*3*resn_mon))
#matlablines:79
    
    normT2 = 0
#matlablines:80
    grouphessianG = numpy.zeros((4*3*resn_mon,4*3*resn_mon))
#matlablines:81
    
    normG = 0
#matlablines:82
    grouphessianH = numpy.zeros((5*3*resn_mon,5*3*resn_mon))
#matlablines:83
    
    normH = 0
#matlablines:84
    V_11 = numpy.zeros([3*resn_mon,3*resn_mon],float)
#matlablines:85
    for i in range(0,resn_mon):
        for j in range(0,n2):
            if j != i:
                dist = juli02.juli(postall[i,:],postall[j,:])
#matlablines:89
                if dist <= cutoff:
                    V_11[3*i,3*i] += (postall[j,0] - postall[i,0])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:92
                    V_11[3*i,3*i + 1] += (postall[j,0] - postall[i,0])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:93
                    V_11[3*i,3*i+2] += (postall[j,0] - postall[i,0])*(postall[j,2] - postall[i,2]) / (dist*dist)
#matlablines:94
                    V_11[3*i + 1,3*i] += (postall[j,1] - postall[i,1])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:95
                    V_11[3*i + 1,3*i + 1] += (postall[j,1] - postall[i,1])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:96
                    V_11[3*i + 1,3*i+2] += (postall[j,1] - postall[i,1])*(postall[j,2] - postall[i,2]) / (dist*dist)
#matlablines:97
                    V_11[3*i+2,3*i] += (postall[j,2] - postall[i,2])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:98
                    V_11[3*i+2,3*i + 1] += (postall[j,2] - postall[i,2])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:99
                    V_11[3*i+2,3*i+2] += (postall[j,2] - postall[i,2])*(postall[j,2] - postall[i,2]) / (dist*dist)
#matlablines:100
    for i in range(0,resn_mon):
        for j in range(0,resn_mon):
            if j != i:
                dist = juli02.juli(postall[i,:],postall[j,:])
#matlablines:111
                if dist <= cutoff:
                    V_11[3*i,3*j]= - (postall[j,0] - postall[i,0])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:113
                    V_11[3*i,3*j + 1]= - (postall[j,0] - postall[i,0])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:114
                    V_11[3*i,3*j+2]= - (postall[j,0] - postall[i,0])*(postall[j,2] - postall[i,2]) / (dist*dist)
#matlablines:115
                    V_11[3*i + 1,3*j]= - (postall[j,1] - postall[i,1])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:116
                    V_11[3*i + 1,3*j + 1]= - (postall[j,1] - postall[i,1])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:117
                    V_11[3*i + 1,3*j+2]= - (postall[j,1] - postall[i,1])*(postall[j,2] - postall[i,2]) / (dist*dist)
#matlablines:118
                    V_11[3*i+2,3*j]= - (postall[j,2] - postall[i,2])*(postall[j,0] - postall[i,0]) / (dist*dist)
#matlablines:119
                    V_11[3*i+2,3*j + 1]= - (postall[j,2] - postall[i,2])*(postall[j,1] - postall[i,1]) / (dist*dist)
#matlablines:120
                    V_11[3*i+2,3*j+2]= - (postall[j,2] - postall[i,2])*(postall[j,2] - postall[i,2]) / (dist*dist)

    for M in range(0,60):
        if M == 0:
            V_1M = numpy.copy(V_11)
#matlablines:131
        else:
            V_1M = numpy.zeros([3*resn_mon,3*resn_mon],float)
#matlablines:133
        for i in range(0,resn_mon):
            k = -1
#matlablines:136
            for j in range((int(op[M] - 1)*resn_mon),int(op[M]*resn_mon)):
                k = k + 1
#matlablines:139
                if i == j:
                    continue
                else:
                    dist = juli02.juli(postall[i,:],postall[j,:])
#matlablines:143
                    if dist <= cutoff:
                        V_1M[3*i,3*k]=numpy.dot(- (postall[j,0] - postall[i,0]),(postall[j,0] - postall[i,0])) / (dist*dist)
#matlablines:145
                        V_1M[3*i,3*k + 1]=numpy.dot(- (postall[j,0] - postall[i,0]),(postall[j,1] - postall[i,1])) / (dist*dist)
#matlablines:146
                        V_1M[3*i,3*k+2]=numpy.dot(- (postall[j,0] - postall[i,0]),(postall[j,2] - postall[i,2])) / (dist*dist)
#matlablines:147
                        V_1M[3*i + 1,3*k]=numpy.dot(- (postall[j,1] - postall[i,1]),(postall[j,0] - postall[i,0])) / (dist*dist)
#matlablines:148
                        V_1M[3*i + 1,3*k + 1]=numpy.dot(- (postall[j,1] - postall[i,1]),(postall[j,1] - postall[i,1])) / (dist*dist)
#matlablines:149
                        V_1M[3*i + 1,3*k+2]=numpy.dot(- (postall[j,1] - postall[i,1]),(postall[j,2] - postall[i,2])) / (dist*dist)
#matlablines:150
                        V_1M[3*i+2,3*k]=numpy.dot(- (postall[j,2] - postall[i,2]),(postall[j,0] - postall[i,0])) / (dist*dist)
#matlablines:151
                        V_1M[3*i+2,3*k + 1]=numpy.dot(- (postall[j,2] - postall[i,2]),(postall[j,1] - postall[i,1])) / (dist*dist)
#matlablines:152
                        V_1M[3*i+2,3*k+2]=numpy.dot(- (postall[j,2] - postall[i,2]),(postall[j,2] - postall[i,2])) / (dist*dist)
#matlablines:153         
        T_M = numpy.kron(Digmatrix,R[M,:,:])
#matlablines:163
        grouphessianAm = grouphessianAm + numpy.dot(numpy.dot((60 * Am[M,0,0]),V_1M),T_M)
#matlablines:177
        normAm += numpy.dot((T_M[:,0].T),T_M[:,0])
#matlablines:179
        gt11 = numpy.dot((((60/3)*T1[M,0,0])*V_1M),T_M)
        gt12 = numpy.dot((((60/3)*T1[M,0,1])*V_1M),T_M)
        gt13 = numpy.dot((((60/3)*T1[M,0,2])*V_1M),T_M)
        gt14 = numpy.dot((((60/3)*T1[M,1,0])*V_1M),T_M)
        gt15 = numpy.dot((((60/3)*T1[M,1,1])*V_1M),T_M)
        gt16 = numpy.dot((((60/3)*T1[M,1,2])*V_1M),T_M)
        gt17 = numpy.dot((((60/3)*T1[M,2,0])*V_1M),T_M)
        gt18 = numpy.dot((((60/3)*T1[M,2,1])*V_1M),T_M)
        gt19 = numpy.dot((((60/3)*T1[M,2,2])*V_1M),T_M)
        grouphessianT1 = grouphessianT1 + numpy.bmat('gt11 gt12 gt13;gt14 gt15 gt16;gt17 gt18 gt19')
#matlablines:180
        normT1 += numpy.dot((numpy.dot(T1[M,0,0],T_M[:,0])).T,(numpy.dot(T1[M,0,0],T_M[:,0])))
#matlablines:183
        gt21 = numpy.dot((((60/3)*T2[M,0,0])*V_1M),T_M)
        gt22 = numpy.dot((((60/3)*T2[M,0,1])*V_1M),T_M)
        gt23 = numpy.dot((((60/3)*T2[M,0,2])*V_1M),T_M)
        gt24 = numpy.dot((((60/3)*T2[M,1,0])*V_1M),T_M)
        gt25 = numpy.dot((((60/3)*T2[M,1,1])*V_1M),T_M)
        gt26 = numpy.dot((((60/3)*T2[M,1,2])*V_1M),T_M)
        gt27 = numpy.dot((((60/3)*T2[M,2,0])*V_1M),T_M)
        gt28 = numpy.dot((((60/3)*T2[M,2,1])*V_1M),T_M)
        gt29 = numpy.dot((((60/3)*T2[M,2,2])*V_1M),T_M)
        grouphessianT2 = grouphessianT2 + numpy.bmat('gt21 gt22 gt23;gt24 gt25 gt26;gt27 gt28 gt29')
#matlablines:184
        normT2 += numpy.dot((numpy.dot(T2[M,0,0],T_M[:,0])).T,(numpy.dot(T2[M,0,0],T_M[:,0])))
#matlablines:187
        gg1 = numpy.dot((((60 / 4)*G[M,0,0])*V_1M),T_M)
        gg2 = numpy.dot((((60 / 4)*G[M,0,1])*V_1M),T_M)
        gg3 = numpy.dot((((60 / 4)*G[M,0,2])*V_1M),T_M)
        gg4 = numpy.dot((((60 / 4)*G[M,0,3])*V_1M),T_M)
        gg5 = numpy.dot((((60 / 4)*G[M,1,0])*V_1M),T_M)
        gg6 = numpy.dot((((60 / 4)*G[M,1,1])*V_1M),T_M)
        gg7 = numpy.dot((((60 / 4)*G[M,1,2])*V_1M),T_M)
        gg8 = numpy.dot((((60 / 4)*G[M,1,3])*V_1M),T_M)
        gg9 = numpy.dot((((60 / 4)*G[M,2,0])*V_1M),T_M)
        gg10 = numpy.dot((((60 / 4)*G[M,2,1])*V_1M),T_M)
        gg11 = numpy.dot((((60 / 4)*G[M,2,2])*V_1M),T_M)
        gg12 = numpy.dot((((60 / 4)*G[M,2,3])*V_1M),T_M)
        gg13 = numpy.dot((((60 / 4)*G[M,3,0])*V_1M),T_M)
        gg14 = numpy.dot((((60 / 4)*G[M,3,1])*V_1M),T_M)
        gg15 = numpy.dot((((60 / 4)*G[M,3,2])*V_1M),T_M)
        gg16 = numpy.dot((((60 / 4)*G[M,3,3])*V_1M),T_M)
        grouphessianG = grouphessianG + numpy.bmat('gg1 gg2 gg3 gg4;gg5 gg6 gg7 gg8;gg9 gg10 gg11 gg12;gg13 gg14 gg15 gg16')
#matlablines:188
        normG += numpy.dot((numpy.dot(G[M,0,0],T_M[:,0])).T,(numpy.dot(G[M,0,0],T_M[:,0])))
#matlablines:192
        gh1 = numpy.dot((((60 / 5)*H[M,0,0])*V_1M),T_M)
        gh2 = numpy.dot((((60 / 5)*H[M,0,1])*V_1M),T_M)
        gh3 = numpy.dot((((60 / 5)*H[M,0,2])*V_1M),T_M)
        gh4 = numpy.dot((((60 / 5)*H[M,0,3])*V_1M),T_M)
        gh5 = numpy.dot((((60 / 5)*H[M,0,4])*V_1M),T_M)
        gh6 = numpy.dot((((60 / 5)*H[M,1,0])*V_1M),T_M)
        gh7 = numpy.dot((((60 / 5)*H[M,1,1])*V_1M),T_M)
        gh8 = numpy.dot((((60 / 5)*H[M,1,2])*V_1M),T_M)
        gh9 = numpy.dot((((60 / 5)*H[M,1,3])*V_1M),T_M)
        gh10 = numpy.dot((((60 / 5)*H[M,1,4])*V_1M),T_M)
        gh11 = numpy.dot((((60 / 5)*H[M,2,0])*V_1M),T_M)
        gh12 = numpy.dot((((60 / 5)*H[M,2,1])*V_1M),T_M)
        gh13 = numpy.dot((((60 / 5)*H[M,2,2])*V_1M),T_M)
        gh14 = numpy.dot((((60 / 5)*H[M,2,3])*V_1M),T_M)
        gh15 = numpy.dot((((60 / 5)*H[M,2,4])*V_1M),T_M)
        gh16 = numpy.dot((((60 / 5)*H[M,3,0])*V_1M),T_M)
        gh17 = numpy.dot((((60 / 5)*H[M,3,1])*V_1M),T_M)
        gh18 = numpy.dot((((60 / 5)*H[M,3,2])*V_1M),T_M)
        gh19 = numpy.dot((((60 / 5)*H[M,3,3])*V_1M),T_M)
        gh20 = numpy.dot((((60 / 5)*H[M,3,4])*V_1M),T_M)
        gh21 = numpy.dot((((60 / 5)*H[M,4,0])*V_1M),T_M)
        gh22 = numpy.dot((((60 / 5)*H[M,4,1])*V_1M),T_M)
        gh23 = numpy.dot((((60 / 5)*H[M,4,2])*V_1M),T_M)
        gh24 = numpy.dot((((60 / 5)*H[M,4,3])*V_1M),T_M)
        gh25 = numpy.dot((((60 / 5)*H[M,4,4])*V_1M),T_M)
        grouphessianH = grouphessianH + numpy.bmat('gh1 gh2 gh3 gh4 gh5;gh6 gh7 gh8 gh9 gh10;gh11 gh12 gh13 gh14 gh15;gh16 gh17 gh18 gh19 gh20;gh21 gh22 gh23 gh24 gh25')
#matlablines:193
        normH += numpy.dot((numpy.dot(H[M,0,0],T_M[:,0])).T,(numpy.dot(H[M,0,0],T_M[:,0])))
#matlablines:198
    
    vAm,eAm = numpy.linalg.eig(grouphessianAm)#numpy.linalg.eig(grouphessianAm)
    vAm,eAm = vAm.real,eAm.real
#matlablines:204
    vT1,eT1 = numpy.linalg.eig(grouphessianT1)
    vT1,eT1 = vT1.real,eT1.real
#matlablines:206
    vT2,eT2 = numpy.linalg.eig(grouphessianT2)
    vT2,eT2 = vT2.real,eT2.real
#matlablines:208
    vG,eG = numpy.linalg.eig(grouphessianG)
    vG,eG = vG.real,eG.real
#matlablines:210
    vH,eH = numpy.linalg.eig(grouphessianH)
    vH,eH = vH.real,eH.real
#matlablines:212
    nAm = int(len(vAm))
#matlablines:215
    nT1 = int(len(vT1))
#matlablines:216
    nT2 = int(len(vT2))
#matlablines:217
    nG = int(len(vG))
#matlablines:218
    nH = int(len(vH))
#matlablines:219
    
    #calbfactor(eAm,vAm,eT1,vT1,eT2,vT2,eG,vG,eH,vH,Am,T1,T2,G,H,Digmatrix,R,resn_mon,nAm,nT1,nT2,nG,nH,op,n2,normAm_u,normT1_u,normT2_u,normG_u,normH_u)
    return postall,cutoff,eAm,vAm,eT1,vT1,eT2,vT2,eG,vG,eH,vH,Am,T1,T2,G,H,Digmatrix,R,resn_mon,nAm,nT1,nT2,nG,nH,op,n2#,normAm_u,normT1_u,normT2_u,normG_u,normH_u
    
    