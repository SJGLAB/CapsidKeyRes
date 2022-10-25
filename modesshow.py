# -*- coding: utf-8 -*-
import numpy
import juli02,transformMatrix03,pdbread02,pdbwrite
   
def modesshows(pdbfile,Ueig):    
    filename = pdbfile
    pi = 3.1415926
    postall,resall,rname,pdb_store,chain_id = pdbread02.pdbread(filename)
    n2 = int(len(resall))
    resn_mon = n2 //60
    postall_c = numpy.zeros([60,3],float)
    for i in range(0,60):
        postall_c[i,:] = numpy.sum(postall[i*resn_mon:(i+1)*resn_mon,:],axis=0) / resn_mon#sum(postall[numpy.arange((numpy.dot(i,resn_mon)),numpy.dot((i+1),resn_mon)),:]) / resn_mon
    
    ave_point1 = numpy.sum(postall_c[numpy.arange(40,45),:],axis=0) / 5.0
    ave_point2 = numpy.sum(postall_c[numpy.arange(55,60),:],axis=0) / 5.0
    r2 = juli02.juli(ave_point1,ave_point2)
    vector_native = numpy.array([[(ave_point1[0] - ave_point2[0]) / r2,(ave_point1[1] - ave_point2[1]) / r2,(ave_point1[2] - ave_point2[2]) / r2]]).T
    vector_trans = numpy.array([[numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
    
    ave_point1_2 = numpy.sum(postall_c[numpy.arange(45,50),:],axis=0) / 5.0
    ave_point2_2 = numpy.sum(postall_c[numpy.arange(50,55),:],axis=0) / 5.0
    r2_2 = juli02.juli(ave_point1_2,ave_point2_2)
    vector_native_2 = numpy.array([[(ave_point1_2[0] - ave_point2_2[0]) / r2_2,(ave_point1_2[1] - ave_point2_2[1]) / r2_2,(ave_point1_2[2] - ave_point2_2[2]) / r2_2]]).T
    vector_trans_2 = numpy.array([[numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
    
    ave_point1_3 = numpy.sum(postall_c[numpy.arange(5,10),:],axis=0) / 5.0
    ave_point2_3 = numpy.sum(postall_c[numpy.arange(10,15),:],axis=0) / 5.0
    r2_3 = juli02.juli(ave_point1_3,ave_point2_3)
    vector_native_3 = numpy.array([[(ave_point1_3[0] - ave_point2_3[0]) / r2_3,(ave_point1_3[1] - ave_point2_3[1]) / r2_3,(ave_point1_3[2] - ave_point2_3[2]) / r2_3]]).T
    vector_trans_3 = numpy.array([[numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(numpy.dot(63.43,pi) / 180),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(numpy.dot(63.43,pi) / 180)]]).T
    
    X = numpy.hstack((numpy.hstack((vector_native,vector_native_2)),vector_native_3))
    X_trans = numpy.hstack((numpy.hstack((vector_trans,vector_trans_2)),vector_trans_3))
    rotation_matrix = numpy.dot(X_trans,(numpy.linalg.inv(X)))#X.I)
    #numpy.save('rotation_matrixdat.npy',rotation_matrix)
    posall,resall,rname,pdb_store,chain_id = pdbread02.pdbread(filename)
    postall_trans = (numpy.dot(rotation_matrix,(postall.T))).T
    postall = numpy.copy(postall_trans)
    
    n2=int(len(resall))
    n3=int(3*n2)
    correx,correy,correz = numpy.zeros([1,n2]),numpy.zeros([1,n2]),numpy.zeros([1,n2])
    for i in range(0,3):
        correx =-Ueig[range(0,n3,3),i]
        correy =-Ueig[range(1,n3,3),i]
        correz =-Ueig[range(2,n3,3),i] 
        writefile='e'+str(i)+'.pdb'
        bildfile='modesshow'+str(i)+'.bild'
        pdbwrite.pdbwrites(writefile,bildfile,postall,pdb_store,n2,correx,correy,correz)
    return writefile,bildfile
    