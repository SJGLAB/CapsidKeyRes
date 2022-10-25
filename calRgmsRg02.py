# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:55:19 2022

@author: hp
"""
import numpy
import matplotlib.pyplot as plt

import juli02#,groupanm02
def calRgmsRg(postall=None,cutoff=None,eAm=None,vAm=None,eT1=None,vT1=None,eT2=None,vT2=None,eG=None,vG=None,eH=None,vH=None,Am=None,T1=None,T2=None,G=None,H=None,Digmatrix=None,R=None,resn_mon=None,nAm=None,nT1=None,nT2=None,nG=None,nH=None,op=None,n2=None):#,normAm_u=None,normT1_u=None,normT2_u=None,normG_u=None,normH_u=None,*args,**kwargs): 
    # #1.calculate the center of mass of the VLP. here the mass of all residues is 1.
# #P、Q分别为每一组螺旋的两个质心，共30组
    PZ= numpy.zeros(shape=(30,3))#30组质心坐标中的质心P坐标
    QZ= numpy.zeros(shape=(30,3))#30组质心坐标中的质心Q坐标
    del_r_PQ_del_xyzP= numpy.zeros(shape=(30,3))#30组质心平均距离对P求导
    del_r_PQ_del_xyzQ= numpy.zeros(shape=(30,3))#30组质心平均距离对Q求导
    r_PQZ=numpy.zeros(shape=(30,1))#30组质心距离
# #model 1，model 22
    x_P= postall[157:167,0].sum()/10#########
#     #print(len(x_P))
    y_P=postall[157:167,1].sum()/10
    z_P=postall[157:167,2].sum()/10
    x_Q=postall[16390:16400,0].sum()/10
    y_Q=postall[16390:16400,1].sum()/10
    z_Q=postall[16390:16400,2].sum()/10
    P1=[x_P,y_P,z_P]
    Q1=[x_Q,y_Q,z_Q]
    PZ[0,:]=P1
    QZ[0,:]=Q1
    r_PQ1=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[0,0]=r_PQ1
    #print('r_PQZ[1]=',r_PQZ[1])
#model 2，model 41
    x_P=postall[930:940,0].sum()/10
    y_P=postall[930:940,1].sum()/10
    z_P=postall[930:940,2].sum()/10
    x_Q=postall[31077:31087,0].sum()/10
    y_Q=postall[31077:31087,1].sum()/10
    z_Q=postall[31077:31087,2].sum()/10
    P2=[x_P,y_P,z_P]
    Q2=[x_Q,y_Q,z_Q]
    PZ[1,:]=P2
    QZ[1,:]=Q2
    r_PQ2=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[1,0]=r_PQ2
#model 3，model 49
    x_P=postall[1703:1713,0].sum()/10
    y_P=postall[1703:1713,1].sum()/10
    z_P=postall[1703:1713,2].sum()/10
    x_Q=postall[37261:37271,0].sum()/10
    y_Q=postall[37261:37271,1].sum()/10
    z_Q=postall[37261:37271,2].sum()/10
    P3=[x_P,y_P,z_P]
    Q3=[x_Q,y_Q,z_Q]
    PZ[2,:]=P3
    QZ[2,:]=Q3
    r_PQ3=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[2,0]=r_PQ3
#model 4，model 33
    x_P=postall[2476:2486,0].sum()/10
    y_P=postall[2476:2486,1].sum()/10
    z_P=postall[2476:2486,2].sum()/10
    x_Q=postall[24893:24903,0].sum()/10
    y_Q=postall[24893:24903,1].sum()/10
    z_Q=postall[24893:24903,2].sum()/10
    P4=[x_P,y_P,z_P]
    Q4=[x_Q,y_Q,z_Q]
    PZ[3,:]=P4
    QZ[3,:]=Q4
    r_PQ4=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[3,0]=r_PQ4
#model 5，model 10
    x_P=postall[3249:3259,0].sum()/10
    y_P=postall[3249:3259,1].sum()/10
    z_P=postall[3249:3259,2].sum()/10
    x_Q=postall[7114:7124,0].sum()/10
    y_Q=postall[7114:7124,1].sum()/10
    z_Q=postall[7114:7124,2].sum()/10
    P5=[x_P,y_P,z_P]
    Q5=[x_Q,y_Q,z_Q]
    PZ[4,:]=P5
    QZ[4,:]=Q5
    r_PQ5=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[4,0]=r_PQ5
#model 6，model 32
    x_P=postall[4022:4032,0].sum()/10
    y_P=postall[4022:4032,1].sum()/10
    z_P=postall[4022:4032,2].sum()/10
    x_Q=postall[24120:24130,0].sum()/10
    y_Q=postall[24120:24130,1].sum()/10
    z_Q=postall[24120:24130,2].sum()/10
    P6=[x_P,y_P,z_P]
    Q6=[x_Q,y_Q,z_Q]
    PZ[5,:]=P6
    QZ[5,:]=Q6
    r_PQ6=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[5,0]=r_PQ6
# #model 7，model 56
    x_P=postall[4795:4805,0].sum()/10
    y_P=postall[4795:4805,1].sum()/10
    z_P=postall[4795:4805,2].sum()/10
    x_Q=postall[42672:42682,0].sum()/10
    y_Q=postall[42672:42682,1].sum()/10
    z_Q=postall[42672:42682,2].sum()/10
    P7=[x_P,y_P,z_P]
    Q7=[x_Q,y_Q,z_Q]
    PZ[6,:]=P7
    QZ[6,:]=Q7
    r_PQ7=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[6,0]=r_PQ7
#model 8，model 54
    x_P=postall[5568:5578,0].sum()/10
    y_P=postall[5568:5578,1].sum()/10
    z_P=postall[5568:5578,2].sum()/10
    x_Q=postall[41126:41136,0].sum()/10
    y_Q=postall[41126:41136,1].sum()/10
    z_Q=postall[41126:41136,2].sum()/10
    P8=[x_P,y_P,z_P]
    Q8=[x_Q,y_Q,z_Q]
    PZ[7,:]=P8
    QZ[7,:]=Q8
    r_PQ8=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[7,0]=r_PQ8
#model 9，model 23
    x_P=postall[6341:6351,0].sum()/10
    y_P=postall[6341:6351,1].sum()/10
    z_P=postall[6341:6351,2].sum()/10
    x_Q=postall[17163:17173,0].sum()/10
    y_Q=postall[17163:17173,1].sum()/10
    z_Q=postall[17163:17173,2].sum()/10
    P9=[x_P,y_P,z_P]
    Q9=[x_Q,y_Q,z_Q]
    PZ[8,:]=P9
    QZ[8,:]=Q9
    r_PQ9=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[8,0]=r_PQ9
#model 11，model 37
    x_P=postall[7887:7897,0].sum()/10
    y_P=postall[7887:7897,1].sum()/10
    z_P=postall[7887:7897,2].sum()/10
    x_Q=postall[27985:27995,0].sum()/10
    y_Q=postall[27985:27995,1].sum()/10
    z_Q=postall[27985:27995,2].sum()/10
    P10=[x_P,y_P,z_P]
    Q10=[x_Q,y_Q,z_Q]
    PZ[9,:]=P10
    QZ[9,:]=Q10
    r_PQ10=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[9,0]=r_PQ10
# #model 12，model 46
    x_P=postall[8660:8670,0].sum()/10
    y_P=postall[8660:8670,1].sum()/10
    z_P=postall[8660:8670,2].sum()/10
    x_Q=postall[34942:34952,0].sum()/10
    y_Q=postall[34942:34952,1].sum()/10
    z_Q=postall[34942:34952,2].sum()/10
    P11=[x_P,y_P,z_P]
    Q11=[x_Q,y_Q,z_Q]
    PZ[10,:]=P11
    QZ[10,:]=Q11
    r_PQ11=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[10,0]=r_PQ11
    #model 13，model 44
    x_P=postall[9433:9443,0].sum()/10
    y_P=postall[9433:9443,1].sum()/10
    z_P=postall[9433:9443,2].sum()/10
    x_Q=postall[33396:33406,0].sum()/10
    y_Q=postall[33396:33406,1].sum()/10
    z_Q=postall[33396:33406,2].sum()/10
    P12=[x_P,y_P,z_P]
    Q12=[x_Q,y_Q,z_Q]
    PZ[11,:]=P12
    QZ[11,:]=Q12
    r_PQ12=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[11,0]=r_PQ12
    #model 14，model 28
    x_P=postall[10206:10216,0].sum()/10
    y_P=postall[10206:10216,1].sum()/10
    z_P=postall[10206:10216,2].sum()/10
    x_Q=postall[21028:21038,0].sum()/10
    y_Q=postall[21028:21038,1].sum()/10
    z_Q=postall[21028:21038,2].sum()/10
    P13=[x_P,y_P,z_P]
    Q13=[x_Q,y_Q,z_Q]
    PZ[12,:]=P13
    QZ[12,:]=Q13
    r_PQ13=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    print(r_PQ13.shape)
    r_PQZ[12,0]=r_PQ13
    #model 15，model 20
    x_P=postall[10979:10989,0].sum()/10
    y_P=postall[10979:10989,1].sum()/10
    z_P=postall[10979:10989,2].sum()/10
    x_Q=postall[14844:14854,0].sum()/10
    y_Q=postall[14844:14854,1].sum()/10
    z_Q=postall[14844:14854,2].sum()/10
    P14=[x_P,y_P,z_P]
    Q14=[x_Q,y_Q,z_Q]
    PZ[13,:]=P14
    QZ[13,:]=Q14
    r_PQ14=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[13,0]=r_PQ14
    #model 16，model 52
    x_P=postall[11752:11762,0].sum()/10
    y_P=postall[11752:11762,1].sum()/10
    z_P=postall[11752:11762,2].sum()/10
    x_Q=postall[39580:39590,0].sum()/10
    y_Q=postall[39580:39590,1].sum()/10
    z_Q=postall[39580:39590,2].sum()/10
    P15=[x_P,y_P,z_P]
    Q15=[x_Q,y_Q,z_Q]
    PZ[14,:]=P15
    QZ[14,:]=Q15
    r_PQ15=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[14,0]=r_PQ15
    #model 17，model 51
    x_P=postall[12525:12535,0].sum()/10
    y_P=postall[12525:12535,1].sum()/10
    z_P=postall[12525:12535,2].sum()/10
    x_Q=postall[38807:38817,0].sum()/10
    y_Q=postall[38807:38817,1].sum()/10
    z_Q=postall[38807:38817,2].sum()/10
    P16=[x_P,y_P,z_P]
    Q16=[x_Q,y_Q,z_Q]
    PZ[15,:]=P16
    QZ[15,:]=Q16
    r_PQ16=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[15,0]=r_PQ16
    #model 18选取残基14209-14220，model 59选取残基47501-47512。
    x_P=postall[13298:13308,0].sum()/10
    y_P=postall[13298:13308,1].sum()/10
    z_P=postall[13298:13308,2].sum()/10
    x_Q=postall[44991:45001,0].sum()/10
    y_Q=postall[44991:45001,1].sum()/10
    z_Q=postall[44991:45001,2].sum()/10
    P17=[x_P,y_P,z_P]
    Q17=[x_Q,y_Q,z_Q]
    PZ[16,:]=P17
    QZ[16,:]=Q17
    r_PQ17=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[16,0]=r_PQ17
    #model 19，model 38
    x_P=postall[14071:14081,0].sum()/10
    y_P=postall[14071:14081,1].sum()/10
    z_P=postall[14071:14081,2].sum()/10
    x_Q=postall[28758:28768,0].sum()/10
    y_Q=postall[28758:28768,1].sum()/10
    z_Q=postall[28758:28768,2].sum()/10
    P18=[x_P,y_P,z_P]
    Q18=[x_Q,y_Q,z_Q]
    PZ[17,:]=P18
    QZ[17,:]=Q18
    r_PQ18=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[17,0]=r_PQ18
    #model 21，model 42
    x_P=postall[15617:15627,0].sum()/10
    y_P=postall[15617:15627,1].sum()/10
    z_P=postall[15617:15627,2].sum()/10
    x_Q=postall[31850:31860,0].sum()/10
    y_Q=postall[31850:31860,1].sum()/10
    z_Q=postall[31850:31860,2].sum()/10
    P19=[x_P,y_P,z_P]
    Q19=[x_Q,y_Q,z_Q]
    PZ[18,:]=P19
    QZ[18,:]=Q19
    r_PQ19=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[18,0]=r_PQ19
    #model 24，model 53
    x_P=postall[17936:17946,0].sum()/10
    y_P=postall[17936:17946,1].sum()/10
    z_P=postall[17936:17946,2].sum()/10
    x_Q=postall[40353:40363,0].sum()/10
    y_Q=postall[40353:40363,1].sum()/10
    z_Q=postall[40353:40363,2].sum()/10
    P20=[x_P,y_P,z_P]
    Q20=[x_Q,y_Q,z_Q]
    PZ[19,:]=P20
    QZ[19,:]=Q20
    r_PQ20=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[19,0]=r_PQ20
    #model 25，model 30
    x_P=postall[18709:18719,0].sum()/10
    y_P=postall[18709:18719,1].sum()/10
    z_P=postall[18709:18719,2].sum()/10
    x_Q=postall[22574:22584,0].sum()/10
    y_Q=postall[22574:22584,1].sum()/10
    z_Q=postall[22574:22584,2].sum()/10
    P21=[x_P,y_P,z_P]
    Q21=[x_Q,y_Q,z_Q]
    PZ[20,:]=P21
    QZ[20,:]=Q21
    r_PQ21=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[20,0]=r_PQ21
    #model 26，model 52
    x_P=postall[19482:19492,0].sum()/10
    y_P=postall[19482:19492,1].sum()/10
    z_P=postall[19482:19492,2].sum()/10
    x_Q=postall[39580:39590,0].sum()/10
    y_Q=postall[39580:39590,1].sum()/10
    z_Q=postall[39580:39590,2].sum()/10
    P22=[x_P,y_P,z_P]
    Q22=[x_Q,y_Q,z_Q]
    PZ[21,:]=P22
    QZ[21,:]=Q22
    r_PQ22=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[21,0]=r_PQ22
    #model 29，model 43
    x_P=postall[21801:21811,0].sum()/10
    y_P=postall[21801:21811,1].sum()/10
    z_P=postall[21801:21811,2].sum()/10
    x_Q=postall[32623:32633,0].sum()/10
    y_Q=postall[32623:32633,1].sum()/10
    z_Q=postall[32623:32633,2].sum()/10
    P23=[x_P,y_P,z_P]
    Q23=[x_Q,y_Q,z_Q]
    PZ[22,:]=P23
    QZ[22,:]=Q23
    r_PQ23=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[22,0]=r_PQ23
    #model 31，model 57
    x_P=postall[23347:23357,0].sum()/10
    y_P=postall[23347:23357,1].sum()/10
    z_P=postall[23347:23357,2].sum()/10
    x_Q=postall[43445:43455,0].sum()/10
    y_Q=postall[43445:43455,1].sum()/10
    z_Q=postall[43445:43455,2].sum()/10
    P24=[x_P,y_P,z_P]
    Q24=[x_Q,y_Q,z_Q]
    PZ[23,:]=P24
    QZ[23,:]=Q24
    r_PQ24=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[23,0]=r_PQ24
    #model 34，model 48
    x_P=postall[25666:25676,0].sum()/10
    y_P=postall[25666:25676,1].sum()/10
    z_P=postall[25666:25676,2].sum()/10
    x_Q=postall[36488:36498,0].sum()/10
    y_Q=postall[36488:36498,1].sum()/10
    z_Q=postall[36488:36498,2].sum()/10
    P25=[x_P,y_P,z_P]
    Q25=[x_Q,y_Q,z_Q]
    PZ[24,:]=P25
    QZ[24,:]=Q25
    r_PQ25=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[24,0]=r_PQ25
    #model 35，model 40
    x_P=postall[26439:26449,0].sum()/10
    y_P=postall[26439:26449,1].sum()/10
    z_P=postall[26439:26449,2].sum()/10
    x_Q=postall[30304:30314,0].sum()/10
    y_Q=postall[30304:30314,1].sum()/10
    z_Q=postall[30304:30314,2].sum()/10
    P26=[x_P,y_P,z_P]
    Q26=[x_Q,y_Q,z_Q]
    PZ[25,:]=P26
    QZ[25,:]=Q26
    r_PQ26=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[25,0]=r_PQ26
    #model 36，model 47
    x_P=postall[27212:27222,0].sum()/10
    y_P=postall[27212:27222,1].sum()/10
    z_P=postall[27212:27222,2].sum()/10
    x_Q=postall[35715:35725,0].sum()/10
    y_Q=postall[35715:35725,1].sum()/10
    z_Q=postall[35715:35725,2].sum()/10
    P27=[x_P,y_P,z_P]
    Q27=[x_Q,y_Q,z_Q]
    PZ[26,:]=P27
    QZ[26,:]=Q27
    r_PQ27=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[26,0]=r_PQ27
    #model 39，model 58
    x_P=postall[29531:29541,0].sum()/10
    y_P=postall[29531:29541,1].sum()/10
    z_P=postall[29531:29541,2].sum()/10
    x_Q=postall[44218:44228,0].sum()/10
    y_Q=postall[44218:44228,1].sum()/10
    z_Q=postall[44218:44228,2].sum()/10
    P28=[x_P,y_P,z_P]
    Q28=[x_Q,y_Q,z_Q]
    PZ[27,:]=P28
    QZ[27,:]=Q28
    r_PQ28=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[27,0]=r_PQ28
    #model 45，model 50
    x_P=postall[34169:34179,0].sum()/10
    y_P=postall[34169:34179,1].sum()/10
    z_P=postall[34169:34179,2].sum()/10
    x_Q=postall[38034:38044,0].sum()/10
    y_Q=postall[38034:38044,1].sum()/10
    z_Q=postall[38034:38044,2].sum()/10
    P29=[x_P,y_P,z_P]
    Q29=[x_Q,y_Q,z_Q]
    PZ[28,:]=P29
    QZ[28,:]=Q29
    r_PQ29=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[28,0]=r_PQ29
    #model 55，model 60
    x_P=postall[41899:41909,0].sum()/10
    y_P=postall[41899:41909,1].sum()/10
    z_P=postall[41899:41909,2].sum()/10
    x_Q=postall[45764:45774,0].sum()/10
    y_Q=postall[45764:45774,1].sum()/10
    z_Q=postall[45764:45774,2].sum()/10
    P30=[x_P,y_P,z_P]
    Q30=[x_Q,y_Q,z_Q]
    PZ[29,:]=P30
    QZ[29,:]=Q30
    r_PQ30=((x_P-x_Q)*(x_P-x_Q)+(y_P-y_Q)*(y_P-y_Q)+(z_P-z_Q)*(z_P-z_Q))**0.5
    r_PQZ[29,0]=r_PQ30
    #2.calculate the average distance with 30 center of mass.
    r_PQ=(r_PQ1+r_PQ2+r_PQ3+r_PQ4+r_PQ5+r_PQ6+r_PQ7+r_PQ8+r_PQ9+r_PQ10+r_PQ11+r_PQ12+r_PQ13+r_PQ14+r_PQ15+r_PQ16+r_PQ17+r_PQ18+r_PQ19+r_PQ20+r_PQ21+r_PQ22+r_PQ23+r_PQ24+r_PQ25+r_PQ26+r_PQ27+r_PQ28+r_PQ29+r_PQ30)/30
    #3.calculate the partial derivative of r_PQ with respect to x_i,y_i and z_i
    del_r_PQ_del_xyzP=(PZ-QZ)/(30*r_PQZ)
    del_r_PQ_del_xyzQ=(QZ-PZ)/(30*r_PQZ)
    print('r_PQ_dat.npy',r_PQ)
    print('del_r_PQ_del_xyzP_dat.nyp',del_r_PQ_del_xyzP)
    print('del_r_PQ_del_xyzQ_dat.npy',del_r_PQ_del_xyzQ)
# #the dimensions of del_r_PQ_del_xyz is 30*3, i.e. line number is 30 and col num is 3;
# #calculate U_r_PQ,i.e. the fluctuation of r_PQ for all the normal modes
    normAm_u,normT1_u,normT2_u,normG_u,normH_u = 1,1,1,1,1#all the norm are 1.
    vall = numpy.bmat('vAm vT1 vT1 vT1 vT2 vT2 vT2 vG vG vG vG vH vH vH vH vH')
    vall=numpy.squeeze(numpy.array(vall))
    print('vallshape',vall.shape)
    numpy.save('vall_dat',vall)
    rrr = numpy.linspace(1,3*n2,3*n2)
    vall1 = sorted(vall)
    numpy.save('vsort_dat.npy', vall1)
    plt.plot(rrr,vall1)
    plt.savefig('vallsort.png')
    plt.show()
    #vaoo = vall[vall<=nonzerocutoff]
    del rrr,vall1
    meansqure_r_PQ = []
    r_PQ_eigvalues = []
    r_PQ_markers = []
    nonzerocutoff=0.02
# #perturbation
    perturbation = numpy.zeros(shape=(resn_mon,n2))

    connectedresi = []
    connectedresj = []
    distsave = []
    for i in range(0,resn_mon):
        for j in range(0,n2):
            if j!=i:
                dist = juli02.juli(postall[i,:], postall[j,:])
                if dist <= cutoff:
                  connectedresi.append(i)
                  connectedresj.append(j)
                  distsave.append(dist)
    #1.Am
    print('Am:')
    disp = numpy.zeros(shape=(3*n2,nAm))
    #Ur_PQAm = numpy.zeros([nAm,1],float)
    for j in range(0,60):
        T_M = numpy.kron(Digmatrix,R[j,:,:])
        disp_nn= numpy.dot((Am[j,0,0] * T_M),eAm)/normAm_u #normAm_u is 1; see the first line of the code.
  #normalize the disp_nn
        disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp_nn
    
    for i in range(0,nAm):
        if vAm[i] > nonzerocutoff:
      #calculate U_r_PQ
            U_r_PQ_Am=0
            #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            for k in range(0,10):
               
 #U30 += del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
            #U_r_PQ_Am =U1+U2+U3+U4+U5+U6+U7+U8+U9+U10+U11+U12+U13+U14+U15+U16+U17+U18+U19+U20+U21+U22+U23+U24+U25+U26+U27+U28+U29+U30
                U_r_PQ_Am += del_r_PQ_del_xyzP[0,0]*disp[3*(k+157),i]+del_r_PQ_del_xyzP[0,1]*disp[3*(k+157)+1,i]+del_r_PQ_del_xyzP[0,2]*disp[3*(k+157)+2,i]+del_r_PQ_del_xyzQ[0,0]*disp[3*(k+16390),i]+del_r_PQ_del_xyzQ[0,1]*disp[3*(k+16390)+1,i]+del_r_PQ_del_xyzQ[0,2]*disp[3*(k+16390)+2,i]+del_r_PQ_del_xyzP[1,0]*disp[3*(k+930),i]+del_r_PQ_del_xyzP[1,1]*disp[3*(k+930)+1,i]+del_r_PQ_del_xyzP[1,2]*disp[3*(k+930)+2,i]+del_r_PQ_del_xyzQ[1,0]*disp[3*(k+31077),i]+del_r_PQ_del_xyzQ[1,1]*disp[3*(k+31077)+1,i]+del_r_PQ_del_xyzQ[1,2]*disp[3*(k+31077)+2,i]+del_r_PQ_del_xyzP[2,0]*disp[3*(k+1703),i]+del_r_PQ_del_xyzP[2,1]*disp[3*(k+1703)+1,i]+del_r_PQ_del_xyzP[2,2]*disp[3*(k+1703)+2,i]+del_r_PQ_del_xyzQ[2,0]*disp[3*(k+37261),i]+del_r_PQ_del_xyzQ[2,1]*disp[3*(k+37261)+1,i]+del_r_PQ_del_xyzQ[2,2]*disp[3*(k+37261)+2,i]+del_r_PQ_del_xyzP[3,0]*disp[3*(k+2476),i]+del_r_PQ_del_xyzP[3,1]*disp[3*(k+2476)+1,i]+del_r_PQ_del_xyzP[3,2]*disp[3*(k+2476)+2,i]+del_r_PQ_del_xyzQ[3,0]*disp[3*(k+24893),i]+del_r_PQ_del_xyzQ[3,1]*disp[3*(k+24893)+1,i]+del_r_PQ_del_xyzQ[3,2]*disp[3*(k+24893)+2,i]+del_r_PQ_del_xyzP[4,0]*disp[3*(k+3249),i]+del_r_PQ_del_xyzP[4,1]*disp[3*(k+3249)+1,i]+del_r_PQ_del_xyzP[4,2]*disp[3*(k+3249)+2,i]+del_r_PQ_del_xyzQ[4,0]*disp[3*(k+7114),i]+del_r_PQ_del_xyzQ[4,1]*disp[3*(k+7114)+1,i]+del_r_PQ_del_xyzQ[4,2]*disp[3*(k+7114)+2,i]+del_r_PQ_del_xyzP[5,0]*disp[3*(k+4022),i]+del_r_PQ_del_xyzP[5,1]*disp[3*(k+4022)+1,i]+del_r_PQ_del_xyzP[5,2]*disp[3*(k+4022)+2,i]+del_r_PQ_del_xyzQ[5,0]*disp[3*(k+24120),i]+del_r_PQ_del_xyzQ[5,1]*disp[3*(k+24120)+1,i]+del_r_PQ_del_xyzQ[5,2]*disp[3*(k+24120)+2,i]+del_r_PQ_del_xyzP[6,0]*disp[3*(k+4795),i]+del_r_PQ_del_xyzP[6,1]*disp[3*(k+4795)+1,i]+del_r_PQ_del_xyzP[6,2]*disp[3*(k+4795)+2,i]+del_r_PQ_del_xyzQ[6,0]*disp[3*(k+42672),i]+del_r_PQ_del_xyzQ[6,1]*disp[3*(k+42672)+1,i]+del_r_PQ_del_xyzQ[6,2]*disp[3*(k+42672)+2,i]+del_r_PQ_del_xyzP[7,0]*disp[3*(k+5568),i]+del_r_PQ_del_xyzP[7,1]*disp[3*(k+5568)+1,i]+del_r_PQ_del_xyzP[7,2]*disp[3*(k+5568)+2,i]+del_r_PQ_del_xyzQ[7,0]*disp[3*(k+41126),i]+del_r_PQ_del_xyzQ[7,1]*disp[3*(k+41126)+1,i]+del_r_PQ_del_xyzQ[7,2]*disp[3*(k+41126)+2,i]+del_r_PQ_del_xyzP[8,0]*disp[3*(k+6341),i]+del_r_PQ_del_xyzP[8,1]*disp[3*(k+6341)+1,i]+del_r_PQ_del_xyzP[8,2]*disp[3*(k+6341)+2,i]+del_r_PQ_del_xyzQ[8,0]*disp[3*(k+17163),i]+del_r_PQ_del_xyzQ[8,1]*disp[3*(k+17163)+1,i]+del_r_PQ_del_xyzQ[8,2]*disp[3*(k+17163)+2,i]+del_r_PQ_del_xyzP[9,0]*disp[3*(k+7887),i]+del_r_PQ_del_xyzP[9,1]*disp[3*(k+7887)+1,i]+del_r_PQ_del_xyzP[9,2]*disp[3*(k+7887)+2,i]+del_r_PQ_del_xyzQ[9,0]*disp[3*(k+27985),i]+del_r_PQ_del_xyzQ[9,1]*disp[3*(k+27985)+1,i]+del_r_PQ_del_xyzQ[9,2]*disp[3*(k+27985)+2,i]+del_r_PQ_del_xyzP[10,0]*disp[3*(k+8660),i]+del_r_PQ_del_xyzP[10,1]*disp[3*(k+8660)+1,i]+del_r_PQ_del_xyzP[10,2]*disp[3*(k+8660)+2,i]+del_r_PQ_del_xyzQ[10,0]*disp[3*(k+34942),i]+del_r_PQ_del_xyzQ[10,1]*disp[3*(k+34942)+1,i]+del_r_PQ_del_xyzQ[10,2]*disp[3*(k+34942)+2,i]+ del_r_PQ_del_xyzP[11,0]*disp[3*(k+9433),i]+del_r_PQ_del_xyzP[11,1]*disp[3*(k+9433)+1,i]+del_r_PQ_del_xyzP[11,2]*disp[3*(k+9433)+2,i]+del_r_PQ_del_xyzQ[11,0]*disp[3*(k+33396),i]+del_r_PQ_del_xyzQ[11,1]*disp[3*(k+33396)+1,i]+del_r_PQ_del_xyzQ[11,2]*disp[3*(k+33396)+2,i]+ del_r_PQ_del_xyzP[12,0]*disp[3*(k+10206),i]+del_r_PQ_del_xyzP[12,1]*disp[3*(k+10206)+1,i]+del_r_PQ_del_xyzP[12,2]*disp[3*(k+10206)+2,i]+del_r_PQ_del_xyzQ[12,0]*disp[3*(k+21028),i]+del_r_PQ_del_xyzQ[12,1]*disp[3*(k+21028)+1,i]+del_r_PQ_del_xyzQ[12,2]*disp[3*(k+21028)+2,i]+del_r_PQ_del_xyzP[13,0]*disp[3*(k+10979),i]+del_r_PQ_del_xyzP[13,1]*disp[3*(k+10979)+1,i]+del_r_PQ_del_xyzP[13,2]*disp[3*(k+10979)+2,i]+del_r_PQ_del_xyzQ[13,0]*disp[3*(k+14844),i]+del_r_PQ_del_xyzQ[13,1]*disp[3*(k+14844)+1,i]+del_r_PQ_del_xyzQ[13,2]*disp[3*(k+14844)+2,i]+del_r_PQ_del_xyzP[14,0]*disp[3*(k+11752),i]+del_r_PQ_del_xyzP[14,1]*disp[3*(k+11752)+1,i]+del_r_PQ_del_xyzP[14,2]*disp[3*(k+11752)+2,i]+del_r_PQ_del_xyzQ[14,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[14,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[14,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[15,0]*disp[3*(k+12525),i]+del_r_PQ_del_xyzP[15,1]*disp[3*(k+12525)+1,i]+del_r_PQ_del_xyzP[15,2]*disp[3*(k+12525)+2,i]+del_r_PQ_del_xyzQ[15,0]*disp[3*(k+38807),i]+del_r_PQ_del_xyzQ[15,1]*disp[3*(k+38807)+1,i]+del_r_PQ_del_xyzQ[15,2]*disp[3*(k+38807)+2,i]+del_r_PQ_del_xyzP[16,0]*disp[3*(k+13298),i]+del_r_PQ_del_xyzP[16,1]*disp[3*(k+13298)+1,i]+del_r_PQ_del_xyzP[16,2]*disp[3*(k+13298)+2,i]+del_r_PQ_del_xyzQ[16,0]*disp[3*(k+44991),i]+del_r_PQ_del_xyzQ[16,1]*disp[3*(k+44991)+1,i]+del_r_PQ_del_xyzQ[16,2]*disp[3*(k+44991)+2,i]+del_r_PQ_del_xyzP[17,0]*disp[3*(k+14071),i]+del_r_PQ_del_xyzP[17,1]*disp[3*(k+14071)+1,i]+del_r_PQ_del_xyzP[17,2]*disp[3*(k+14071)+2,i]+del_r_PQ_del_xyzQ[17,0]*disp[3*(k+28758),i]+del_r_PQ_del_xyzQ[17,1]*disp[3*(k+28758)+1,i]+del_r_PQ_del_xyzQ[17,2]*disp[3*(k+28758)+2,i]+ del_r_PQ_del_xyzP[18,0]*disp[3*(k+15617),i]+del_r_PQ_del_xyzP[18,1]*disp[3*(k+15617)+1,i]+del_r_PQ_del_xyzP[18,2]*disp[3*(k+15617)+2,i]+del_r_PQ_del_xyzQ[18,0]*disp[3*(k+31850),i]+del_r_PQ_del_xyzQ[18,1]*disp[3*(k+31850)+1,i]+del_r_PQ_del_xyzQ[18,2]*disp[3*(k+31850)+2,i]+del_r_PQ_del_xyzP[19,0]*disp[3*(k+17936),i]+del_r_PQ_del_xyzP[19,1]*disp[3*(k+17936)+1,i]+del_r_PQ_del_xyzP[19,2]*disp[3*(k+17936)+2,i]+del_r_PQ_del_xyzQ[19,0]*disp[3*(k+40353),i]+del_r_PQ_del_xyzQ[19,1]*disp[3*(k+40353)+1,i]+del_r_PQ_del_xyzQ[19,2]*disp[3*(k+40353)+2,i]+del_r_PQ_del_xyzP[20,0]*disp[3*(k+18709),i]+del_r_PQ_del_xyzP[20,1]*disp[3*(k+18709)+1,i]+del_r_PQ_del_xyzP[20,2]*disp[3*(k+18709)+2,i]+del_r_PQ_del_xyzQ[20,0]*disp[3*(k+22574),i]+del_r_PQ_del_xyzQ[20,1]*disp[3*(k+22574)+1,i]+del_r_PQ_del_xyzQ[20,2]*disp[3*(k+22574)+2,i]+ del_r_PQ_del_xyzP[21,0]*disp[3*(k+19482),i]+del_r_PQ_del_xyzP[21,1]*disp[3*(k+19482)+1,i]+del_r_PQ_del_xyzP[21,2]*disp[3*(k+19482)+2,i]+del_r_PQ_del_xyzQ[21,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[21,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[21,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[22,0]*disp[3*(k+21801),i]+del_r_PQ_del_xyzP[22,1]*disp[3*(k+21801)+1,i]+del_r_PQ_del_xyzP[22,2]*disp[3*(k+21801)+2,i]+del_r_PQ_del_xyzQ[22,0]*disp[3*(k+32623),i]+del_r_PQ_del_xyzQ[22,1]*disp[3*(k+32623)+1,i]+del_r_PQ_del_xyzQ[22,2]*disp[3*(k+32623)+2,i]+ del_r_PQ_del_xyzP[23,0]*disp[3*(k+23347),i]+del_r_PQ_del_xyzP[23,1]*disp[3*(k+23347)+1,i]+del_r_PQ_del_xyzP[23,2]*disp[3*(k+23347)+2,i]+del_r_PQ_del_xyzQ[23,0]*disp[3*(k+43445),i]+del_r_PQ_del_xyzQ[23,1]*disp[3*(k+43445)+1,i]+del_r_PQ_del_xyzQ[23,2]*disp[3*(k+43445)+2,i]+del_r_PQ_del_xyzP[24,0]*disp[3*(k+25666),i]+del_r_PQ_del_xyzP[24,1]*disp[3*(k+25666)+1,i]+del_r_PQ_del_xyzP[24,2]*disp[3*(k+25666)+2,i]+del_r_PQ_del_xyzQ[24,0]*disp[3*(k+36488),i]+del_r_PQ_del_xyzQ[24,1]*disp[3*(k+36488)+1,i]+del_r_PQ_del_xyzQ[24,2]*disp[3*(k+36488)+2,i]+del_r_PQ_del_xyzP[25,0]*disp[3*(k+26439),i]+del_r_PQ_del_xyzP[25,1]*disp[3*(k+26439)+1,i]+del_r_PQ_del_xyzP[25,2]*disp[3*(k+26439)+2,i]+del_r_PQ_del_xyzQ[25,0]*disp[3*(k+30304),i]+del_r_PQ_del_xyzQ[25,1]*disp[3*(k+30304)+1,i]+del_r_PQ_del_xyzQ[25,2]*disp[3*(k+30304)+2,i]+ del_r_PQ_del_xyzP[26,0]*disp[3*(k+27212),i]+del_r_PQ_del_xyzP[26,1]*disp[3*(k+27212)+1,i]+del_r_PQ_del_xyzP[26,2]*disp[3*(k+27212)+2,i]+del_r_PQ_del_xyzQ[26,0]*disp[3*(k+35715),i]+del_r_PQ_del_xyzQ[26,1]*disp[3*(k+35715)+1,i]+del_r_PQ_del_xyzQ[26,2]*disp[3*(k+35715)+2,i]+ del_r_PQ_del_xyzP[27,0]*disp[3*(k+29531),i]+del_r_PQ_del_xyzP[27,1]*disp[3*(k+29531)+1,i]+del_r_PQ_del_xyzP[27,2]*disp[3*(k+29531)+2,i]+del_r_PQ_del_xyzQ[27,0]*disp[3*(k+44218),i]+del_r_PQ_del_xyzQ[27,1]*disp[3*(k+44218)+1,i]+del_r_PQ_del_xyzQ[27,2]*disp[3*(k+44218)+2,i]+del_r_PQ_del_xyzP[28,0]*disp[3*(k+34169),i]+del_r_PQ_del_xyzP[28,1]*disp[3*(k+34169)+1,i]+del_r_PQ_del_xyzP[28,2]*disp[3*(k+34169)+2,i]+del_r_PQ_del_xyzQ[28,0]*disp[3*(k+38034),i]+del_r_PQ_del_xyzQ[28,1]*disp[3*(k+38034)+1,i]+del_r_PQ_del_xyzQ[28,2]*disp[3*(k+38034)+2,i]+del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
                #Ur_PQAm(i,1)=U_r_PQ_Am
            meansqure_r_PQ_cal = U_r_PQ_Am * U_r_PQ_Am / vAm[i]
            meansqure_r_PQ.append(meansqure_r_PQ_cal)
            r_PQ_eigvalues.append(vAm[i])
            r_PQ_markers.append(1)
    #%calculate perturbation for each pairwise residues
            for ii in range(0,len(connectedresi)):
                res_i = connectedresi[ii]
                res_j = connectedresj[ii]
                dist = distsave[ii]
          # perturbation[res_i,res_j] += ((((postall(res_i,1)-postall(res_j,1))/dist)*U_r_PQ_Am*disp(3*res_i-2,i)+((postall(res_i,2)-postall(res_j,2))/dist)*U_r_PQ_Am*disp(3*res_i-1,i)+((postall(res_i,3)-postall(res_j,3))/dist)*U_r_PQ_Am*disp(3*res_i,i)-((postall(res_i,1)-postall(res_j,1))/dist)*U_r_PQ_Am*disp(3*res_j-2,i)-((postall(res_i,2)-postall(res_j,2))/dist)*U_r_PQ_Am*disp(3*res_j-1,i)-((postall(res_i,3)-postall(res_j,3))/dist)*U_r_PQ_Am*disp(3*res_j,i))/vAm(i,i));
                perturbation[res_i, res_j] += (((postall[res_i, 0] - postall[res_j,0]) / dist) * U_r_PQ_Am* disp[3 * res_i, i] + ((postall[res_i, 1] - postall[res_j, 1])/ dist) * U_r_PQ_Am * disp[3 * res_i + 1, i] + ((postall[res_i,2] - postall[res_j,2]) / dist) * U_r_PQ_Am * disp[3 * res_i+2, i] - ((postall[res_i, 0] - postall[res_j, 0])/ dist)* U_r_PQ_Am * disp[3 * res_j, i] - ((postall[res_i,1] - postall[res_j,1])/ dist) * U_r_PQ_Am * disp[3 * res_j + 1, i] - ((postall[res_i, 2] - postall[res_j, 2]) / dist) * U_r_PQ_Am * disp[3 * res_j+2, i]) / vAm[i]
               
    print('U_r_PQ_Am_dat.nyp',U_r_PQ_Am)
    print('perturbation',perturbation)  
  #2_1.T1_1_2_3  
    #Ur_PQT1=numpy.zeros([nT1,3],float)
    print('T1:')
    for hangi in range(0,3):
        for modei in range(0,3):
            disp = numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):   
                T_M = numpy.kron(Digmatrix,R[j,:,:])
                disp1_nn = numpy.dot((T1[j,hangi, 0] * T_M),eT1[0:3 * resn_mon,:])/ normT1_u
                disp2_nn = numpy.dot((T1[j,hangi, 1] * T_M),eT1[3 * resn_mon:3 * 2 * resn_mon,:])/ normT1_u
                disp3_nn = numpy.dot((T1[j,hangi, 2] * T_M),eT1[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT1_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
                                    
            for i in range(0,nAm):
                if vT1[ nAm * modei + i] > nonzerocutoff:
                    U_r_PQ_T1 = 0
                    #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                    for k in range(0,10):                 
                        U_r_PQ_T1 += del_r_PQ_del_xyzP[0,0]*disp[3*(k+157),i]+del_r_PQ_del_xyzP[0,1]*disp[3*(k+157)+1,i]+del_r_PQ_del_xyzP[0,2]*disp[3*(k+157)+2,i]+del_r_PQ_del_xyzQ[0,0]*disp[3*(k+16390),i]+del_r_PQ_del_xyzQ[0,1]*disp[3*(k+16390)+1,i]+del_r_PQ_del_xyzQ[0,2]*disp[3*(k+16390)+2,i]+del_r_PQ_del_xyzP[1,0]*disp[3*(k+930),i]+del_r_PQ_del_xyzP[1,1]*disp[3*(k+930)+1,i]+del_r_PQ_del_xyzP[1,2]*disp[3*(k+930)+2,i]+del_r_PQ_del_xyzQ[1,0]*disp[3*(k+31077),i]+del_r_PQ_del_xyzQ[1,1]*disp[3*(k+31077)+1,i]+del_r_PQ_del_xyzQ[1,2]*disp[3*(k+31077)+2,i]+del_r_PQ_del_xyzP[2,0]*disp[3*(k+1703),i]+del_r_PQ_del_xyzP[2,1]*disp[3*(k+1703)+1,i]+del_r_PQ_del_xyzP[2,2]*disp[3*(k+1703)+2,i]+del_r_PQ_del_xyzQ[2,0]*disp[3*(k+37261),i]+del_r_PQ_del_xyzQ[2,1]*disp[3*(k+37261)+1,i]+del_r_PQ_del_xyzQ[2,2]*disp[3*(k+37261)+2,i]+del_r_PQ_del_xyzP[3,0]*disp[3*(k+2476),i]+del_r_PQ_del_xyzP[3,1]*disp[3*(k+2476)+1,i]+del_r_PQ_del_xyzP[3,2]*disp[3*(k+2476)+2,i]+del_r_PQ_del_xyzQ[3,0]*disp[3*(k+24893),i]+del_r_PQ_del_xyzQ[3,1]*disp[3*(k+24893)+1,i]+del_r_PQ_del_xyzQ[3,2]*disp[3*(k+24893)+2,i]+del_r_PQ_del_xyzP[4,0]*disp[3*(k+3249),i]+del_r_PQ_del_xyzP[4,1]*disp[3*(k+3249)+1,i]+del_r_PQ_del_xyzP[4,2]*disp[3*(k+3249)+2,i]+del_r_PQ_del_xyzQ[4,0]*disp[3*(k+7114),i]+del_r_PQ_del_xyzQ[4,1]*disp[3*(k+7114)+1,i]+del_r_PQ_del_xyzQ[4,2]*disp[3*(k+7114)+2,i]+del_r_PQ_del_xyzP[5,0]*disp[3*(k+4022),i]+del_r_PQ_del_xyzP[5,1]*disp[3*(k+4022)+1,i]+del_r_PQ_del_xyzP[5,2]*disp[3*(k+4022)+2,i]+del_r_PQ_del_xyzQ[5,0]*disp[3*(k+24120),i]+del_r_PQ_del_xyzQ[5,1]*disp[3*(k+24120)+1,i]+del_r_PQ_del_xyzQ[5,2]*disp[3*(k+24120)+2,i]+del_r_PQ_del_xyzP[6,0]*disp[3*(k+4795),i]+del_r_PQ_del_xyzP[6,1]*disp[3*(k+4795)+1,i]+del_r_PQ_del_xyzP[6,2]*disp[3*(k+4795)+2,i]+del_r_PQ_del_xyzQ[6,0]*disp[3*(k+42672),i]+del_r_PQ_del_xyzQ[6,1]*disp[3*(k+42672)+1,i]+del_r_PQ_del_xyzQ[6,2]*disp[3*(k+42672)+2,i]+del_r_PQ_del_xyzP[7,0]*disp[3*(k+5568),i]+del_r_PQ_del_xyzP[7,1]*disp[3*(k+5568)+1,i]+del_r_PQ_del_xyzP[7,2]*disp[3*(k+5568)+2,i]+del_r_PQ_del_xyzQ[7,0]*disp[3*(k+41126),i]+del_r_PQ_del_xyzQ[7,1]*disp[3*(k+41126)+1,i]+del_r_PQ_del_xyzQ[7,2]*disp[3*(k+41126)+2,i]+del_r_PQ_del_xyzP[8,0]*disp[3*(k+6341),i]+del_r_PQ_del_xyzP[8,1]*disp[3*(k+6341)+1,i]+del_r_PQ_del_xyzP[8,2]*disp[3*(k+6341)+2,i]+del_r_PQ_del_xyzQ[8,0]*disp[3*(k+17163),i]+del_r_PQ_del_xyzQ[8,1]*disp[3*(k+17163)+1,i]+del_r_PQ_del_xyzQ[8,2]*disp[3*(k+17163)+2,i]+del_r_PQ_del_xyzP[9,0]*disp[3*(k+7887),i]+del_r_PQ_del_xyzP[9,1]*disp[3*(k+7887)+1,i]+del_r_PQ_del_xyzP[9,2]*disp[3*(k+7887)+2,i]+del_r_PQ_del_xyzQ[9,0]*disp[3*(k+27985),i]+del_r_PQ_del_xyzQ[9,1]*disp[3*(k+27985)+1,i]+del_r_PQ_del_xyzQ[9,2]*disp[3*(k+27985)+2,i]+del_r_PQ_del_xyzP[10,0]*disp[3*(k+8660),i]+del_r_PQ_del_xyzP[10,1]*disp[3*(k+8660)+1,i]+del_r_PQ_del_xyzP[10,2]*disp[3*(k+8660)+2,i]+del_r_PQ_del_xyzQ[10,0]*disp[3*(k+34942),i]+del_r_PQ_del_xyzQ[10,1]*disp[3*(k+34942)+1,i]+del_r_PQ_del_xyzQ[10,2]*disp[3*(k+34942)+2,i]+ del_r_PQ_del_xyzP[11,0]*disp[3*(k+9433),i]+del_r_PQ_del_xyzP[11,1]*disp[3*(k+9433)+1,i]+del_r_PQ_del_xyzP[11,2]*disp[3*(k+9433)+2,i]+del_r_PQ_del_xyzQ[11,0]*disp[3*(k+33396),i]+del_r_PQ_del_xyzQ[11,1]*disp[3*(k+33396)+1,i]+del_r_PQ_del_xyzQ[11,2]*disp[3*(k+33396)+2,i]+ del_r_PQ_del_xyzP[12,0]*disp[3*(k+10206),i]+del_r_PQ_del_xyzP[12,1]*disp[3*(k+10206)+1,i]+del_r_PQ_del_xyzP[12,2]*disp[3*(k+10206)+2,i]+del_r_PQ_del_xyzQ[12,0]*disp[3*(k+21028),i]+del_r_PQ_del_xyzQ[12,1]*disp[3*(k+21028)+1,i]+del_r_PQ_del_xyzQ[12,2]*disp[3*(k+21028)+2,i]+del_r_PQ_del_xyzP[13,0]*disp[3*(k+10979),i]+del_r_PQ_del_xyzP[13,1]*disp[3*(k+10979)+1,i]+del_r_PQ_del_xyzP[13,2]*disp[3*(k+10979)+2,i]+del_r_PQ_del_xyzQ[13,0]*disp[3*(k+14844),i]+del_r_PQ_del_xyzQ[13,1]*disp[3*(k+14844)+1,i]+del_r_PQ_del_xyzQ[13,2]*disp[3*(k+14844)+2,i]+del_r_PQ_del_xyzP[14,0]*disp[3*(k+11752),i]+del_r_PQ_del_xyzP[14,1]*disp[3*(k+11752)+1,i]+del_r_PQ_del_xyzP[14,2]*disp[3*(k+11752)+2,i]+del_r_PQ_del_xyzQ[14,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[14,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[14,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[15,0]*disp[3*(k+12525),i]+del_r_PQ_del_xyzP[15,1]*disp[3*(k+12525)+1,i]+del_r_PQ_del_xyzP[15,2]*disp[3*(k+12525)+2,i]+del_r_PQ_del_xyzQ[15,0]*disp[3*(k+38807),i]+del_r_PQ_del_xyzQ[15,1]*disp[3*(k+38807)+1,i]+del_r_PQ_del_xyzQ[15,2]*disp[3*(k+38807)+2,i]+del_r_PQ_del_xyzP[16,0]*disp[3*(k+13298),i]+del_r_PQ_del_xyzP[16,1]*disp[3*(k+13298)+1,i]+del_r_PQ_del_xyzP[16,2]*disp[3*(k+13298)+2,i]+del_r_PQ_del_xyzQ[16,0]*disp[3*(k+44991),i]+del_r_PQ_del_xyzQ[16,1]*disp[3*(k+44991)+1,i]+del_r_PQ_del_xyzQ[16,2]*disp[3*(k+44991)+2,i]+del_r_PQ_del_xyzP[17,0]*disp[3*(k+14071),i]+del_r_PQ_del_xyzP[17,1]*disp[3*(k+14071)+1,i]+del_r_PQ_del_xyzP[17,2]*disp[3*(k+14071)+2,i]+del_r_PQ_del_xyzQ[17,0]*disp[3*(k+28758),i]+del_r_PQ_del_xyzQ[17,1]*disp[3*(k+28758)+1,i]+del_r_PQ_del_xyzQ[17,2]*disp[3*(k+28758)+2,i]+ del_r_PQ_del_xyzP[18,0]*disp[3*(k+15617),i]+del_r_PQ_del_xyzP[18,1]*disp[3*(k+15617)+1,i]+del_r_PQ_del_xyzP[18,2]*disp[3*(k+15617)+2,i]+del_r_PQ_del_xyzQ[18,0]*disp[3*(k+31850),i]+del_r_PQ_del_xyzQ[18,1]*disp[3*(k+31850)+1,i]+del_r_PQ_del_xyzQ[18,2]*disp[3*(k+31850)+2,i]+del_r_PQ_del_xyzP[19,0]*disp[3*(k+17936),i]+del_r_PQ_del_xyzP[19,1]*disp[3*(k+17936)+1,i]+del_r_PQ_del_xyzP[19,2]*disp[3*(k+17936)+2,i]+del_r_PQ_del_xyzQ[19,0]*disp[3*(k+40353),i]+del_r_PQ_del_xyzQ[19,1]*disp[3*(k+40353)+1,i]+del_r_PQ_del_xyzQ[19,2]*disp[3*(k+40353)+2,i]+del_r_PQ_del_xyzP[20,0]*disp[3*(k+18709),i]+del_r_PQ_del_xyzP[20,1]*disp[3*(k+18709)+1,i]+del_r_PQ_del_xyzP[20,2]*disp[3*(k+18709)+2,i]+del_r_PQ_del_xyzQ[20,0]*disp[3*(k+22574),i]+del_r_PQ_del_xyzQ[20,1]*disp[3*(k+22574)+1,i]+del_r_PQ_del_xyzQ[20,2]*disp[3*(k+22574)+2,i]+ del_r_PQ_del_xyzP[21,0]*disp[3*(k+19482),i]+del_r_PQ_del_xyzP[21,1]*disp[3*(k+19482)+1,i]+del_r_PQ_del_xyzP[21,2]*disp[3*(k+19482)+2,i]+del_r_PQ_del_xyzQ[21,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[21,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[21,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[22,0]*disp[3*(k+21801),i]+del_r_PQ_del_xyzP[22,1]*disp[3*(k+21801)+1,i]+del_r_PQ_del_xyzP[22,2]*disp[3*(k+21801)+2,i]+del_r_PQ_del_xyzQ[22,0]*disp[3*(k+32623),i]+del_r_PQ_del_xyzQ[22,1]*disp[3*(k+32623)+1,i]+del_r_PQ_del_xyzQ[22,2]*disp[3*(k+32623)+2,i]+ del_r_PQ_del_xyzP[23,0]*disp[3*(k+23347),i]+del_r_PQ_del_xyzP[23,1]*disp[3*(k+23347)+1,i]+del_r_PQ_del_xyzP[23,2]*disp[3*(k+23347)+2,i]+del_r_PQ_del_xyzQ[23,0]*disp[3*(k+43445),i]+del_r_PQ_del_xyzQ[23,1]*disp[3*(k+43445)+1,i]+del_r_PQ_del_xyzQ[23,2]*disp[3*(k+43445)+2,i]+del_r_PQ_del_xyzP[24,0]*disp[3*(k+25666),i]+del_r_PQ_del_xyzP[24,1]*disp[3*(k+25666)+1,i]+del_r_PQ_del_xyzP[24,2]*disp[3*(k+25666)+2,i]+del_r_PQ_del_xyzQ[24,0]*disp[3*(k+36488),i]+del_r_PQ_del_xyzQ[24,1]*disp[3*(k+36488)+1,i]+del_r_PQ_del_xyzQ[24,2]*disp[3*(k+36488)+2,i]+del_r_PQ_del_xyzP[25,0]*disp[3*(k+26439),i]+del_r_PQ_del_xyzP[25,1]*disp[3*(k+26439)+1,i]+del_r_PQ_del_xyzP[25,2]*disp[3*(k+26439)+2,i]+del_r_PQ_del_xyzQ[25,0]*disp[3*(k+30304),i]+del_r_PQ_del_xyzQ[25,1]*disp[3*(k+30304)+1,i]+del_r_PQ_del_xyzQ[25,2]*disp[3*(k+30304)+2,i]+ del_r_PQ_del_xyzP[26,0]*disp[3*(k+27212),i]+del_r_PQ_del_xyzP[26,1]*disp[3*(k+27212)+1,i]+del_r_PQ_del_xyzP[26,2]*disp[3*(k+27212)+2,i]+del_r_PQ_del_xyzQ[26,0]*disp[3*(k+35715),i]+del_r_PQ_del_xyzQ[26,1]*disp[3*(k+35715)+1,i]+del_r_PQ_del_xyzQ[26,2]*disp[3*(k+35715)+2,i]+ del_r_PQ_del_xyzP[27,0]*disp[3*(k+29531),i]+del_r_PQ_del_xyzP[27,1]*disp[3*(k+29531)+1,i]+del_r_PQ_del_xyzP[27,2]*disp[3*(k+29531)+2,i]+del_r_PQ_del_xyzQ[27,0]*disp[3*(k+44218),i]+del_r_PQ_del_xyzQ[27,1]*disp[3*(k+44218)+1,i]+del_r_PQ_del_xyzQ[27,2]*disp[3*(k+44218)+2,i]+del_r_PQ_del_xyzP[28,0]*disp[3*(k+34169),i]+del_r_PQ_del_xyzP[28,1]*disp[3*(k+34169)+1,i]+del_r_PQ_del_xyzP[28,2]*disp[3*(k+34169)+2,i]+del_r_PQ_del_xyzQ[28,0]*disp[3*(k+38034),i]+del_r_PQ_del_xyzQ[28,1]*disp[3*(k+38034)+1,i]+del_r_PQ_del_xyzQ[28,2]*disp[3*(k+38034)+2,i]+del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
            
                                       
                    meansqure_r_PQ_cal = U_r_PQ_T1 * U_r_PQ_T1 / vT1[ nAm * modei + i]
                    meansqure_r_PQ.append(meansqure_r_PQ_cal)
                    r_PQ_eigvalues.append(vT1[nAm * modei + i])
                    r_PQ_markers.append(2)                        
  # Ur_PQT1(nAm*(modei-1)+i,hangi)=U_r_PQ_T1;
                    for ii in range(0,len(connectedresi)):
                        res_i = connectedresi[ii]
                        res_j = connectedresj[ii]
                        dist = distsave[ii]
                        perturbation[res_i, res_j] += (((postall[res_i, 0] - postall[res_j,0]) / dist) * U_r_PQ_T1* disp[3 * res_i, i] + ((postall[res_i, 1] - postall[res_j, 1])/ dist) * U_r_PQ_T1 * disp[3 * res_i + 1, i] + ((postall[res_i,2] - postall[res_j,2]) / dist) * U_r_PQ_T1 * disp[3 * res_i+2, i] - ((postall[res_i, 0] - postall[res_j, 0])/ dist)* U_r_PQ_T1 * disp[3 * res_j, i] - ((postall[res_i,1] - postall[res_j,1])/ dist) * U_r_PQ_T1 * disp[3 * res_j + 1, i] - ((postall[res_i, 2] - postall[res_j, 2]) / dist) * U_r_PQ_T1 * disp[3 * res_j+2, i]) / vT1[ nAm * modei + i] 
# #3_1.T2_1_2_3
    print('T2:')
    #Ur_PQT2=numpy.zeros([nT1,3],float) 
    for hangi in range(0,3):
        for modei in range(0,3):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M = numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((T2[j,hangi, 0] * T_M),eT2[0:3 * resn_mon,:])/ normT2_u
                disp2_nn = numpy.dot((T2[j,hangi, 1] * T_M),eT2[3 * resn_mon:3 * 2 * resn_mon,:])/ normT2_u
                disp3_nn = numpy.dot((T2[j,hangi, 2] * T_M),eT2[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT2_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
                #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            for i in range(0,nAm):
                if vT2[nAm * modei + i] > nonzerocutoff:
                    U_r_PQ_T2 = 0
                    #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                    for k in range(0,10):
                        U_r_PQ_T2 += del_r_PQ_del_xyzP[0,0]*disp[3*(k+157),i]+del_r_PQ_del_xyzP[0,1]*disp[3*(k+157)+1,i]+del_r_PQ_del_xyzP[0,2]*disp[3*(k+157)+2,i]+del_r_PQ_del_xyzQ[0,0]*disp[3*(k+16390),i]+del_r_PQ_del_xyzQ[0,1]*disp[3*(k+16390)+1,i]+del_r_PQ_del_xyzQ[0,2]*disp[3*(k+16390)+2,i]+del_r_PQ_del_xyzP[1,0]*disp[3*(k+930),i]+del_r_PQ_del_xyzP[1,1]*disp[3*(k+930)+1,i]+del_r_PQ_del_xyzP[1,2]*disp[3*(k+930)+2,i]+del_r_PQ_del_xyzQ[1,0]*disp[3*(k+31077),i]+del_r_PQ_del_xyzQ[1,1]*disp[3*(k+31077)+1,i]+del_r_PQ_del_xyzQ[1,2]*disp[3*(k+31077)+2,i]+del_r_PQ_del_xyzP[2,0]*disp[3*(k+1703),i]+del_r_PQ_del_xyzP[2,1]*disp[3*(k+1703)+1,i]+del_r_PQ_del_xyzP[2,2]*disp[3*(k+1703)+2,i]+del_r_PQ_del_xyzQ[2,0]*disp[3*(k+37261),i]+del_r_PQ_del_xyzQ[2,1]*disp[3*(k+37261)+1,i]+del_r_PQ_del_xyzQ[2,2]*disp[3*(k+37261)+2,i]+del_r_PQ_del_xyzP[3,0]*disp[3*(k+2476),i]+del_r_PQ_del_xyzP[3,1]*disp[3*(k+2476)+1,i]+del_r_PQ_del_xyzP[3,2]*disp[3*(k+2476)+2,i]+del_r_PQ_del_xyzQ[3,0]*disp[3*(k+24893),i]+del_r_PQ_del_xyzQ[3,1]*disp[3*(k+24893)+1,i]+del_r_PQ_del_xyzQ[3,2]*disp[3*(k+24893)+2,i]+del_r_PQ_del_xyzP[4,0]*disp[3*(k+3249),i]+del_r_PQ_del_xyzP[4,1]*disp[3*(k+3249)+1,i]+del_r_PQ_del_xyzP[4,2]*disp[3*(k+3249)+2,i]+del_r_PQ_del_xyzQ[4,0]*disp[3*(k+7114),i]+del_r_PQ_del_xyzQ[4,1]*disp[3*(k+7114)+1,i]+del_r_PQ_del_xyzQ[4,2]*disp[3*(k+7114)+2,i]+del_r_PQ_del_xyzP[5,0]*disp[3*(k+4022),i]+del_r_PQ_del_xyzP[5,1]*disp[3*(k+4022)+1,i]+del_r_PQ_del_xyzP[5,2]*disp[3*(k+4022)+2,i]+del_r_PQ_del_xyzQ[5,0]*disp[3*(k+24120),i]+del_r_PQ_del_xyzQ[5,1]*disp[3*(k+24120)+1,i]+del_r_PQ_del_xyzQ[5,2]*disp[3*(k+24120)+2,i]+del_r_PQ_del_xyzP[6,0]*disp[3*(k+4795),i]+del_r_PQ_del_xyzP[6,1]*disp[3*(k+4795)+1,i]+del_r_PQ_del_xyzP[6,2]*disp[3*(k+4795)+2,i]+del_r_PQ_del_xyzQ[6,0]*disp[3*(k+42672),i]+del_r_PQ_del_xyzQ[6,1]*disp[3*(k+42672)+1,i]+del_r_PQ_del_xyzQ[6,2]*disp[3*(k+42672)+2,i]+del_r_PQ_del_xyzP[7,0]*disp[3*(k+5568),i]+del_r_PQ_del_xyzP[7,1]*disp[3*(k+5568)+1,i]+del_r_PQ_del_xyzP[7,2]*disp[3*(k+5568)+2,i]+del_r_PQ_del_xyzQ[7,0]*disp[3*(k+41126),i]+del_r_PQ_del_xyzQ[7,1]*disp[3*(k+41126)+1,i]+del_r_PQ_del_xyzQ[7,2]*disp[3*(k+41126)+2,i]+del_r_PQ_del_xyzP[8,0]*disp[3*(k+6341),i]+del_r_PQ_del_xyzP[8,1]*disp[3*(k+6341)+1,i]+del_r_PQ_del_xyzP[8,2]*disp[3*(k+6341)+2,i]+del_r_PQ_del_xyzQ[8,0]*disp[3*(k+17163),i]+del_r_PQ_del_xyzQ[8,1]*disp[3*(k+17163)+1,i]+del_r_PQ_del_xyzQ[8,2]*disp[3*(k+17163)+2,i]+del_r_PQ_del_xyzP[9,0]*disp[3*(k+7887),i]+del_r_PQ_del_xyzP[9,1]*disp[3*(k+7887)+1,i]+del_r_PQ_del_xyzP[9,2]*disp[3*(k+7887)+2,i]+del_r_PQ_del_xyzQ[9,0]*disp[3*(k+27985),i]+del_r_PQ_del_xyzQ[9,1]*disp[3*(k+27985)+1,i]+del_r_PQ_del_xyzQ[9,2]*disp[3*(k+27985)+2,i]+del_r_PQ_del_xyzP[10,0]*disp[3*(k+8660),i]+del_r_PQ_del_xyzP[10,1]*disp[3*(k+8660)+1,i]+del_r_PQ_del_xyzP[10,2]*disp[3*(k+8660)+2,i]+del_r_PQ_del_xyzQ[10,0]*disp[3*(k+34942),i]+del_r_PQ_del_xyzQ[10,1]*disp[3*(k+34942)+1,i]+del_r_PQ_del_xyzQ[10,2]*disp[3*(k+34942)+2,i]+ del_r_PQ_del_xyzP[11,0]*disp[3*(k+9433),i]+del_r_PQ_del_xyzP[11,1]*disp[3*(k+9433)+1,i]+del_r_PQ_del_xyzP[11,2]*disp[3*(k+9433)+2,i]+del_r_PQ_del_xyzQ[11,0]*disp[3*(k+33396),i]+del_r_PQ_del_xyzQ[11,1]*disp[3*(k+33396)+1,i]+del_r_PQ_del_xyzQ[11,2]*disp[3*(k+33396)+2,i]+ del_r_PQ_del_xyzP[12,0]*disp[3*(k+10206),i]+del_r_PQ_del_xyzP[12,1]*disp[3*(k+10206)+1,i]+del_r_PQ_del_xyzP[12,2]*disp[3*(k+10206)+2,i]+del_r_PQ_del_xyzQ[12,0]*disp[3*(k+21028),i]+del_r_PQ_del_xyzQ[12,1]*disp[3*(k+21028)+1,i]+del_r_PQ_del_xyzQ[12,2]*disp[3*(k+21028)+2,i]+del_r_PQ_del_xyzP[13,0]*disp[3*(k+10979),i]+del_r_PQ_del_xyzP[13,1]*disp[3*(k+10979)+1,i]+del_r_PQ_del_xyzP[13,2]*disp[3*(k+10979)+2,i]+del_r_PQ_del_xyzQ[13,0]*disp[3*(k+14844),i]+del_r_PQ_del_xyzQ[13,1]*disp[3*(k+14844)+1,i]+del_r_PQ_del_xyzQ[13,2]*disp[3*(k+14844)+2,i]+del_r_PQ_del_xyzP[14,0]*disp[3*(k+11752),i]+del_r_PQ_del_xyzP[14,1]*disp[3*(k+11752)+1,i]+del_r_PQ_del_xyzP[14,2]*disp[3*(k+11752)+2,i]+del_r_PQ_del_xyzQ[14,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[14,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[14,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[15,0]*disp[3*(k+12525),i]+del_r_PQ_del_xyzP[15,1]*disp[3*(k+12525)+1,i]+del_r_PQ_del_xyzP[15,2]*disp[3*(k+12525)+2,i]+del_r_PQ_del_xyzQ[15,0]*disp[3*(k+38807),i]+del_r_PQ_del_xyzQ[15,1]*disp[3*(k+38807)+1,i]+del_r_PQ_del_xyzQ[15,2]*disp[3*(k+38807)+2,i]+del_r_PQ_del_xyzP[16,0]*disp[3*(k+13298),i]+del_r_PQ_del_xyzP[16,1]*disp[3*(k+13298)+1,i]+del_r_PQ_del_xyzP[16,2]*disp[3*(k+13298)+2,i]+del_r_PQ_del_xyzQ[16,0]*disp[3*(k+44991),i]+del_r_PQ_del_xyzQ[16,1]*disp[3*(k+44991)+1,i]+del_r_PQ_del_xyzQ[16,2]*disp[3*(k+44991)+2,i]+del_r_PQ_del_xyzP[17,0]*disp[3*(k+14071),i]+del_r_PQ_del_xyzP[17,1]*disp[3*(k+14071)+1,i]+del_r_PQ_del_xyzP[17,2]*disp[3*(k+14071)+2,i]+del_r_PQ_del_xyzQ[17,0]*disp[3*(k+28758),i]+del_r_PQ_del_xyzQ[17,1]*disp[3*(k+28758)+1,i]+del_r_PQ_del_xyzQ[17,2]*disp[3*(k+28758)+2,i]+ del_r_PQ_del_xyzP[18,0]*disp[3*(k+15617),i]+del_r_PQ_del_xyzP[18,1]*disp[3*(k+15617)+1,i]+del_r_PQ_del_xyzP[18,2]*disp[3*(k+15617)+2,i]+del_r_PQ_del_xyzQ[18,0]*disp[3*(k+31850),i]+del_r_PQ_del_xyzQ[18,1]*disp[3*(k+31850)+1,i]+del_r_PQ_del_xyzQ[18,2]*disp[3*(k+31850)+2,i]+del_r_PQ_del_xyzP[19,0]*disp[3*(k+17936),i]+del_r_PQ_del_xyzP[19,1]*disp[3*(k+17936)+1,i]+del_r_PQ_del_xyzP[19,2]*disp[3*(k+17936)+2,i]+del_r_PQ_del_xyzQ[19,0]*disp[3*(k+40353),i]+del_r_PQ_del_xyzQ[19,1]*disp[3*(k+40353)+1,i]+del_r_PQ_del_xyzQ[19,2]*disp[3*(k+40353)+2,i]+del_r_PQ_del_xyzP[20,0]*disp[3*(k+18709),i]+del_r_PQ_del_xyzP[20,1]*disp[3*(k+18709)+1,i]+del_r_PQ_del_xyzP[20,2]*disp[3*(k+18709)+2,i]+del_r_PQ_del_xyzQ[20,0]*disp[3*(k+22574),i]+del_r_PQ_del_xyzQ[20,1]*disp[3*(k+22574)+1,i]+del_r_PQ_del_xyzQ[20,2]*disp[3*(k+22574)+2,i]+ del_r_PQ_del_xyzP[21,0]*disp[3*(k+19482),i]+del_r_PQ_del_xyzP[21,1]*disp[3*(k+19482)+1,i]+del_r_PQ_del_xyzP[21,2]*disp[3*(k+19482)+2,i]+del_r_PQ_del_xyzQ[21,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[21,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[21,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[22,0]*disp[3*(k+21801),i]+del_r_PQ_del_xyzP[22,1]*disp[3*(k+21801)+1,i]+del_r_PQ_del_xyzP[22,2]*disp[3*(k+21801)+2,i]+del_r_PQ_del_xyzQ[22,0]*disp[3*(k+32623),i]+del_r_PQ_del_xyzQ[22,1]*disp[3*(k+32623)+1,i]+del_r_PQ_del_xyzQ[22,2]*disp[3*(k+32623)+2,i]+ del_r_PQ_del_xyzP[23,0]*disp[3*(k+23347),i]+del_r_PQ_del_xyzP[23,1]*disp[3*(k+23347)+1,i]+del_r_PQ_del_xyzP[23,2]*disp[3*(k+23347)+2,i]+del_r_PQ_del_xyzQ[23,0]*disp[3*(k+43445),i]+del_r_PQ_del_xyzQ[23,1]*disp[3*(k+43445)+1,i]+del_r_PQ_del_xyzQ[23,2]*disp[3*(k+43445)+2,i]+del_r_PQ_del_xyzP[24,0]*disp[3*(k+25666),i]+del_r_PQ_del_xyzP[24,1]*disp[3*(k+25666)+1,i]+del_r_PQ_del_xyzP[24,2]*disp[3*(k+25666)+2,i]+del_r_PQ_del_xyzQ[24,0]*disp[3*(k+36488),i]+del_r_PQ_del_xyzQ[24,1]*disp[3*(k+36488)+1,i]+del_r_PQ_del_xyzQ[24,2]*disp[3*(k+36488)+2,i]+del_r_PQ_del_xyzP[25,0]*disp[3*(k+26439),i]+del_r_PQ_del_xyzP[25,1]*disp[3*(k+26439)+1,i]+del_r_PQ_del_xyzP[25,2]*disp[3*(k+26439)+2,i]+del_r_PQ_del_xyzQ[25,0]*disp[3*(k+30304),i]+del_r_PQ_del_xyzQ[25,1]*disp[3*(k+30304)+1,i]+del_r_PQ_del_xyzQ[25,2]*disp[3*(k+30304)+2,i]+ del_r_PQ_del_xyzP[26,0]*disp[3*(k+27212),i]+del_r_PQ_del_xyzP[26,1]*disp[3*(k+27212)+1,i]+del_r_PQ_del_xyzP[26,2]*disp[3*(k+27212)+2,i]+del_r_PQ_del_xyzQ[26,0]*disp[3*(k+35715),i]+del_r_PQ_del_xyzQ[26,1]*disp[3*(k+35715)+1,i]+del_r_PQ_del_xyzQ[26,2]*disp[3*(k+35715)+2,i]+ del_r_PQ_del_xyzP[27,0]*disp[3*(k+29531),i]+del_r_PQ_del_xyzP[27,1]*disp[3*(k+29531)+1,i]+del_r_PQ_del_xyzP[27,2]*disp[3*(k+29531)+2,i]+del_r_PQ_del_xyzQ[27,0]*disp[3*(k+44218),i]+del_r_PQ_del_xyzQ[27,1]*disp[3*(k+44218)+1,i]+del_r_PQ_del_xyzQ[27,2]*disp[3*(k+44218)+2,i]+del_r_PQ_del_xyzP[28,0]*disp[3*(k+34169),i]+del_r_PQ_del_xyzP[28,1]*disp[3*(k+34169)+1,i]+del_r_PQ_del_xyzP[28,2]*disp[3*(k+34169)+2,i]+del_r_PQ_del_xyzQ[28,0]*disp[3*(k+38034),i]+del_r_PQ_del_xyzQ[28,1]*disp[3*(k+38034)+1,i]+del_r_PQ_del_xyzQ[28,2]*disp[3*(k+38034)+2,i]+del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
                        
                    meansqure_r_PQ_cal = U_r_PQ_T2 * U_r_PQ_T2 / vT2[nAm * modei + i]
                    meansqure_r_PQ.append(meansqure_r_PQ_cal)
                    r_PQ_eigvalues.append(vT2[nAm * modei + i])
                    r_PQ_markers.append(3)        
 
    # Ur_PQT2(nAm*(modei-1)+i,hangi)=U_r_PQ_T2;
    #calculate perturbation for each pairwise residues

                    for ii in range(0,len(connectedresi)):
                        res_i = connectedresi[ii]
                        res_j = connectedresj[ii]
                        dist = distsave[ii]
                        perturbation[res_i, res_j] += (((postall[res_i, 0] - postall[res_j,0]) / dist) * U_r_PQ_T2* disp[3 * res_i, i] + ((postall[res_i, 1] - postall[res_j, 1])/ dist) * U_r_PQ_T2 * disp[3 * res_i + 1, i] + ((postall[res_i,2] - postall[res_j,2]) / dist) * U_r_PQ_T2 * disp[3 * res_i+2, i] - ((postall[res_i, 0] - postall[res_j, 0])/ dist)* U_r_PQ_T2 * disp[3 * res_j, i] - ((postall[res_i,1] - postall[res_j,1])/ dist) * U_r_PQ_T2 * disp[3 * res_j + 1, i] - ((postall[res_i, 2] - postall[res_j, 2]) / dist) * U_r_PQ_T2 * disp[3 * res_j+2, i]) / vT2[ nAm * modei + i]
        
 
  #4_1.G_1_2_3_4
    print('G:')
    #Ur_PQG=numpy.zeros([nG,4],float)  
    for hangi in range(0,4):
        for modei in range(0,4):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((G[j,hangi, 0] * T_M),eG[0:3 * resn_mon,:])/ normG_u
                disp2_nn = numpy.dot((G[j,hangi, 1] * T_M),eG[3 * resn_mon:3 * 2 * resn_mon,:])/ normG_u
                disp3_nn = numpy.dot((G[j,hangi, 2] * T_M),eG[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normG_u
                disp4_nn = numpy.dot((G[j,hangi, 3] * T_M),eG[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normG_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
                #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
            for i in range(0,nAm): 
                if vG[nAm * modei + i] > nonzerocutoff:
                    U_r_PQ_G = 0
                    #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                    for k in range(0,10):
                        U_r_PQ_G += del_r_PQ_del_xyzP[0,0]*disp[3*(k+157),i]+del_r_PQ_del_xyzP[0,1]*disp[3*(k+157)+1,i]+del_r_PQ_del_xyzP[0,2]*disp[3*(k+157)+2,i]+del_r_PQ_del_xyzQ[0,0]*disp[3*(k+16390),i]+del_r_PQ_del_xyzQ[0,1]*disp[3*(k+16390)+1,i]+del_r_PQ_del_xyzQ[0,2]*disp[3*(k+16390)+2,i]+del_r_PQ_del_xyzP[1,0]*disp[3*(k+930),i]+del_r_PQ_del_xyzP[1,1]*disp[3*(k+930)+1,i]+del_r_PQ_del_xyzP[1,2]*disp[3*(k+930)+2,i]+del_r_PQ_del_xyzQ[1,0]*disp[3*(k+31077),i]+del_r_PQ_del_xyzQ[1,1]*disp[3*(k+31077)+1,i]+del_r_PQ_del_xyzQ[1,2]*disp[3*(k+31077)+2,i]+del_r_PQ_del_xyzP[2,0]*disp[3*(k+1703),i]+del_r_PQ_del_xyzP[2,1]*disp[3*(k+1703)+1,i]+del_r_PQ_del_xyzP[2,2]*disp[3*(k+1703)+2,i]+del_r_PQ_del_xyzQ[2,0]*disp[3*(k+37261),i]+del_r_PQ_del_xyzQ[2,1]*disp[3*(k+37261)+1,i]+del_r_PQ_del_xyzQ[2,2]*disp[3*(k+37261)+2,i]+del_r_PQ_del_xyzP[3,0]*disp[3*(k+2476),i]+del_r_PQ_del_xyzP[3,1]*disp[3*(k+2476)+1,i]+del_r_PQ_del_xyzP[3,2]*disp[3*(k+2476)+2,i]+del_r_PQ_del_xyzQ[3,0]*disp[3*(k+24893),i]+del_r_PQ_del_xyzQ[3,1]*disp[3*(k+24893)+1,i]+del_r_PQ_del_xyzQ[3,2]*disp[3*(k+24893)+2,i]+del_r_PQ_del_xyzP[4,0]*disp[3*(k+3249),i]+del_r_PQ_del_xyzP[4,1]*disp[3*(k+3249)+1,i]+del_r_PQ_del_xyzP[4,2]*disp[3*(k+3249)+2,i]+del_r_PQ_del_xyzQ[4,0]*disp[3*(k+7114),i]+del_r_PQ_del_xyzQ[4,1]*disp[3*(k+7114)+1,i]+del_r_PQ_del_xyzQ[4,2]*disp[3*(k+7114)+2,i]+del_r_PQ_del_xyzP[5,0]*disp[3*(k+4022),i]+del_r_PQ_del_xyzP[5,1]*disp[3*(k+4022)+1,i]+del_r_PQ_del_xyzP[5,2]*disp[3*(k+4022)+2,i]+del_r_PQ_del_xyzQ[5,0]*disp[3*(k+24120),i]+del_r_PQ_del_xyzQ[5,1]*disp[3*(k+24120)+1,i]+del_r_PQ_del_xyzQ[5,2]*disp[3*(k+24120)+2,i]+del_r_PQ_del_xyzP[6,0]*disp[3*(k+4795),i]+del_r_PQ_del_xyzP[6,1]*disp[3*(k+4795)+1,i]+del_r_PQ_del_xyzP[6,2]*disp[3*(k+4795)+2,i]+del_r_PQ_del_xyzQ[6,0]*disp[3*(k+42672),i]+del_r_PQ_del_xyzQ[6,1]*disp[3*(k+42672)+1,i]+del_r_PQ_del_xyzQ[6,2]*disp[3*(k+42672)+2,i]+del_r_PQ_del_xyzP[7,0]*disp[3*(k+5568),i]+del_r_PQ_del_xyzP[7,1]*disp[3*(k+5568)+1,i]+del_r_PQ_del_xyzP[7,2]*disp[3*(k+5568)+2,i]+del_r_PQ_del_xyzQ[7,0]*disp[3*(k+41126),i]+del_r_PQ_del_xyzQ[7,1]*disp[3*(k+41126)+1,i]+del_r_PQ_del_xyzQ[7,2]*disp[3*(k+41126)+2,i]+del_r_PQ_del_xyzP[8,0]*disp[3*(k+6341),i]+del_r_PQ_del_xyzP[8,1]*disp[3*(k+6341)+1,i]+del_r_PQ_del_xyzP[8,2]*disp[3*(k+6341)+2,i]+del_r_PQ_del_xyzQ[8,0]*disp[3*(k+17163),i]+del_r_PQ_del_xyzQ[8,1]*disp[3*(k+17163)+1,i]+del_r_PQ_del_xyzQ[8,2]*disp[3*(k+17163)+2,i]+del_r_PQ_del_xyzP[9,0]*disp[3*(k+7887),i]+del_r_PQ_del_xyzP[9,1]*disp[3*(k+7887)+1,i]+del_r_PQ_del_xyzP[9,2]*disp[3*(k+7887)+2,i]+del_r_PQ_del_xyzQ[9,0]*disp[3*(k+27985),i]+del_r_PQ_del_xyzQ[9,1]*disp[3*(k+27985)+1,i]+del_r_PQ_del_xyzQ[9,2]*disp[3*(k+27985)+2,i]+del_r_PQ_del_xyzP[10,0]*disp[3*(k+8660),i]+del_r_PQ_del_xyzP[10,1]*disp[3*(k+8660)+1,i]+del_r_PQ_del_xyzP[10,2]*disp[3*(k+8660)+2,i]+del_r_PQ_del_xyzQ[10,0]*disp[3*(k+34942),i]+del_r_PQ_del_xyzQ[10,1]*disp[3*(k+34942)+1,i]+del_r_PQ_del_xyzQ[10,2]*disp[3*(k+34942)+2,i]+ del_r_PQ_del_xyzP[11,0]*disp[3*(k+9433),i]+del_r_PQ_del_xyzP[11,1]*disp[3*(k+9433)+1,i]+del_r_PQ_del_xyzP[11,2]*disp[3*(k+9433)+2,i]+del_r_PQ_del_xyzQ[11,0]*disp[3*(k+33396),i]+del_r_PQ_del_xyzQ[11,1]*disp[3*(k+33396)+1,i]+del_r_PQ_del_xyzQ[11,2]*disp[3*(k+33396)+2,i]+ del_r_PQ_del_xyzP[12,0]*disp[3*(k+10206),i]+del_r_PQ_del_xyzP[12,1]*disp[3*(k+10206)+1,i]+del_r_PQ_del_xyzP[12,2]*disp[3*(k+10206)+2,i]+del_r_PQ_del_xyzQ[12,0]*disp[3*(k+21028),i]+del_r_PQ_del_xyzQ[12,1]*disp[3*(k+21028)+1,i]+del_r_PQ_del_xyzQ[12,2]*disp[3*(k+21028)+2,i]+del_r_PQ_del_xyzP[13,0]*disp[3*(k+10979),i]+del_r_PQ_del_xyzP[13,1]*disp[3*(k+10979)+1,i]+del_r_PQ_del_xyzP[13,2]*disp[3*(k+10979)+2,i]+del_r_PQ_del_xyzQ[13,0]*disp[3*(k+14844),i]+del_r_PQ_del_xyzQ[13,1]*disp[3*(k+14844)+1,i]+del_r_PQ_del_xyzQ[13,2]*disp[3*(k+14844)+2,i]+del_r_PQ_del_xyzP[14,0]*disp[3*(k+11752),i]+del_r_PQ_del_xyzP[14,1]*disp[3*(k+11752)+1,i]+del_r_PQ_del_xyzP[14,2]*disp[3*(k+11752)+2,i]+del_r_PQ_del_xyzQ[14,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[14,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[14,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[15,0]*disp[3*(k+12525),i]+del_r_PQ_del_xyzP[15,1]*disp[3*(k+12525)+1,i]+del_r_PQ_del_xyzP[15,2]*disp[3*(k+12525)+2,i]+del_r_PQ_del_xyzQ[15,0]*disp[3*(k+38807),i]+del_r_PQ_del_xyzQ[15,1]*disp[3*(k+38807)+1,i]+del_r_PQ_del_xyzQ[15,2]*disp[3*(k+38807)+2,i]+del_r_PQ_del_xyzP[16,0]*disp[3*(k+13298),i]+del_r_PQ_del_xyzP[16,1]*disp[3*(k+13298)+1,i]+del_r_PQ_del_xyzP[16,2]*disp[3*(k+13298)+2,i]+del_r_PQ_del_xyzQ[16,0]*disp[3*(k+44991),i]+del_r_PQ_del_xyzQ[16,1]*disp[3*(k+44991)+1,i]+del_r_PQ_del_xyzQ[16,2]*disp[3*(k+44991)+2,i]+del_r_PQ_del_xyzP[17,0]*disp[3*(k+14071),i]+del_r_PQ_del_xyzP[17,1]*disp[3*(k+14071)+1,i]+del_r_PQ_del_xyzP[17,2]*disp[3*(k+14071)+2,i]+del_r_PQ_del_xyzQ[17,0]*disp[3*(k+28758),i]+del_r_PQ_del_xyzQ[17,1]*disp[3*(k+28758)+1,i]+del_r_PQ_del_xyzQ[17,2]*disp[3*(k+28758)+2,i]+ del_r_PQ_del_xyzP[18,0]*disp[3*(k+15617),i]+del_r_PQ_del_xyzP[18,1]*disp[3*(k+15617)+1,i]+del_r_PQ_del_xyzP[18,2]*disp[3*(k+15617)+2,i]+del_r_PQ_del_xyzQ[18,0]*disp[3*(k+31850),i]+del_r_PQ_del_xyzQ[18,1]*disp[3*(k+31850)+1,i]+del_r_PQ_del_xyzQ[18,2]*disp[3*(k+31850)+2,i]+del_r_PQ_del_xyzP[19,0]*disp[3*(k+17936),i]+del_r_PQ_del_xyzP[19,1]*disp[3*(k+17936)+1,i]+del_r_PQ_del_xyzP[19,2]*disp[3*(k+17936)+2,i]+del_r_PQ_del_xyzQ[19,0]*disp[3*(k+40353),i]+del_r_PQ_del_xyzQ[19,1]*disp[3*(k+40353)+1,i]+del_r_PQ_del_xyzQ[19,2]*disp[3*(k+40353)+2,i]+del_r_PQ_del_xyzP[20,0]*disp[3*(k+18709),i]+del_r_PQ_del_xyzP[20,1]*disp[3*(k+18709)+1,i]+del_r_PQ_del_xyzP[20,2]*disp[3*(k+18709)+2,i]+del_r_PQ_del_xyzQ[20,0]*disp[3*(k+22574),i]+del_r_PQ_del_xyzQ[20,1]*disp[3*(k+22574)+1,i]+del_r_PQ_del_xyzQ[20,2]*disp[3*(k+22574)+2,i]+ del_r_PQ_del_xyzP[21,0]*disp[3*(k+19482),i]+del_r_PQ_del_xyzP[21,1]*disp[3*(k+19482)+1,i]+del_r_PQ_del_xyzP[21,2]*disp[3*(k+19482)+2,i]+del_r_PQ_del_xyzQ[21,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[21,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[21,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[22,0]*disp[3*(k+21801),i]+del_r_PQ_del_xyzP[22,1]*disp[3*(k+21801)+1,i]+del_r_PQ_del_xyzP[22,2]*disp[3*(k+21801)+2,i]+del_r_PQ_del_xyzQ[22,0]*disp[3*(k+32623),i]+del_r_PQ_del_xyzQ[22,1]*disp[3*(k+32623)+1,i]+del_r_PQ_del_xyzQ[22,2]*disp[3*(k+32623)+2,i]+ del_r_PQ_del_xyzP[23,0]*disp[3*(k+23347),i]+del_r_PQ_del_xyzP[23,1]*disp[3*(k+23347)+1,i]+del_r_PQ_del_xyzP[23,2]*disp[3*(k+23347)+2,i]+del_r_PQ_del_xyzQ[23,0]*disp[3*(k+43445),i]+del_r_PQ_del_xyzQ[23,1]*disp[3*(k+43445)+1,i]+del_r_PQ_del_xyzQ[23,2]*disp[3*(k+43445)+2,i]+del_r_PQ_del_xyzP[24,0]*disp[3*(k+25666),i]+del_r_PQ_del_xyzP[24,1]*disp[3*(k+25666)+1,i]+del_r_PQ_del_xyzP[24,2]*disp[3*(k+25666)+2,i]+del_r_PQ_del_xyzQ[24,0]*disp[3*(k+36488),i]+del_r_PQ_del_xyzQ[24,1]*disp[3*(k+36488)+1,i]+del_r_PQ_del_xyzQ[24,2]*disp[3*(k+36488)+2,i]+del_r_PQ_del_xyzP[25,0]*disp[3*(k+26439),i]+del_r_PQ_del_xyzP[25,1]*disp[3*(k+26439)+1,i]+del_r_PQ_del_xyzP[25,2]*disp[3*(k+26439)+2,i]+del_r_PQ_del_xyzQ[25,0]*disp[3*(k+30304),i]+del_r_PQ_del_xyzQ[25,1]*disp[3*(k+30304)+1,i]+del_r_PQ_del_xyzQ[25,2]*disp[3*(k+30304)+2,i]+ del_r_PQ_del_xyzP[26,0]*disp[3*(k+27212),i]+del_r_PQ_del_xyzP[26,1]*disp[3*(k+27212)+1,i]+del_r_PQ_del_xyzP[26,2]*disp[3*(k+27212)+2,i]+del_r_PQ_del_xyzQ[26,0]*disp[3*(k+35715),i]+del_r_PQ_del_xyzQ[26,1]*disp[3*(k+35715)+1,i]+del_r_PQ_del_xyzQ[26,2]*disp[3*(k+35715)+2,i]+ del_r_PQ_del_xyzP[27,0]*disp[3*(k+29531),i]+del_r_PQ_del_xyzP[27,1]*disp[3*(k+29531)+1,i]+del_r_PQ_del_xyzP[27,2]*disp[3*(k+29531)+2,i]+del_r_PQ_del_xyzQ[27,0]*disp[3*(k+44218),i]+del_r_PQ_del_xyzQ[27,1]*disp[3*(k+44218)+1,i]+del_r_PQ_del_xyzQ[27,2]*disp[3*(k+44218)+2,i]+del_r_PQ_del_xyzP[28,0]*disp[3*(k+34169),i]+del_r_PQ_del_xyzP[28,1]*disp[3*(k+34169)+1,i]+del_r_PQ_del_xyzP[28,2]*disp[3*(k+34169)+2,i]+del_r_PQ_del_xyzQ[28,0]*disp[3*(k+38034),i]+del_r_PQ_del_xyzQ[28,1]*disp[3*(k+38034)+1,i]+del_r_PQ_del_xyzQ[28,2]*disp[3*(k+38034)+2,i]+del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
           
                    meansqure_r_PQ_cal = U_r_PQ_G * U_r_PQ_G / vG[nAm * modei + i]
                    meansqure_r_PQ.append(meansqure_r_PQ_cal)
                    r_PQ_eigvalues.append(vG[nAm * modei + i])
                    r_PQ_markers.append(4)         
    # Ur_PQG(nAm*(modei-1)+i,hangi)=U_r_PQ_G;
    #calculate perturbation for each pairwise residues
                    for ii in range(0,len(connectedresi)):
                        res_i = connectedresi[ii]
                        res_j = connectedresj[ii]
                        dist = distsave[ii]
                        perturbation[res_i, res_j] += (((postall[res_i, 0] - postall[res_j,0]) / dist) * U_r_PQ_G* disp[3 * res_i, i] + ((postall[res_i, 1] - postall[res_j, 1])/ dist) * U_r_PQ_G * disp[3 * res_i + 1, i] + ((postall[res_i,2] - postall[res_j,2]) / dist) * U_r_PQ_G * disp[3 * res_i+2, i] - ((postall[res_i, 0] - postall[res_j, 0])/ dist)* U_r_PQ_G * disp[3 * res_j, i] - ((postall[res_i,1] - postall[res_j,1])/ dist) * U_r_PQ_G * disp[3 * res_j + 1, i] - ((postall[res_i, 2] - postall[res_j, 2]) / dist) * U_r_PQ_G * disp[3 * res_j+2, i]) / vG[ nAm * modei + i]
    
    print('H:')       
  #5_1.H_1_2_3_4_5

    #Ur_PQH=numpy.zeros([nH,5],float)  
    for hangi in range(0,5):
        for modei in range(0,5):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((H[j,hangi, 0] * T_M),eH[0:3 * resn_mon,:])/ normH_u
                disp2_nn = numpy.dot((H[j,hangi, 1] * T_M),eH[3 * resn_mon:3 * 2 * resn_mon,:])/ normH_u
                disp3_nn = numpy.dot((H[j,hangi, 2] * T_M),eH[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normH_u
                disp4_nn = numpy.dot((H[j,hangi, 3] * T_M),eH[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normH_u
                disp5_nn = numpy.dot((H[j,hangi, 4] * T_M),eH[3 * 4 * resn_mon:3 * 5 * resn_mon,:])/ normH_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp5_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
                #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            for i in range(0,nAm):
                if vH[nAm * modei + i] > nonzerocutoff:
                  U_r_PQ_H = 0
                    #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                  for k in range(0,10):
                        #U1,U2,U3,U4,U5,U6,U7,U8,U9,U10,U11,U12,U13,U14,U15,U16,U17,U18,U19,U20,U21,U22,U23,U24,U25,U26,U27,U28,U29,U30=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0  
                      U_r_PQ_H += del_r_PQ_del_xyzP[0,0]*disp[3*(k+157),i]+del_r_PQ_del_xyzP[0,1]*disp[3*(k+157)+1,i]+del_r_PQ_del_xyzP[0,2]*disp[3*(k+157)+2,i]+del_r_PQ_del_xyzQ[0,0]*disp[3*(k+16390),i]+del_r_PQ_del_xyzQ[0,1]*disp[3*(k+16390)+1,i]+del_r_PQ_del_xyzQ[0,2]*disp[3*(k+16390)+2,i]+del_r_PQ_del_xyzP[1,0]*disp[3*(k+930),i]+del_r_PQ_del_xyzP[1,1]*disp[3*(k+930)+1,i]+del_r_PQ_del_xyzP[1,2]*disp[3*(k+930)+2,i]+del_r_PQ_del_xyzQ[1,0]*disp[3*(k+31077),i]+del_r_PQ_del_xyzQ[1,1]*disp[3*(k+31077)+1,i]+del_r_PQ_del_xyzQ[1,2]*disp[3*(k+31077)+2,i]+del_r_PQ_del_xyzP[2,0]*disp[3*(k+1703),i]+del_r_PQ_del_xyzP[2,1]*disp[3*(k+1703)+1,i]+del_r_PQ_del_xyzP[2,2]*disp[3*(k+1703)+2,i]+del_r_PQ_del_xyzQ[2,0]*disp[3*(k+37261),i]+del_r_PQ_del_xyzQ[2,1]*disp[3*(k+37261)+1,i]+del_r_PQ_del_xyzQ[2,2]*disp[3*(k+37261)+2,i]+del_r_PQ_del_xyzP[3,0]*disp[3*(k+2476),i]+del_r_PQ_del_xyzP[3,1]*disp[3*(k+2476)+1,i]+del_r_PQ_del_xyzP[3,2]*disp[3*(k+2476)+2,i]+del_r_PQ_del_xyzQ[3,0]*disp[3*(k+24893),i]+del_r_PQ_del_xyzQ[3,1]*disp[3*(k+24893)+1,i]+del_r_PQ_del_xyzQ[3,2]*disp[3*(k+24893)+2,i]+del_r_PQ_del_xyzP[4,0]*disp[3*(k+3249),i]+del_r_PQ_del_xyzP[4,1]*disp[3*(k+3249)+1,i]+del_r_PQ_del_xyzP[4,2]*disp[3*(k+3249)+2,i]+del_r_PQ_del_xyzQ[4,0]*disp[3*(k+7114),i]+del_r_PQ_del_xyzQ[4,1]*disp[3*(k+7114)+1,i]+del_r_PQ_del_xyzQ[4,2]*disp[3*(k+7114)+2,i]+del_r_PQ_del_xyzP[5,0]*disp[3*(k+4022),i]+del_r_PQ_del_xyzP[5,1]*disp[3*(k+4022)+1,i]+del_r_PQ_del_xyzP[5,2]*disp[3*(k+4022)+2,i]+del_r_PQ_del_xyzQ[5,0]*disp[3*(k+24120),i]+del_r_PQ_del_xyzQ[5,1]*disp[3*(k+24120)+1,i]+del_r_PQ_del_xyzQ[5,2]*disp[3*(k+24120)+2,i]+del_r_PQ_del_xyzP[6,0]*disp[3*(k+4795),i]+del_r_PQ_del_xyzP[6,1]*disp[3*(k+4795)+1,i]+del_r_PQ_del_xyzP[6,2]*disp[3*(k+4795)+2,i]+del_r_PQ_del_xyzQ[6,0]*disp[3*(k+42672),i]+del_r_PQ_del_xyzQ[6,1]*disp[3*(k+42672)+1,i]+del_r_PQ_del_xyzQ[6,2]*disp[3*(k+42672)+2,i]+del_r_PQ_del_xyzP[7,0]*disp[3*(k+5568),i]+del_r_PQ_del_xyzP[7,1]*disp[3*(k+5568)+1,i]+del_r_PQ_del_xyzP[7,2]*disp[3*(k+5568)+2,i]+del_r_PQ_del_xyzQ[7,0]*disp[3*(k+41126),i]+del_r_PQ_del_xyzQ[7,1]*disp[3*(k+41126)+1,i]+del_r_PQ_del_xyzQ[7,2]*disp[3*(k+41126)+2,i]+del_r_PQ_del_xyzP[8,0]*disp[3*(k+6341),i]+del_r_PQ_del_xyzP[8,1]*disp[3*(k+6341)+1,i]+del_r_PQ_del_xyzP[8,2]*disp[3*(k+6341)+2,i]+del_r_PQ_del_xyzQ[8,0]*disp[3*(k+17163),i]+del_r_PQ_del_xyzQ[8,1]*disp[3*(k+17163)+1,i]+del_r_PQ_del_xyzQ[8,2]*disp[3*(k+17163)+2,i]+del_r_PQ_del_xyzP[9,0]*disp[3*(k+7887),i]+del_r_PQ_del_xyzP[9,1]*disp[3*(k+7887)+1,i]+del_r_PQ_del_xyzP[9,2]*disp[3*(k+7887)+2,i]+del_r_PQ_del_xyzQ[9,0]*disp[3*(k+27985),i]+del_r_PQ_del_xyzQ[9,1]*disp[3*(k+27985)+1,i]+del_r_PQ_del_xyzQ[9,2]*disp[3*(k+27985)+2,i]+del_r_PQ_del_xyzP[10,0]*disp[3*(k+8660),i]+del_r_PQ_del_xyzP[10,1]*disp[3*(k+8660)+1,i]+del_r_PQ_del_xyzP[10,2]*disp[3*(k+8660)+2,i]+del_r_PQ_del_xyzQ[10,0]*disp[3*(k+34942),i]+del_r_PQ_del_xyzQ[10,1]*disp[3*(k+34942)+1,i]+del_r_PQ_del_xyzQ[10,2]*disp[3*(k+34942)+2,i]+ del_r_PQ_del_xyzP[11,0]*disp[3*(k+9433),i]+del_r_PQ_del_xyzP[11,1]*disp[3*(k+9433)+1,i]+del_r_PQ_del_xyzP[11,2]*disp[3*(k+9433)+2,i]+del_r_PQ_del_xyzQ[11,0]*disp[3*(k+33396),i]+del_r_PQ_del_xyzQ[11,1]*disp[3*(k+33396)+1,i]+del_r_PQ_del_xyzQ[11,2]*disp[3*(k+33396)+2,i]+ del_r_PQ_del_xyzP[12,0]*disp[3*(k+10206),i]+del_r_PQ_del_xyzP[12,1]*disp[3*(k+10206)+1,i]+del_r_PQ_del_xyzP[12,2]*disp[3*(k+10206)+2,i]+del_r_PQ_del_xyzQ[12,0]*disp[3*(k+21028),i]+del_r_PQ_del_xyzQ[12,1]*disp[3*(k+21028)+1,i]+del_r_PQ_del_xyzQ[12,2]*disp[3*(k+21028)+2,i]+del_r_PQ_del_xyzP[13,0]*disp[3*(k+10979),i]+del_r_PQ_del_xyzP[13,1]*disp[3*(k+10979)+1,i]+del_r_PQ_del_xyzP[13,2]*disp[3*(k+10979)+2,i]+del_r_PQ_del_xyzQ[13,0]*disp[3*(k+14844),i]+del_r_PQ_del_xyzQ[13,1]*disp[3*(k+14844)+1,i]+del_r_PQ_del_xyzQ[13,2]*disp[3*(k+14844)+2,i]+del_r_PQ_del_xyzP[14,0]*disp[3*(k+11752),i]+del_r_PQ_del_xyzP[14,1]*disp[3*(k+11752)+1,i]+del_r_PQ_del_xyzP[14,2]*disp[3*(k+11752)+2,i]+del_r_PQ_del_xyzQ[14,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[14,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[14,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[15,0]*disp[3*(k+12525),i]+del_r_PQ_del_xyzP[15,1]*disp[3*(k+12525)+1,i]+del_r_PQ_del_xyzP[15,2]*disp[3*(k+12525)+2,i]+del_r_PQ_del_xyzQ[15,0]*disp[3*(k+38807),i]+del_r_PQ_del_xyzQ[15,1]*disp[3*(k+38807)+1,i]+del_r_PQ_del_xyzQ[15,2]*disp[3*(k+38807)+2,i]+del_r_PQ_del_xyzP[16,0]*disp[3*(k+13298),i]+del_r_PQ_del_xyzP[16,1]*disp[3*(k+13298)+1,i]+del_r_PQ_del_xyzP[16,2]*disp[3*(k+13298)+2,i]+del_r_PQ_del_xyzQ[16,0]*disp[3*(k+44991),i]+del_r_PQ_del_xyzQ[16,1]*disp[3*(k+44991)+1,i]+del_r_PQ_del_xyzQ[16,2]*disp[3*(k+44991)+2,i]+del_r_PQ_del_xyzP[17,0]*disp[3*(k+14071),i]+del_r_PQ_del_xyzP[17,1]*disp[3*(k+14071)+1,i]+del_r_PQ_del_xyzP[17,2]*disp[3*(k+14071)+2,i]+del_r_PQ_del_xyzQ[17,0]*disp[3*(k+28758),i]+del_r_PQ_del_xyzQ[17,1]*disp[3*(k+28758)+1,i]+del_r_PQ_del_xyzQ[17,2]*disp[3*(k+28758)+2,i]+ del_r_PQ_del_xyzP[18,0]*disp[3*(k+15617),i]+del_r_PQ_del_xyzP[18,1]*disp[3*(k+15617)+1,i]+del_r_PQ_del_xyzP[18,2]*disp[3*(k+15617)+2,i]+del_r_PQ_del_xyzQ[18,0]*disp[3*(k+31850),i]+del_r_PQ_del_xyzQ[18,1]*disp[3*(k+31850)+1,i]+del_r_PQ_del_xyzQ[18,2]*disp[3*(k+31850)+2,i]+del_r_PQ_del_xyzP[19,0]*disp[3*(k+17936),i]+del_r_PQ_del_xyzP[19,1]*disp[3*(k+17936)+1,i]+del_r_PQ_del_xyzP[19,2]*disp[3*(k+17936)+2,i]+del_r_PQ_del_xyzQ[19,0]*disp[3*(k+40353),i]+del_r_PQ_del_xyzQ[19,1]*disp[3*(k+40353)+1,i]+del_r_PQ_del_xyzQ[19,2]*disp[3*(k+40353)+2,i]+del_r_PQ_del_xyzP[20,0]*disp[3*(k+18709),i]+del_r_PQ_del_xyzP[20,1]*disp[3*(k+18709)+1,i]+del_r_PQ_del_xyzP[20,2]*disp[3*(k+18709)+2,i]+del_r_PQ_del_xyzQ[20,0]*disp[3*(k+22574),i]+del_r_PQ_del_xyzQ[20,1]*disp[3*(k+22574)+1,i]+del_r_PQ_del_xyzQ[20,2]*disp[3*(k+22574)+2,i]+ del_r_PQ_del_xyzP[21,0]*disp[3*(k+19482),i]+del_r_PQ_del_xyzP[21,1]*disp[3*(k+19482)+1,i]+del_r_PQ_del_xyzP[21,2]*disp[3*(k+19482)+2,i]+del_r_PQ_del_xyzQ[21,0]*disp[3*(k+39580),i]+del_r_PQ_del_xyzQ[21,1]*disp[3*(k+39580)+1,i]+del_r_PQ_del_xyzQ[21,2]*disp[3*(k+39580)+2,i]+ del_r_PQ_del_xyzP[22,0]*disp[3*(k+21801),i]+del_r_PQ_del_xyzP[22,1]*disp[3*(k+21801)+1,i]+del_r_PQ_del_xyzP[22,2]*disp[3*(k+21801)+2,i]+del_r_PQ_del_xyzQ[22,0]*disp[3*(k+32623),i]+del_r_PQ_del_xyzQ[22,1]*disp[3*(k+32623)+1,i]+del_r_PQ_del_xyzQ[22,2]*disp[3*(k+32623)+2,i]+ del_r_PQ_del_xyzP[23,0]*disp[3*(k+23347),i]+del_r_PQ_del_xyzP[23,1]*disp[3*(k+23347)+1,i]+del_r_PQ_del_xyzP[23,2]*disp[3*(k+23347)+2,i]+del_r_PQ_del_xyzQ[23,0]*disp[3*(k+43445),i]+del_r_PQ_del_xyzQ[23,1]*disp[3*(k+43445)+1,i]+del_r_PQ_del_xyzQ[23,2]*disp[3*(k+43445)+2,i]+del_r_PQ_del_xyzP[24,0]*disp[3*(k+25666),i]+del_r_PQ_del_xyzP[24,1]*disp[3*(k+25666)+1,i]+del_r_PQ_del_xyzP[24,2]*disp[3*(k+25666)+2,i]+del_r_PQ_del_xyzQ[24,0]*disp[3*(k+36488),i]+del_r_PQ_del_xyzQ[24,1]*disp[3*(k+36488)+1,i]+del_r_PQ_del_xyzQ[24,2]*disp[3*(k+36488)+2,i]+del_r_PQ_del_xyzP[25,0]*disp[3*(k+26439),i]+del_r_PQ_del_xyzP[25,1]*disp[3*(k+26439)+1,i]+del_r_PQ_del_xyzP[25,2]*disp[3*(k+26439)+2,i]+del_r_PQ_del_xyzQ[25,0]*disp[3*(k+30304),i]+del_r_PQ_del_xyzQ[25,1]*disp[3*(k+30304)+1,i]+del_r_PQ_del_xyzQ[25,2]*disp[3*(k+30304)+2,i]+ del_r_PQ_del_xyzP[26,0]*disp[3*(k+27212),i]+del_r_PQ_del_xyzP[26,1]*disp[3*(k+27212)+1,i]+del_r_PQ_del_xyzP[26,2]*disp[3*(k+27212)+2,i]+del_r_PQ_del_xyzQ[26,0]*disp[3*(k+35715),i]+del_r_PQ_del_xyzQ[26,1]*disp[3*(k+35715)+1,i]+del_r_PQ_del_xyzQ[26,2]*disp[3*(k+35715)+2,i]+ del_r_PQ_del_xyzP[27,0]*disp[3*(k+29531),i]+del_r_PQ_del_xyzP[27,1]*disp[3*(k+29531)+1,i]+del_r_PQ_del_xyzP[27,2]*disp[3*(k+29531)+2,i]+del_r_PQ_del_xyzQ[27,0]*disp[3*(k+44218),i]+del_r_PQ_del_xyzQ[27,1]*disp[3*(k+44218)+1,i]+del_r_PQ_del_xyzQ[27,2]*disp[3*(k+44218)+2,i]+del_r_PQ_del_xyzP[28,0]*disp[3*(k+34169),i]+del_r_PQ_del_xyzP[28,1]*disp[3*(k+34169)+1,i]+del_r_PQ_del_xyzP[28,2]*disp[3*(k+34169)+2,i]+del_r_PQ_del_xyzQ[28,0]*disp[3*(k+38034),i]+del_r_PQ_del_xyzQ[28,1]*disp[3*(k+38034)+1,i]+del_r_PQ_del_xyzQ[28,2]*disp[3*(k+38034)+2,i]+del_r_PQ_del_xyzP[29,0]*disp[3*(k+41899),i]+del_r_PQ_del_xyzP[29,1]*disp[3*(k+41899)+1,i]+del_r_PQ_del_xyzP[29,2]*disp[3*(k+41899)+2,i]+del_r_PQ_del_xyzQ[29,0]*disp[3*(k+45764),i]+del_r_PQ_del_xyzQ[29,1]*disp[3*(k+45764)+1,i]+del_r_PQ_del_xyzQ[29,2]*disp[3*(k+45764)+2,i]
           
                  meansqure_r_PQ_cal = U_r_PQ_H * U_r_PQ_H / vH[nAm * modei + i]
                  meansqure_r_PQ.append(meansqure_r_PQ_cal)
                  r_PQ_eigvalues.append(vH[nAm * modei + i])
                  r_PQ_markers.append(5)
      #Ur_PQH(nAm*(modei-1)+i,hangi)=U_r_PQ_H;
    #calculate perturbation for each pairwise residues
                  for ii in range(0,len(connectedresi)):
                      res_i = connectedresi[ii]
                      res_j = connectedresj[ii]
                      dist = distsave[ii]
                      perturbation[res_i, res_j] += (((postall[res_i, 0] - postall[res_j,0]) / dist) * U_r_PQ_H* disp[3 * res_i, i] + ((postall[res_i, 1] - postall[res_j, 1])/ dist) * U_r_PQ_G * disp[3 * res_i + 1, i] + ((postall[res_i,2] - postall[res_j,2]) / dist) * U_r_PQ_H * disp[3 * res_i+2, i] - ((postall[res_i, 0] - postall[res_j, 0])/ dist)* U_r_PQ_H * disp[3 * res_j, i] - ((postall[res_i,1] - postall[res_j,1])/ dist) * U_r_PQ_H * disp[3 * res_j + 1, i] - ((postall[res_i, 2] - postall[res_j, 2]) / dist) * U_r_PQ_H * disp[3 * res_j+2, i]) / vH[ nAm * modei + i]
           
    numpy.save('measqure_r_PQdat.npy', meansqure_r_PQ)
    numpy.save('r_PQ_eigvaluesdat.npy', r_PQ_eigvalues)
    numpy.save('r_PQ_markersdat.npy', r_PQ_markers)
    numpy.save('perturbationdat.npy', perturbation)
    del r_PQ_eigvalues,r_PQ_markers
    perturbation=perturbation*perturbation
    perturbation_sum = numpy.sum(perturbation,axis=1)
    numpy.save('perturbationsumdat.npy',perturbation_sum)
    resnn =numpy.linspace(1,resn_mon,resn_mon)#figure[23]
    plt.plot(resnn,perturbation_sum)
    plt.savefig('perturba.png')
    plt.show()  
#Next is calculation of the mean-square fluctuation of r_PQ for each mode
    perturbation_sum=numpy.load('perturbationsumdat.npy')    
    meansqure_r_PQ=numpy.load('measqure_r_PQdat.npy')    
    countnum =-1
    countk =-1
    global Ueig 
    Ueig = numpy.zeros(shape=(3*n2,10))
    ms_r_PQ =[]
    rgsort=sorted(meansqure_r_PQ,reverse=True)
    #insort=numpy.argsort(-numpy.array(rgsort))
    insort=(-numpy.array(meansqure_r_PQ)).argsort()
    vall=numpy.array(vall)
    vall2=vall[vall>nonzerocutoff]
    del vall,vall2,rgsort
    
    print('am:')
    disp =numpy.zeros(shape=(3 * n2, nAm))
    for j in range(0,60):
        T_M =numpy.kron(Digmatrix, R[j,:,:])
        disp1_nn = numpy.dot((Am[j,0,0] * T_M),eAm)/ normAm_u
        disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn
    for i in range(0,nAm):
        if vAm[i] > nonzerocutoff:
            countnum+=1
            if countnum == insort[0] or countnum == insort[1] or countnum == insort[2] or countnum == insort[3] or countnum == insort[4] or countnum == insort[5] or countnum == insort[6] or countnum == insort[7] or countnum == insort[8] or countnum == insort[9]:
                countk+=1
                Ueig[:,countk]=disp[:, i]
                ms_r_PQ.extend([countk,meansqure_r_PQ[countnum]])
    
    print('t1:')
    for hangi in range(0,3):
        for modei in range(0,3):
            disp = numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((T1[j,hangi,0] * T_M),eT1[0:3 * resn_mon,:])/ normT1_u
                disp2_nn = numpy.dot((T1[j,hangi,1] * T_M),eT1[3 * resn_mon:3 * 2 * resn_mon,:])/ normT1_u
                disp3_nn = numpy.dot((T1[j,hangi,2] * T_M),eT1[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT1_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)) :int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
            for i in range(0,nAm):
                if vT1[ nAm * modei + i] > nonzerocutoff:
                    countnum+=1
                    if countnum == insort[0] or countnum == insort[1] or countnum == insort[2] or countnum == insort[3] or countnum == insort[4] or countnum == insort[5] or countnum == insort[6] or countnum == insort[7] or countnum == insort[8] or countnum == insort[9]:
                        countk+=1
                        Ueig[:, countk]=disp[:, nAm * modei + i]
                        ms_r_PQ.extend([countk,meansqure_r_PQ[countnum]])
    
    print('t2:')
    for hangi in range(0,3):
        for modei in range(0,3):
            disp = numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((T2[j,hangi, 0] * T_M),eT2[0:3 * resn_mon,:])/ normT2_u
                disp2_nn = numpy.dot((T2[j,hangi, 1] * T_M),eT2[3 * resn_mon:3 * 2 * resn_mon,:])/ normT2_u
                disp3_nn = numpy.dot((T2[j,hangi, 2] * T_M),eT2[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT2_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
            for i in range(0,nAm):
                if vT2[nAm * modei + i] > nonzerocutoff:
                    countnum+=1
                    if countnum == insort[0] or countnum == insort[1] or countnum == insort[2] or countnum == insort[3] or countnum == insort[4] or countnum == insort[5] or countnum == insort[6] or countnum == insort[7] or countnum == insort[8] or countnum == insort[9]:
                        countk+=1
                        Ueig[:, countk]=disp[:, nAm * modei + i]
                        ms_r_PQ.extend([countk,meansqure_r_PQ[countnum]])
    
    print('g:')
    for hangi in range(0,4):
        for modei in range(0,4):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((G[j,hangi, 0] * T_M),eG[0:3 * resn_mon,:])/ normG_u
                disp2_nn = numpy.dot((G[j,hangi, 1] * T_M),eG[3 * resn_mon:3 * 2 * resn_mon,:])/ normG_u
                disp3_nn = numpy.dot((G[j,hangi, 2] * T_M),eG[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normG_u
                disp4_nn = numpy.dot((G[j,hangi, 3] * T_M),eG[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normG_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
            for i in range(0,nAm):
                if vG[nAm * modei + i] > nonzerocutoff:
                    countnum+=1
                    if countnum == insort[0] or countnum == insort[1] or countnum == insort[2] or countnum == insort[3] or countnum == insort[4] or countnum == insort[5] or countnum == insort[6] or countnum == insort[7] or countnum == insort[8] or countnum == insort[9]:
                        countk+=1
                        Ueig[:, countk]=disp[:, nAm * modei + i]
                        ms_r_PQ.extend([countk,meansqure_r_PQ[countnum]])
    
    print('h:')
    for hangi in range(0,5):
        for modei in range(0,5):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((H[j,hangi, 0] * T_M),eH[0:3 * resn_mon,:])/ normH_u
                disp2_nn = numpy.dot((H[j,hangi, 1] * T_M),eH[3 * resn_mon:3 * 2 * resn_mon,:])/ normH_u
                disp3_nn = numpy.dot((H[j,hangi, 2] * T_M),eH[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normH_u
                disp4_nn = numpy.dot((H[j,hangi, 3] * T_M),eH[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normH_u
                disp5_nn = numpy.dot((H[j,hangi, 4] * T_M),eH[3 * 4 * resn_mon:3 * 5 * resn_mon,:])/ normH_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp5_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
            for i in range(0,nAm):
                if vH[nAm * modei + i] > nonzerocutoff:
                    countnum+=1
                    if countnum == insort[0] or countnum == insort[1] or countnum == insort[2] or countnum == insort[3] or countnum == insort[4] or countnum == insort[5] or countnum == insort[6] or countnum == insort[7] or countnum == insort[8] or countnum == insort[9]:
                        countk+=1
                        Ueig[:, countk]=disp[:, nAm * modei + i]
                        ms_r_PQ.extend([countk,meansqure_r_PQ[countnum]])
    numpy.save('countkdat.npy', countk)
    numpy.save('countnumdat.npy', countnum)
    numpy.save('Ueigdat.npy', Ueig)
    numpy.save('ms_r_PQdat.npy', ms_r_PQ)

# #calculate B-factors%%%%%%%%%

    bfactoradd_group=numpy.zeros(shape=(60,resn_mon))
    bfactorx_group=numpy.zeros(shape=(60,resn_mon))
    bfactory_group=numpy.zeros(shape=(60,resn_mon))
    bfactorz_group=numpy.zeros(shape=(60,resn_mon))
    #B_A =int(op[j,0])
    #print(B_A)
#Am
    print('BAm:')
    disp = numpy.zeros(shape=(3*n2,nAm))
    for j in range(0,60):
        T_M = numpy.kron(Digmatrix,R[j,:,:])
    disp_nn= numpy.dot((Am[j,0,0] * T_M),eAm)/normAm_u #normAm_u is 1; see the first line of the code.
  #normalize the disp_nn
    disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp_nn
      
    for k in range(0,resn_mon):
        for i in range(0,nAm):
            if vAm[i] > 0.02:  
               
                bfactorx_group[int(op[j,0]),k] += disp[3*k,i]*disp[3*k,i] /vAm[i]
                bfactory_group[int(op[j,0]),k] += disp[3*k+1,i]*disp[3*k+1,i] /vAm[i]
                bfactorz_group[int(op[j,0]),k] += disp[3*k+2,i]*disp[3*k+2,i] /vAm[i]
 
             
#T1
    print('BT1:')
    for hangi in range(0,3):
        for modei in range(0,3):
            disp = numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((T1[j,hangi,0] * T_M),eT1[0:3 * resn_mon,:])/ normT1_u
                disp2_nn = numpy.dot((T1[j,hangi,1] * T_M),eT1[3 * resn_mon:3 * 2 * resn_mon,:])/ normT1_u
                disp3_nn = numpy.dot((T1[j,hangi,2] * T_M),eT1[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT1_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)) :int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
               
            for k in range(0,resn_mon):
                for i in range(0,nAm):
                    if vT1[ nAm * modei + i] > 0.02:
                       
                        bfactorx_group[int(op[j,0]),k] += disp[3*k,i]*disp[3*k,i]/vT1[ nAm * modei + i]
                        bfactory_group[int(op[j,0]),k] += disp[3*k+1,i]*disp[3*k+1,i]/vT1[ nAm * modei + i]
                        bfactorz_group[int(op[j,0]),k] += disp[3*k+2,i]*disp[3*k+2,i]/vT1[ nAm * modei + i]
 
#T2  
    print('BT2:')
    for hangi in range(0,3):
        for modei in range(0,3):
            disp = numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((T2[j,hangi, 0] * T_M),eT2[0:3 * resn_mon,:])/ normT2_u
                disp2_nn = numpy.dot((T2[j,hangi, 1] * T_M),eT2[3 * resn_mon:3 * 2 * resn_mon,:])/ normT2_u
                disp3_nn = numpy.dot((T2[j,hangi, 2] * T_M),eT2[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normT2_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
             
            for k in range(0,resn_mon):
                for i in range(0,nAm):
                    if vT2[nAm * modei + i] > 0.02:
                       
                        bfactorx_group[int(op[j,0]),k] += disp[3*k,i]*disp[3*k,i]/vT2[nAm * modei + i]
                        bfactory_group[int(op[j,0]),k] += disp[3*k+1,i]*disp[3*k+1,i]/vT2[nAm * modei + i]
                        bfactorz_group[int(op[j,0]),k] += disp[3*k+2,i]*disp[3*k+2,i]/vT2[nAm * modei + i]
       
#G
    print('BG:')
    for hangi in range(0,4):
        for modei in range(0,4):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((G[j,hangi, 0] * T_M),eG[0:3 * resn_mon,:])/ normG_u
                disp2_nn = numpy.dot((G[j,hangi, 1] * T_M),eG[3 * resn_mon:3 * 2 * resn_mon,:])/ normG_u
                disp3_nn = numpy.dot((G[j,hangi, 2] * T_M),eG[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normG_u
                disp4_nn = numpy.dot((G[j,hangi, 3] * T_M),eG[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normG_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
          
            for k in range(0,resn_mon):
                for i in range(0,nAm):
                    if vG[nAm * modei + i] >  0.02:
                       
                        bfactorx_group[int(op[j,0]),k] += disp[3*k,i]*disp[3*k,i]/ vG[nAm * modei + i]
                        bfactory_group[int(op[j,0]),k] += disp[3*k+1,i]*disp[3*k+1,i]/ vG[nAm * modei + i]
                        bfactorz_group[int(op[j,0]),k] += disp[3*k+2,i]*disp[3*k+2,i]/ vG[nAm * modei + i]
#H  
    print('BH:')
    for hangi in range(0,5):
        for modei in range(0,5):
            disp =numpy.zeros(shape=(3 * n2, nAm))
            for j in range(0,60):
                T_M =numpy.kron(Digmatrix, R[j,:,:])
                disp1_nn = numpy.dot((H[j,hangi, 0] * T_M),eH[0:3 * resn_mon,:])/ normH_u
                disp2_nn = numpy.dot((H[j,hangi, 1] * T_M),eH[3 * resn_mon:3 * 2 * resn_mon,:])/ normH_u
                disp3_nn = numpy.dot((H[j,hangi, 2] * T_M),eH[3 * 2 * resn_mon:3 * 3 * resn_mon,:])/ normH_u
                disp4_nn = numpy.dot((H[j,hangi, 3] * T_M),eH[3 * 3 * resn_mon:3 * 4 * resn_mon,:])/ normH_u
                disp5_nn = numpy.dot((H[j,hangi, 4] * T_M),eH[3 * 4 * resn_mon:3 * 5 * resn_mon,:])/ normH_u
                disp[int(3 * ((op[j,0] - 1) * resn_mon)):int(3 * op[j,0] * resn_mon),:]=disp1_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp2_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp3_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp4_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]+disp5_nn[0: 3 * resn_mon, nAm * modei: nAm * (modei+1)]
                 
            for k in range(0,resn_mon):
                for i in range(0,nAm):
                    if vH[nAm * modei + i]> 0.02: 
                       
                        bfactorx_group[int(op[j,0]),k] += disp[3*k,i]*disp[3*k,i]/vH[nAm * modei + i]
                        bfactory_group[int(op[j,0]),k] += disp[3*k+1,i]*disp[3*k+1,i]/vH[nAm * modei + i]
                        bfactorz_group[int(op[j,0]),k] += disp[3*k+2,i]*disp[3*k+2,i]/vH[nAm * modei + i]
                                            
               
                bfactoradd_group[int(op[j,0]),:]=bfactorx_group[int(op[j,0]),:]+bfactory_group[int(op[j,0]),:]+bfactorz_group[int(op[j,0]),:]
              
                numpy.save('bfactoradd_group[op[%s,0],:]_dat.npy'%str(j),bfactoradd_group[int(op[j,0]),:])

    return perturbation_sum,ms_r_PQ,Ueig

   



