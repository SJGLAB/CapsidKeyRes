# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:34:07 2022

@author: hp
"""

# -*- coding: utf-8 -*-
import numpy
#import pandas
#import torch
import rotationmatrix02

pi=3.1415926 

def transformMatrix():

    a0=0
# transformMatrix03.m:2
    a1=1
# transformMatrix03.m:3
    a2=0.1
# transformMatrix03.m:4
    a3=0.2
# transformMatrix03.m:5
    a4=0.4
# transformMatrix03.m:6
    a5=0.5
# transformMatrix03.m:7
    a6=0.6
# transformMatrix03.m:8
    a7=(numpy.sqrt(5) - 2) / 5
# transformMatrix03.m:9
    a8=(5 - numpy.dot(2,numpy.sqrt(5))) / 10
# transformMatrix03.m:10
    a9=(numpy.dot(3,numpy.sqrt(5)) - 5) / 20
# transformMatrix03.m:11
    a10=((numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 4) - 1 / 2
# transformMatrix03.m:12
    a11=(numpy.sqrt(5) - 1) / 10
# transformMatrix03.m:13
    a12=(5 - numpy.sqrt(5)) / 20
# transformMatrix03.m:14
    a13=(numpy.sqrt(5 - numpy.dot(2,numpy.sqrt(5)))) / 5
# transformMatrix03.m:15
    a14=(numpy.sqrt((5 - numpy.dot(2,numpy.sqrt(5))) / 5)) / 2
# transformMatrix03.m:16
    a15=numpy.dot(3,(numpy.sqrt(5) - 1)) / 20
# transformMatrix03.m:17
    a16=numpy.dot(numpy.sqrt(3),(numpy.sqrt(5) - 1)) / 10
# transformMatrix03.m:18
    a17=numpy.sqrt(5) / 10
# transformMatrix03.m:19
    a18=(numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:20
    a19=(numpy.sqrt((5 - numpy.sqrt(5)) / 10)) / 2
# transformMatrix03.m:21
    a20=(5 - numpy.sqrt(5)) / 10
# transformMatrix03.m:22
    a21=(numpy.sqrt(5) - 1) / 4
# transformMatrix03.m:23
    a22=(numpy.sqrt(5) + 1) / 10
# transformMatrix03.m:24
    a23=numpy.dot(3,numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 20
# transformMatrix03.m:25
    a24=(5 + numpy.sqrt(5)) / 20
# transformMatrix03.m:26
    a25=numpy.sqrt(10 + numpy.dot(2,numpy.sqrt(5))) / 10
# transformMatrix03.m:27
    a26=numpy.dot(numpy.sqrt(3),numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:28
    a27=(numpy.sqrt((5 + numpy.sqrt(5)) / 10)) / 2
# transformMatrix03.m:29
    a28=numpy.sqrt(5) / 5
# transformMatrix03.m:30
    a29=(numpy.sqrt(25 - numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:31
    a30=numpy.dot(3,(numpy.sqrt(5) + 1)) / 20
# transformMatrix03.m:32
    a31=numpy.sqrt((5 - numpy.sqrt(5)) / 10)
# transformMatrix03.m:33
    a32=(numpy.sqrt(25 + numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:34
    a33=numpy.dot(numpy.sqrt(3),(numpy.sqrt(5) + 1)) / 10
# transformMatrix03.m:35
    a34=numpy.dot(3,(numpy.sqrt(10 + numpy.dot(2,numpy.sqrt(5))))) / 20
# transformMatrix03.m:36
    a35=(numpy.dot(3,numpy.sqrt(5)) + 5) / 20
# transformMatrix03.m:37
    a36=(numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 4
# transformMatrix03.m:38
    a37=(numpy.sqrt(5 + numpy.dot(2,numpy.sqrt(5)))) / 5
# transformMatrix03.m:39
    a38=(15 - numpy.sqrt(5)) / 20
# transformMatrix03.m:40
    a39=numpy.dot(numpy.sqrt(3),numpy.sqrt(10 + numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:41
    a40=numpy.dot(3,numpy.sqrt(5)) / 10
# transformMatrix03.m:42
    a41=(numpy.sqrt((5 + numpy.dot(2,numpy.sqrt(5))) / 5)) / 2
# transformMatrix03.m:43
    a42=numpy.dot(2,numpy.sqrt(3)) / 5
# transformMatrix03.m:44
    a43=(5 + numpy.sqrt(5)) / 10
# transformMatrix03.m:45
    a44=numpy.sqrt(10 + numpy.dot(2,numpy.sqrt(5))) / 5
# transformMatrix03.m:46
    a45=(numpy.dot(3,numpy.sqrt(5)) + 1) / 10
# transformMatrix03.m:47
    a46=(numpy.sqrt(5) + 1) / 4
# transformMatrix03.m:48
    a47=(numpy.sqrt(5) + 2) / 5
# transformMatrix03.m:49
    a48=numpy.sqrt((5 + numpy.sqrt(5)) / 10)
# transformMatrix03.m:50
    a49=(15 + numpy.sqrt(5)) / 20
# transformMatrix03.m:51
    a50=numpy.dot(2,numpy.sqrt(5)) / 5
# transformMatrix03.m:52
    a51=(5 + numpy.dot(2,numpy.sqrt(5))) / 10
# transformMatrix03.m:53
    a52=(numpy.sqrt(10 + numpy.dot(2,numpy.sqrt(5)))) / 4
# transformMatrix03.m:54
    a53=(numpy.sqrt(15 + numpy.dot(2,numpy.sqrt(5)))) / 4
# transformMatrix03.m:55
    a54=(numpy.sqrt(50 - numpy.dot(22,numpy.sqrt(5)))) / 20
# transformMatrix03.m:56
    a55=(numpy.sqrt(5 - numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:57
    a56=(7 - numpy.sqrt(5)) / 20
# transformMatrix03.m:58
    a57=(numpy.sqrt(5 + numpy.dot(2,numpy.sqrt(5)))) / 10
# transformMatrix03.m:59
    a58=(numpy.dot(2,numpy.sqrt(5)) - 1) / 10
# transformMatrix03.m:60
    a59=(7 + numpy.sqrt(5)) / 20
# transformMatrix03.m:61
    a60=(numpy.sqrt(10 - numpy.dot(2,numpy.sqrt(5)))) / 5
# transformMatrix03.m:62
    a61=(numpy.sqrt(50 + numpy.dot(22,numpy.sqrt(5)))) / 20
# transformMatrix03.m:63
    a62=(numpy.dot(2,numpy.sqrt(5)) + 1) / 10
# transformMatrix03.m:64
    a63=(numpy.dot(3,numpy.sqrt(5)) - 1) / 10
# transformMatrix03.m:65
    #####################
    T1_1=numpy.array([[a21,- a52,0],[a52,a21,0],[0,0,1]])
# transformMatrix03.m:68
    T2_1=numpy.array([[- a46,a36,0],[- a36,- a46,0],[0,0,1]])
# transformMatrix03.m:71
    G_1=numpy.array([[a21,- a52,0,0],[a52,a21,0,0],[0,0,- a46,- a36],[0,0,a36,- a46]])
# transformMatrix03.m:74
    H_1=numpy.array([[1,0,0,0,0],[0,- a46,- a36,0,0],[0,a36,- a46,0,0],[0,0,0,a21,a52],[0,0,0,- a52,a21]])
# transformMatrix03.m:78
    T1_2=numpy.array([[a21,a52,0],[- a52,a21,0],[0,0,1]])
# transformMatrix03.m:83
    T2_2=numpy.array([[- a46,- a36,0],[a36,- a46,0],[0,0,1]])
# transformMatrix03.m:86
    G_2=numpy.array([[a21,a52,0,0],[- a52,a21,0,0],[0,0,- a46,a36],[0,0,- a36,- a46]])
# transformMatrix03.m:89
    H_2=numpy.array([[1,0,0,0,0],[0,- a46,a36,0,0],[0,- a36,- a46,0,0],[0,0,0,a21,- a52],[0,0,0,a52,a21]])
# transformMatrix03.m:93
    T1_3=numpy.array([[a41,- a14,a43],[a41,a5,- a31],[- a20,a48,a28]])
# transformMatrix03.m:98
    T2_3=numpy.array([[- a40,- a41,- a20],[- a14,a5,- a48],[a43,- a31,- a28]])
# transformMatrix03.m:101
    G_3=numpy.array([[- a17,a41,- a38,a19],[a14,- a5,- a19,a46],[a49,a27,a17,a14],[a27,- a21,- a41,- a5]])
# transformMatrix03.m:104
    H_3=numpy.array([[- a3,- a33,- a26,a39,- a16],[a16,a2,- a29,a13,a47],[- a39,a32,a17,a28,a13],[- a26,- a37,a28,- a17,a29],[a33,- a7,a37,a32,a2]])
# transformMatrix03.m:108
    T1_4=numpy.array([[a40,a41,- a20],[- a14,a5,a48],[a43,- a31,a28]])
# transformMatrix03.m:113
    T2_4=numpy.array([[- a40,- a14,a43],[- a41,a5,- a31],[- a20,- a48,- a28]])
# transformMatrix03.m:116
    G_4=numpy.array([[- a17,a14,a49,a27],[a41,- a5,a27,- a21],[- a38,- a19,a17,- a41],[a19,a46,a14,- a5]])
# transformMatrix03.m:119
    H_4=numpy.array([[- a3,a16,- a39,- a26,a33],[- a33,a2,a32,- a37,- a7],[- a26,- a29,a17,a28,a37],[a39,a13,a28,- a17,a32],[- a16,a47,a13,a29,a2]])
# transformMatrix03.m:123
    T1_5=numpy.array([[a24,- a36,a43],[a19,a46,a31],[- a50,0,a28]])
# transformMatrix03.m:128
    T2_5=numpy.array([[a12,- a52,- a20],[- a27,- a21,a48],[- a50,0,- a28]])
# transformMatrix03.m:131
    G_5=numpy.array([[- a43,0,a24,a36],[- a31,0,a19,- a46],[- a12,- a52,- a20,0],[- a27,a21,- a48,0]])
# transformMatrix03.m:134
    H_5=numpy.array([[- a3,a42,0,0,- a42],[a16,a15,- a27,- a48,a11],[a39,a34,a12,a20,a25],[a26,- a18,- a43,a24,- a23],[a33,- a22,a31,- a19,- a30]])
# transformMatrix03.m:138
    T1_6=numpy.array([[a24,a19,- a50],[- a36,a46,0],[a43,a31,a28]])
# transformMatrix03.m:143
    T2_6=numpy.array([[a12,- a27,- a50],[- a52,- a21,0],[- a20,a48,- a28]])
# transformMatrix03.m:146
    G_6=numpy.array([[- a43,- a31,- a12,- a27],[0,0,- a52,a21],[a24,a19,- a20,- a48],[a36,- a46,0,0]])
# transformMatrix03.m:149
    H_6=numpy.array([[- a3,a16,a39,a26,a33],[a42,a15,a34,- a18,- a22],[0,- a27,a12,- a43,a31],[0,- a48,a20,a24,- a19],[- a42,a11,a25,- a23,- a30]])
# transformMatrix03.m:153
    T1_7=numpy.array([[a49,- a27,- a20],[a27,a21,a48],[- a20,- a48,a28]])
# transformMatrix03.m:158
    T2_7=numpy.array([[a38,- a19,a43],[a19,- a46,- a31],[a43,a31,- a28]])
# transformMatrix03.m:161
    G_7=numpy.array([[a9,a19,- a28,- a48],[- a19,- a46,- a31,0],[- a28,a31,- a35,a27],[a48,0,- a27,a21]])
# transformMatrix03.m:164
    H_7=numpy.array([[- a3,- a33,a26,- a39,- a16],[- a33,a56,- a61,- a13,- a6],[- a26,a61,a9,- a28,a37],[a39,a13,- a28,- a35,- a54],[- a16,- a6,- a37,a54,a59]])
# transformMatrix03.m:168
    T1_8=numpy.array([[a49,a27,- a20],[- a27,a21,- a48],[- a20,a48,a28]])
# transformMatrix03.m:173
    T2_8=numpy.array([[a38,a19,a43],[- a19,- a46,a31],[a43,- a31,- a28]])
# transformMatrix03.m:176
    G_8=numpy.array([[a9,- a19,- a28,a48],[a19,- a46,a31,0],[- a28,- a31,- a35,- a27],[- a48,0,a27,a21]])
# transformMatrix03.m:179
    H_8=numpy.array([[- a3,- a33,- a26,a39,- a16],[- a33,a56,a61,a13,- a6],[a26,- a61,a9,- a28,- a37],[- a39,- a13,- a28,- a35,a54],[- a16,- a6,a37,- a54,a59]])
# transformMatrix03.m:183
    T1_9=numpy.array([[a24,- a19,- a50],[a36,a46,0],[a43,- a31,a28]])
# transformMatrix03.m:188
    T2_9=numpy.array([[a12,a27,- a50],[a52,- a21,0],[- a20,- a48,- a28]])
# transformMatrix03.m:191
    G_9=numpy.array([[- a43,a31,- a12,a27],[0,0,a52,a21],[a24,- a19,- a20,a48],[- a36,- a46,0,0]])
# transformMatrix03.m:194
    H_9=numpy.array([[- a3,a16,- a39,- a26,a33],[a42,a15,- a34,a18,- a22],[0,a27,a12,- a43,- a31],[0,a48,a20,a24,a19],[- a42,a11,- a25,a23,- a30]])
# transformMatrix03.m:198
    T1_10=numpy.array([[a24,a36,a43],[- a19,a46,- a31],[- a50,0,a28]])
# transformMatrix03.m:203
    T2_10=numpy.array([[a12,a52,- a20],[a27,- a21,- a48],[- a50,0,- a28]])
# transformMatrix03.m:206
    G_10=numpy.array([[- a43,0,a24,- a36],[a31,0,- a19,- a46],[- a12,a52,- a20,0],[a27,a21,a48,0]])
# transformMatrix03.m:209
    H_10=numpy.array([[- a3,a42,0,0,- a42],[a16,a15,a27,a48,a11],[- a39,- a34,a12,a20,- a25],[- a26,a18,- a43,a24,a23],[a33,- a22,- a31,a19,- a30]])
# transformMatrix03.m:213
    T1_11=numpy.array([[a40,- a41,- a20],[a14,a5,- a48],[a43,a31,a28]])
# transformMatrix03.m:218
    T2_11=numpy.array([[- a40,a14,a43],[a41,a5,a31],[- a20,a48,- a28]])
# transformMatrix03.m:221
    G_11=numpy.array([[- a17,- a14,a49,- a27],[- a41,- a5,- a27,- a21],[- a38,a19,a17,a41],[- a19,a46,- a14,- a5]])
# transformMatrix03.m:224
    H_11=numpy.array([[- a3,a16,a39,a26,a33],[- a33,a2,- a32,a37,- a7],[a26,a29,a17,a28,- a37],[- a39,- a13,a28,- a17,- a32],[- a16,a47,- a13,- a29,a2]])
# transformMatrix03.m:228
    T1_12=numpy.array([[a40,a14,a43],[- a41,a5,a31],[- a20,- a48,a28]])
# transformMatrix03.m:233
    T2_12=numpy.array([[- a40,a41,- a20],[a14,a5,a48],[a43,a31,- a28]])
# transformMatrix03.m:236
    G_12=numpy.array([[- a17,- a41,- a38,- a19],[- a14,- a5,a19,a46],[a49,- a27,a17,- a14],[- a27,- a21,a41,- a5]])
# transformMatrix03.m:239
    H_12=numpy.array([[- a3,- a33,a26,- a39,- a16],[a16,a2,a29,- a13,a47],[a39,- a32,a17,a28,- a13],[a26,a37,a28,- a17,- a29],[a33,- a7,- a37,- a32,a2]])
# transformMatrix03.m:243
    T1_13=numpy.array([[- a46,- a36,0],[a36,- a46,0],[0,0,1]])
# transformMatrix03.m:248
    T2_13=numpy.array([[a21,- a52,0],[a52,a21,0],[0,0,1]])
# transformMatrix03.m:251
    G_13=numpy.array([[- a46,- a36,0,0],[a36,- a46,0,0],[0,0,a21,a52],[0,0,- a52,a21]])
# transformMatrix03.m:254
    H_13=numpy.array([[1,0,0,0,0],[0,a21,a52,0,0],[0,- a52,a21,0,0],[0,0,0,- a46,a36],[0,0,0,- a36,- a46]])
# transformMatrix03.m:258
    T1_14=numpy.array([[- a46,a36,0],[- a36,- a46,0],[0,0,1]])
# transformMatrix03.m:263
    T2_14=numpy.array([[a21,a52,0],[- a52,a21,0],[0,0,1]])
# transformMatrix03.m:266
    G_14=numpy.array([[- a46,a36,0,0],[- a36,- a46,0,0],[0,0,a21,- a52],[0,0,a52,a21]])
# transformMatrix03.m:269
    H_14=numpy.array([[1,0,0,0,0],[0,a21,- a52,0,0],[0,a52,a21,0,0],[0,0,0,- a46,- a36],[0,0,0,a36,- a46]])
# transformMatrix03.m:273
    T1_15=numpy.array([[a12,a27,a50],[a52,- a21,0],[a20,a48,- a28]])
# transformMatrix03.m:278
    T2_15=numpy.array([[a24,a19,a50],[- a36,a46,0],[- a43,- a31,a28]])
# transformMatrix03.m:281
    G_15=numpy.array([[- a20,- a48,- a24,a19],[0,0,- a36,- a46],[a12,a27,- a43,a31],[- a52,a21,0,0]])
# transformMatrix03.m:284
    H_15=numpy.array([[- a3,- a33,a26,- a39,- a16],[a42,- a30,a23,a25,a11],[0,a19,a24,- a20,a48],[0,a31,a43,a12,- a27],[- a42,- a22,a18,a34,a15]])
# transformMatrix03.m:288
    T1_16=numpy.array([[a12,a52,a20],[a27,- a21,a48],[a50,0,- a28]])
# transformMatrix03.m:293
    T2_16=numpy.array([[a24,- a36,- a43],[a19,a46,- a31],[a50,0,a28]])
# transformMatrix03.m:296
    G_16=numpy.array([[- a20,0,a12,- a52],[- a48,0,a27,a21],[- a24,- a36,- a43,0],[a19,- a46,a31,0]])
# transformMatrix03.m:299
    H_16=numpy.array([[- a3,a42,0,0,- a42],[- a33,- a30,a19,a31,- a22],[a26,a23,a24,a43,a18],[- a39,a25,- a20,a12,a34],[- a16,a11,a48,- a27,a15]])
# transformMatrix03.m:303
    T1_17=numpy.array([[- a40,- a41,a20],[- a14,a5,a48],[- a43,a31,- a28]])
# transformMatrix03.m:308
    T2_17=numpy.array([[a40,a14,- a43],[- a41,a5,- a31],[a20,a48,a28]])
# transformMatrix03.m:311
    G_17=numpy.array([[a17,- a14,- a49,- a27],[a41,- a5,a27,- a21],[a38,a19,- a17,a41],[a19,a46,a14,- a5]])
# transformMatrix03.m:314
    H_17=numpy.array([[- a3,a16,- a39,- a26,a33],[- a33,a2,a32,- a37,- a7],[a26,a29,- a17,- a28,- a37],[- a39,- a13,- a28,a17,- a32],[- a16,a47,a13,a29,a2]])
# transformMatrix03.m:318
    T1_18=numpy.array([[- a40,- a14,- a43],[- a41,a5,a31],[a20,a48,- a28]])
# transformMatrix03.m:323
    T2_18=numpy.array([[a40,- a41,a20],[a14,a5,a48],[- a43,- a31,a28]])
# transformMatrix03.m:326
    G_18=numpy.array([[a17,a41,a38,a19],[- a14,- a5,a19,a46],[- a49,a27,- a17,a14],[- a27,- a21,a41,- a5]])
# transformMatrix03.m:329
    H_18=numpy.array([[- a3,- a33,a26,- a39,- a16],[a16,a2,a29,- a13,a47],[- a39,a32,- a17,- a28,a13],[- a26,- a37,- a28,a17,a29],[a33,- a7,- a37,- a32,a2]])
# transformMatrix03.m:333
    T1_19=numpy.array([[a38,- a19,- a43],[a19,- a46,a31],[- a43,- a31,- a28]])
# transformMatrix03.m:338
    T2_19=numpy.array([[a49,a27,a20],[- a27,a21,a48],[a20,- a48,a28]])
# transformMatrix03.m:341
    G_19=numpy.array([[- a35,- a27,a28,- a31],[a27,a21,a48,0],[a28,- a48,a9,a19],[a31,0,- a19,- a46]])
# transformMatrix03.m:344
    H_19=numpy.array([[- a3,a16,a39,a26,a33],[a16,a59,a54,a37,- a6],[- a39,- a54,- a35,a28,a13],[- a26,- a37,a28,a9,- a61],[a33,- a6,- a13,a61,a56]])
# transformMatrix03.m:348
    T1_20=numpy.array([[a38,a19,- a43],[- a19,- a46,- a31],[- a43,a31,- a28]])
# transformMatrix03.m:353
    T2_20=numpy.array([[a49,- a27,a20],[a27,a21,- a48],[a20,a48,a28]])
# transformMatrix03.m:356
    G_20=numpy.array([[- a35,a27,a28,a31],[- a27,a21,- a48,0],[a28,a48,a9,- a19],[- a31,0,a19,- a46]])
# transformMatrix03.m:359
    H_20=numpy.array([[- a3,a16,- a39,- a26,a33],[a16,a59,- a54,- a37,- a6],[a39,a54,- a35,a28,- a13],[a26,a37,a28,a9,a61],[a33,- a6,a13,- a61,a56]])
# transformMatrix03.m:363
    T1_21=numpy.array([[- a40,a14,- a43],[a41,a5,- a31],[a20,- a48,- a28]])
# transformMatrix03.m:368
    T2_21=numpy.array([[a40,a41,a20],[- a14,a5,- a48],[- a43,a31,a28]])
# transformMatrix03.m:371
    G_21=numpy.array([[a17,- a41,a38,- a19],[a14,- a5,- a19,a46],[- a49,- a27,- a17,- a14],[a27,- a21,- a41,- a5]])
# transformMatrix03.m:374
    H_21=numpy.array([[- a3,- a33,- a26,a39,- a16],[a16,a2,- a29,a13,a47],[a39,- a32,- a17,- a28,- a13],[a26,a37,- a28,a17,- a29],[a33,- a7,a37,a32,a2]])
# transformMatrix03.m:378
    T1_22=numpy.array([[- a40,a41,a20],[a14,a5,- a48],[- a43,- a31,- a28]])
# transformMatrix03.m:383
    T2_22=numpy.array([[a40,- a14,- a43],[a41,a5,a31],[a20,- a48,a28]])
# transformMatrix03.m:386
    G_22=numpy.array([[a17,a14,- a49,a27],[- a41,- a5,- a27,- a21],[a38,- a19,- a17,- a41],[- a19,a46,- a14,- a5]])
# transformMatrix03.m:389
    H_22=numpy.array([[- a3,a16,a39,a26,a33],[- a33,a2,- a32,a37,- a7],[- a26,- a29,- a17,- a28,a37],[a39,a13,- a28,a17,a32],[- a16,a47,- a13,- a29,a2]])
# transformMatrix03.m:393
    T1_23=numpy.array([[a12,- a52,a20],[- a27,- a21,- a48],[a50,0,a28]])
# transformMatrix03.m:398
    T2_23=numpy.array([[a24,a36,- a43],[- a19,a46,a31],[a50,0,a28]])
# transformMatrix03.m:401
    G_23=numpy.array([[- a20,0,a12,a52],[a48,0,- a27,a21],[- a24,a36,- a43,0],[- a19,- a46,- a31,0]])
# transformMatrix03.m:404
    H_23=numpy.array([[- a3,a42,0,0,- a42],[- a33,- a30,- a19,- a31,- a22],[- a26,- a23,a24,a43,- a18],[a39,- a25,- a20,a12,- a34],[- a16,a11,- a48,a27,a15]])
# transformMatrix03.m:408
    T1_24=numpy.array([[a12,- a27,a50],[- a52,- a21,0],[a20,- a48,- a28]])
# transformMatrix03.m:413
    T2_24=numpy.array([[a24,- a19,a50],[a36,a46,0],[- a43,a31,a28]])
# transformMatrix03.m:416
    G_24=numpy.array([[- a20,a48,- a24,- a19],[0,0,a36,- a46],[a12,- a27,- a43,- a31],[a52,a21,0,0]])
# transformMatrix03.m:419
    H_24=numpy.array([[- a3,- a33,- a26,a39,- a16],[a42,- a30,- a23,- a25,a11],[0,- a19,a24,- a20,- a48],[0,- a31,a43,a12,a27],[- a42,- a22,- a18,- a34,a15]])
# transformMatrix03.m:423
    T1_25=numpy.array([[a8,- a41,a43],[a41,- a5,- a31],[a43,a31,a28]])
# transformMatrix03.m:428
    T2_25=numpy.array([[a51,a14,- a20],[- a14,- a5,- a48],[- a20,a48,- a28]])
# transformMatrix03.m:431
    G_25=numpy.array([[a35,a27,a40,a14],[- a27,- a21,a41,- a5],[a40,- a41,- a9,- a19],[- a14,- a5,a19,a46]])
# transformMatrix03.m:434
    H_25=numpy.array([[- a3,a16,a39,a26,a33],[a16,- a58,a57,- a44,a4],[- a39,- a57,- a5,0,a60],[- a26,a44,0,- a5,- a55],[a33,a4,- a60,a55,a62]])
# transformMatrix03.m:438
    T1_26=numpy.array([[a8,a41,a43],[- a41,- a5,a31],[a43,- a31,a28]])
# transformMatrix03.m:443
    T2_26=numpy.array([[a51,- a14,- a20],[a14,- a5,a48],[- a20,- a48,- a28]])
# transformMatrix03.m:446
    G_26=numpy.array([[a35,- a27,a40,- a14],[a27,- a21,- a41,- a5],[a40,a41,- a9,a19],[a14,- a5,- a19,a46]])
# transformMatrix03.m:449
    H_26=numpy.array([[- a3,a16,- a39,- a26,a33],[a16,- a58,- a57,a44,a4],[a39,a57,- a5,0,- a60],[a26,- a44,0,- a5,a55],[a33,a4,a60,- a55,a62]])
# transformMatrix03.m:453
    T1_27=numpy.array([[- a28,- a31,a43],[a48,0,a31],[- a20,a48,a28]])
# transformMatrix03.m:458
    T2_27=numpy.array([[a28,a48,- a20],[a31,0,a48],[a43,- a31,- a28]])
# transformMatrix03.m:461
    G_27=numpy.array([[- a17,a41,a8,- a41],[- a14,a5,- a41,a5],[- a51,- a14,a17,a14],[a14,a5,a41,a5]])
# transformMatrix03.m:464
    H_27=numpy.array([[- a3,- a33,- a26,a39,- a16],[a16,- a4,a18,- a25,- a45],[a39,- a25,- a28,- a20,a25],[a26,- a18,a43,a28,a18],[a33,a63,- a18,a25,- a4]])
# transformMatrix03.m:468
    T1_28=numpy.array([[- a28,a48,- a20],[- a31,0,a48],[a43,a31,a28]])
# transformMatrix03.m:473
    T2_28=numpy.array([[a28,a31,a43],[a48,0,- a31],[- a20,a48,- a28]])
# transformMatrix03.m:476
    G_28=numpy.array([[- a17,- a14,- a51,a14],[a41,a5,- a14,a5],[a8,- a41,a17,a41],[- a41,a5,a14,a5]])
# transformMatrix03.m:479
    H_28=numpy.array([[- a3,a16,a39,a26,a33],[- a33,- a4,- a25,- a18,a63],[- a26,a18,- a28,a43,- a18],[a39,- a25,- a20,a28,a25],[- a16,- a45,a25,a18,- a4]])
# transformMatrix03.m:483
    T1_29=numpy.array([[- a12,- a52,- a20],[a27,- a21,a48],[- a50,0,a28]])
# transformMatrix03.m:488
    T2_29=numpy.array([[- a24,a36,a43],[a19,a46,- a31],[- a50,0,- a28]])
# transformMatrix03.m:491
    G_29=numpy.array([[a20,0,- a12,a52],[- a48,0,a27,a21],[a24,a36,a43,0],[a19,- a46,a31,0]])
# transformMatrix03.m:494
    H_29=numpy.array([[- a3,a42,0,0,- a42],[- a33,- a30,a19,a31,- a22],[- a26,- a23,- a24,- a43,- a18],[a39,- a25,a20,- a12,- a34],[- a16,a11,a48,- a27,a15]])
# transformMatrix03.m:498
    T1_30=numpy.array([[- a12,a27,- a50],[- a52,- a21,0],[- a20,a48,a28]])
# transformMatrix03.m:503
    T2_30=numpy.array([[- a24,a19,- a50],[a36,a46,0],[a43,- a31,- a28]])
# transformMatrix03.m:506
    G_30=numpy.array([[a20,- a48,a24,a19],[0,0,a36,- a46],[- a12,a27,a43,a31],[a52,a21,0,0]])
# transformMatrix03.m:509
    H_30=numpy.array([[- a3,- a33,- a26,a39,- a16],[a42,- a30,- a23,- a25,a11],[0,a19,- a24,a20,a48],[0,a31,- a43,- a12,- a27],[- a42,- a22,- a18,- a34,a15]])
# transformMatrix03.m:513
    T1_31=numpy.array([[- a12,- a27,- a50],[a52,- a21,0],[- a20,- a48,a28]])
# transformMatrix03.m:518
    T2_31=numpy.array([[- a24,- a19,- a50],[- a36,a46,0],[a43,a31,- a28]])
# transformMatrix03.m:521
    G_31=numpy.array([[a20,a48,a24,- a19],[0,0,- a36,- a46],[- a12,- a27,a43,- a31],[- a52,a21,0,0]])
# transformMatrix03.m:524
    H_31=numpy.array([[- a3,- a33,a26,- a39,- a16],[a42,- a30,a23,a25,a11],[0,- a19,- a24,a20,- a48],[0,- a31,- a43,- a12,a27],[- a42,- a22,a18,a34,a15]])
# transformMatrix03.m:528
    T1_32=numpy.array([[- a12,a52,- a20],[- a27,- a21,- a48],[- a50,0,a28]])
# transformMatrix03.m:533
    T2_32=numpy.array([[- a24,- a36,a43],[- a19,a46,a31],[- a50,0,- a28]])
# transformMatrix03.m:536
    G_32=numpy.array([[a20,0,- a12,- a52],[a48,0,- a27,a21],[a24,- a36,a43,0],[- a19,- a46,- a31,0]])
# transformMatrix03.m:539
    H_32=numpy.array([[- a3,a42,0,0,- a42],[- a33,- a30,- a19,- a31,- a22],[a26,a23,- a24,- a43,a18],[- a39,a25,a20,- a12,a34],[- a16,a11,- a48,a27,a15]])
# transformMatrix03.m:543
    T1_33=numpy.array([[- a28,- a48,- a20],[a31,0,- a48],[a43,- a31,a28]])
# transformMatrix03.m:548
    T2_33=numpy.array([[a28,- a31,a43],[- a48,0,a31],[- a20,- a48,- a28]])
# transformMatrix03.m:551
    G_33=numpy.array([[- a17,a14,- a51,- a14],[- a41,a5,a14,a5],[a8,a41,a17,- a41],[a41,a5,- a14,a5]])
# transformMatrix03.m:554
    H_33=numpy.array([[- a3,a16,- a39,- a26,a33],[- a33,- a4,a25,a18,a63],[a26,- a18,- a28,a43,a18],[- a39,a25,- a20,a28,- a25],[- a16,- a45,- a25,- a18,- a4]])
# transformMatrix03.m:558
    T1_34=numpy.array([[- a28,a31,a43],[- a48,0,- a31],[- a20,- a48,a28]])
# transformMatrix03.m:563
    T2_34=numpy.array([[a28,- a48,- a20],[- a31,0,- a48],[a43,a31,- a28]])
# transformMatrix03.m:566
    G_34=numpy.array([[- a17,- a41,a8,a41],[a14,a5,a41,a5],[- a51,a14,a17,- a14],[- a14,a5,- a41,a5]])
# transformMatrix03.m:569
    H_34=numpy.array([[- a3,- a33,a26,- a39,- a16],[a16,- a4,- a18,a25,- a45],[- a39,a25,- a28,- a20,- a25],[- a26,a18,a43,a28,- a18],[a33,a63,a18,- a25,- a4]])
# transformMatrix03.m:573
    T1_35=numpy.array([[a51,- a14,a20],[a14,- a5,- a48],[a20,a48,- a28]])
# transformMatrix03.m:578
    T2_35=numpy.array([[a8,- a41,- a43],[a41,- a5,a31],[- a43,- a31,a28]])
# transformMatrix03.m:581
    G_35=numpy.array([[- a9,- a19,- a40,- a41],[a19,a46,a14,- a5],[- a40,- a14,a35,- a27],[a41,- a5,a27,- a21]])
# transformMatrix03.m:584
    H_35=numpy.array([[- a3,- a33,a26,- a39,- a16],[- a33,a62,- a55,- a60,a4],[- a26,a55,- a5,0,- a44],[a39,a60,0,- a5,- a57],[- a16,a4,a44,a57,- a58]])
# transformMatrix03.m:588
    T1_36=numpy.array([[a51,a14,a20],[- a14,- a5,a48],[a20,- a48,- a28]])
# transformMatrix03.m:593
    T2_36=numpy.array([[a8,a41,- a43],[- a41,- a5,- a31],[- a43,a31,a28]])
# transformMatrix03.m:596
    G_36=numpy.array([[- a9,a19,- a40,a41],[- a19,a46,- a14,- a5],[- a40,a14,a35,a27],[- a41,- a5,- a27,- a21]])
# transformMatrix03.m:599
    H_36=numpy.array([[- a3,- a33,- a26,a39,- a16],[- a33,a62,a55,a60,a4],[a26,- a55,- a5,0,a44],[- a39,- a60,0,- a5,a57],[- a16,a4,- a44,- a57,- a58]])
# transformMatrix03.m:603
    T1_37=numpy.array([[- a24,a19,a50],[a36,a46,0],[- a43,a31,- a28]])
# transformMatrix03.m:608
    T2_37=numpy.array([[- a12,- a27,a50],[a52,- a21,0],[a20,a48,a28]])
# transformMatrix03.m:611
    G_37=numpy.array([[a43,- a31,a12,- a27],[0,0,a52,a21],[- a24,a19,a20,- a48],[- a36,- a46,0,0]])
# transformMatrix03.m:614
    H_37=numpy.array([[- a3,a16,- a39,- a26,a33],[a42,a15,- a34,a18,- a22],[0,- a27,- a12,a43,a31],[0,- a48,- a20,- a24,- a19],[- a42,a11,- a25,a23,- a30]])
# transformMatrix03.m:618
    T1_38=numpy.array([[- a24,a36,- a43],[a19,a46,a31],[a50,0,- a28]])
# transformMatrix03.m:623
    T2_38=numpy.array([[- a12,a52,a20],[- a27,- a21,a48],[a50,0,a28]])
# transformMatrix03.m:626
    G_38=numpy.array([[a43,0,- a24,- a36],[- a31,0,a19,- a46],[a12,a52,a20,0],[- a27,a21,- a48,0]])
# transformMatrix03.m:629
    H_38=numpy.array([[- a3,a42,0,0,- a42],[a16,a15,- a27,- a48,a11],[- a39,- a34,- a12,- a20,- a25],[- a26,a18,a43,- a24,a23],[a33,- a22,a31,- a19,- a30]])
# transformMatrix03.m:633
    T1_39=numpy.array([[a28,- a48,a20],[- a31,0,a48],[- a43,- a31,- a28]])
# transformMatrix03.m:638
    T2_39=numpy.array([[- a28,- a31,- a43],[a48,0,- a31],[a20,- a48,a28]])
# transformMatrix03.m:641
    G_39=numpy.array([[a17,a14,a51,- a14],[a41,a5,- a14,a5],[- a8,a41,- a17,- a41],[- a41,a5,a14,a5]])
# transformMatrix03.m:644
    H_39=numpy.array([[- a3,a16,a39,a26,a33],[- a33,- a4,- a25,- a18,a63],[a26,- a18,a28,- a43,a18],[- a39,a25,a20,- a28,- a25],[- a16,- a45,a25,a18,- a4]])
# transformMatrix03.m:648
    T1_40=numpy.array([[a28,- a31,- a43],[- a48,0,- a31],[a20,a48,- a28]])
# transformMatrix03.m:653
    T2_40=numpy.array([[- a28,a48,a20],[- a31,0,- a48],[- a43,- a31,a28]])
# transformMatrix03.m:656
    G_40=numpy.array([[a17,a41,- a8,- a41],[a14,a5,a41,a5],[a51,- a14,- a17,a14],[- a14,a5,- a41,a5]])
# transformMatrix03.m:659
    H_40=numpy.array([[- a3,- a33,a26,- a39,- a16],[a16,- a4,- a18,a25,- a45],[a39,- a25,a28,a20,a25],[a26,- a18,- a43,- a28,a18],[a33,a63,a18,- a25,- a4]])
# transformMatrix03.m:663
    T1_41=numpy.array([[a28,a31,- a43],[a48,0,a31],[a20,- a48,- a28]])
# transformMatrix03.m:668
    T2_41=numpy.array([[- a28,- a48,a20],[a31,0,a48],[- a43,a31,a28]])
# transformMatrix03.m:671
    G_41=numpy.array([[a17,- a41,- a8,a41],[- a14,a5,- a41,a5],[a51,a14,- a17,- a14],[a14,a5,a41,a5]])
# transformMatrix03.m:674
    H_41=numpy.array([[- a3,- a33,- a26,a39,- a16],[a16,- a4,a18,- a25,- a45],[- a39,a25,a28,a20,- a25],[- a26,a18,- a43,- a28,- a18],[a33,a63,- a18,a25,- a4]])
# transformMatrix03.m:678
    T1_42=numpy.array([[a28,a48,a20],[a31,0,- a48],[- a43,a31,- a28]])
# transformMatrix03.m:683
    T2_42=numpy.array([[- a28,a31,- a43],[- a48,0,a31],[a20,a48,a28]])
# transformMatrix03.m:686
    G_42=numpy.array([[a17,- a14,a51,a14],[- a41,a5,a14,a5],[- a8,- a41,- a17,a41],[a41,a5,- a14,a5]])
# transformMatrix03.m:689
    H_42=numpy.array([[- a3,a16,- a39,- a26,a33],[- a33,- a4,a25,a18,a63],[- a26,a18,a28,- a43,- a18],[a39,- a25,a20,- a28,a25],[- a16,- a45,- a25,- a18,- a4]])
# transformMatrix03.m:693
    T1_43=numpy.array([[- a24,- a36,- a43],[- a19,a46,- a31],[a50,0,- a28]])
# transformMatrix03.m:698
    T2_43=numpy.array([[- a12,- a52,a20],[a27,- a21,- a48],[a50,0,a28]])
# transformMatrix03.m:701
    G_43=numpy.array([[a43,0,- a24,a36],[a31,0,- a19,- a46],[a12,- a52,a20,0],[a27,a21,a48,0]])
# transformMatrix03.m:704
    H_43=numpy.array([[- a3,a42,0,0,- a42],[a16,a15,a27,a48,a11],[a39,a34,- a12,- a20,a25],[a26,- a18,a43,- a24,- a23],[a33,- a22,- a31,a19,- a30]])
# transformMatrix03.m:708
    T1_44=numpy.array([[- a24,- a19,a50],[- a36,a46,0],[- a43,- a31,- a28]])
# transformMatrix03.m:713
    T2_44=numpy.array([[- a12,a27,a50],[- a52,- a21,0],[a20,- a48,a28]])
# transformMatrix03.m:716
    G_44=numpy.array([[a43,a31,a12,a27],[0,0,- a52,a21],[- a24,- a19,a20,a48],[a36,- a46,0,0]])
# transformMatrix03.m:719
    H_44=numpy.array([[- a3,a16,a39,a26,a33],[a42,a15,a34,- a18,- a22],[0,a27,- a12,a43,- a31],[0,a48,- a20,- a24,a19],[- a42,a11,a25,- a23,- a30]])
# transformMatrix03.m:723
    T1_45=numpy.array([[- a38,a19,a43],[a19,- a46,a31],[a43,a31,a28]])
# transformMatrix03.m:728
    T2_45=numpy.array([[- a49,- a27,- a20],[- a27,a21,a48],[- a20,a48,- a28]])
# transformMatrix03.m:731
    G_45=numpy.array([[a35,a27,- a28,a31],[a27,a21,a48,0],[- a28,a48,- a9,- a19],[a31,0,- a19,- a46]])
# transformMatrix03.m:734
    H_45=numpy.array([[- a3,a16,a39,a26,a33],[a16,a59,a54,a37,- a6],[a39,a54,a35,- a28,- a13],[a26,a37,- a28,- a9,a61],[a33,- a6,- a13,a61,a56]])
# transformMatrix03.m:738
    T1_46=numpy.array([[- a51,- a14,- a20],[- a14,- a5,a48],[- a20,a48,a28]])
# transformMatrix03.m:743
    T2_46=numpy.array([[- a8,- a41,a43],[- a41,- a5,- a31],[a43,- a31,- a28]])
# transformMatrix03.m:746
    G_46=numpy.array([[a9,- a19,a40,- a41],[- a19,a46,- a14,- a5],[a40,- a14,- a35,- a27],[- a41,- a5,- a27,- a21]])
# transformMatrix03.m:749
    H_46=numpy.array([[- a3,- a33,- a26,a39,- a16],[- a33,a62,a55,a60,a4],[- a26,a55,a5,0,- a44],[a39,a60,0,a5,- a57],[- a16,a4,- a44,- a57,- a58]])
# transformMatrix03.m:753
    T1_47=numpy.array([[- a28,0,- a50],[0,- a1,0],[- a50,0,a28]])
# transformMatrix03.m:758
    T2_47=numpy.array([[a28,0,- a50],[0,- a1,0],[- a50,0,- a28]])
# transformMatrix03.m:761
    G_47=numpy.array([[a50,0,- a28,0],[0,0,0,a1],[- a28,0,- a50,0],[0,a1,0,0]])
# transformMatrix03.m:764
    H_47=numpy.array([[- a3,a42,0,0,- a42],[a42,a6,0,0,a4],[0,0,a28,a50,0],[0,0,a50,- a28,0],[- a42,a4,0,0,a6]])
# transformMatrix03.m:768
    T1_48=numpy.array([[- a51,a14,- a20],[a14,- a5,- a48],[- a20,- a48,a28]])
# transformMatrix03.m:773
    T2_48=numpy.array([[- a8,a41,a43],[a41,- a5,a31],[a43,a31,- a28]])
# transformMatrix03.m:776
    G_48=numpy.array([[a9,a19,a40,a41],[a19,a46,a14,- a5],[a40,a14,- a35,a27],[a41,- a5,a27,- a21]])
# transformMatrix03.m:779
    H_48=numpy.array([[- a3,- a33,a26,- a39,- a16],[- a33,a62,- a55,- a60,a4],[a26,- a55,a5,0,a44],[- a39,- a60,0,a5,a57],[- a16,a4,a44,a57,- a58]])
# transformMatrix03.m:783
    T1_49=numpy.array([[- a38,- a19,a43],[- a19,- a46,- a31],[a43,- a31,a28]])
# transformMatrix03.m:788
    T2_49=numpy.array([[- a49,a27,- a20],[a27,a21,- a48],[- a20,- a48,- a28]])
# transformMatrix03.m:791
    G_49=numpy.array([[a35,- a27,- a28,- a31],[- a27,a21,- a48,0],[- a28,- a48,- a9,a19],[- a31,0,a19,- a46]])
# transformMatrix03.m:794
    H_49=numpy.array([[- a3,a16,- a39,- a26,a33],[a16,a59,- a54,- a37,- a6],[- a39,- a54,a35,- a28,a13],[- a26,- a37,- a28,- a9,- a61],[a33,- a6,a13,- a61,a56]])
# transformMatrix03.m:798
    T1_50=numpy.array([[a28,0,a50],[0,- a1,0],[a50,0,- a28]])
# transformMatrix03.m:803
    T2_50=numpy.array([[- a28,0,a50],[0,- a1,0],[a50,0,a28]])
# transformMatrix03.m:806
    G_50=numpy.array([[- a50,0,a28,0],[0,0,0,a1],[a28,0,a50,0],[0,a1,0,0]])
# transformMatrix03.m:809
    H_50=numpy.array([[- a3,a42,0,0,- a42],[a42,a6,0,0,a4],[0,0,- a28,- a50,0],[0,0,- a50,a28,0],[- a42,a4,0,0,a6]])
# transformMatrix03.m:813
    T1_51=numpy.array([[- a49,a27,a20],[a27,a21,a48],[a20,a48,- a28]])
# transformMatrix03.m:818
    T2_51=numpy.array([[- a38,a19,- a43],[a19,- a46,- a31],[- a43,- a31,a28]])
# transformMatrix03.m:821
    G_51=numpy.array([[- a9,- a19,a28,a48],[- a19,- a46,- a31,0],[a28,- a31,a35,- a27],[a48,0,- a27,a21]])
# transformMatrix03.m:824
    H_51=numpy.array([[- a3,- a33,a26,- a39,- a16],[- a33,a56,- a61,- a13,- a6],[a26,- a61,- a9,a28,- a37],[- a39,- a13,a28,a35,a54],[- a16,- a6,- a37,a54,a59]])
# transformMatrix03.m:828
    T1_52=numpy.array([[- a8,- a41,- a43],[- a41,- a5,a31],[- a43,a31,- a28]])
# transformMatrix03.m:833
    T2_52=numpy.array([[- a51,a14,a20],[a14,- a5,a48],[a20,a48,a28]])
# transformMatrix03.m:836
    G_52=numpy.array([[- a35,a27,- a40,a14],[a27,- a21,- a41,- a5],[- a40,- a41,a9,- a19],[a14,- a5,- a19,a46]])
# transformMatrix03.m:839
    H_52=numpy.array([[- a3,a16,- a39,- a26,a33],[a16,- a58,- a57,a44,a4],[- a39,- a57,a5,0,a60],[- a26,a44,0,a5,- a55],[a33,a4,a60,- a55,a62]])
# transformMatrix03.m:843
    T1_53=numpy.array([[- a8,a41,- a43],[a41,- a5,- a31],[- a43,- a31,- a28]])
# transformMatrix03.m:848
    T2_53=numpy.array([[- a51,- a14,a20],[- a14,- a5,- a48],[a20,- a48,a28]])
# transformMatrix03.m:851
    G_53=numpy.array([[- a35,- a27,- a40,- a14],[- a27,- a21,a41,- a5],[- a40,a41,a9,a19],[- a14,- a5,a19,a46]])
# transformMatrix03.m:854
    H_53=numpy.array([[- a3,a16,a39,a26,a33],[a16,- a58,a57,- a44,a4],[a39,a57,a5,0,- a60],[a26,- a44,0,a5,a55],[a33,a4,- a60,a55,a62]])
# transformMatrix03.m:858
    T1_54=numpy.array([[- a49,- a27,a20],[- a27,a21,- a48],[a20,- a48,- a28]])
# transformMatrix03.m:863
    T2_54=numpy.array([[- a38,- a19,- a43],[- a19,- a46,a31],[- a43,a31,a28]])
# transformMatrix03.m:866
    G_54=numpy.array([[- a9,a19,a28,- a48],[a19,- a46,a31,0],[a28,a31,a35,a27],[- a48,0,a27,a21]])
# transformMatrix03.m:869
    H_54=numpy.array([[- a3,- a33,- a26,a39,- a16],[- a33,a56,a61,a13,- a6],[- a26,a61,- a9,a28,a37],[a39,a13,a28,a35,- a54],[- a16,- a6,a37,- a54,a59]])
# transformMatrix03.m:873
    T1_55=numpy.array([[a46,a36,0],[a36,- a46,0],[0,0,- a1]])
# transformMatrix03.m:878
    T2_55=numpy.array([[- a21,a52,0],[a52,a21,0],[0,0,- a1]])
# transformMatrix03.m:881
    G_55=numpy.array([[a46,a36,0,0],[a36,- a46,0,0],[0,0,- a21,- a52],[0,0,- a52,a21]])
# transformMatrix03.m:884
    H_55=numpy.array([[a1,0,0,0,0],[0,a21,a52,0,0],[0,a52,- a21,0,0],[0,0,0,a46,- a36],[0,0,0,- a36,- a46]])
# transformMatrix03.m:888
    T1_56=numpy.array([[- a21,a52,0],[a52,a21,0],[0,0,- a1]])
# transformMatrix03.m:893
    T2_56=numpy.array([[a46,- a36,0],[- a36,- a46,0],[0,0,- a1]])
# transformMatrix03.m:896
    G_56=numpy.array([[- a21,a52,0,0],[a52,a21,0,0],[0,0,a46,a36],[0,0,a36,- a46]])
# transformMatrix03.m:899
    H_56=numpy.array([[a1,0,0,0,0],[0,- a46,- a36,0,0],[0,- a36,a46,0,0],[0,0,0,- a21,- a52],[0,0,0,- a52,a21]])
# transformMatrix03.m:903
    T1_57=numpy.array([[- a1,0,0],[0,a1,0],[0,0,- a1]])
# transformMatrix03.m:908
    T2_57=numpy.array([[- a1,0,0],[0,a1,0],[0,0,- a1]])
# transformMatrix03.m:911
    G_57=numpy.array([[- a1,0,0,0],[0,a1,0,0],[0,0,- a1,0],[0,0,0,a1]])
# transformMatrix03.m:914
    H_57=numpy.array([[a1,0,0,0,0],[0,a1,0,0,0],[0,0,- a1,0,0],[0,0,0,- a1,0],[0,0,0,0,a1]])
# transformMatrix03.m:918
    T1_58=numpy.array([[- a21,- a52,0],[- a52,a21,0],[0,0,- a1]])
# transformMatrix03.m:923
    T2_58=numpy.array([[a46,a36,0],[a36,- a46,0],[0,0,- a1]])
# transformMatrix03.m:926
    G_58=numpy.array([[- a21,- a52,0,0],[- a52,a21,0,0],[0,0,a46,- a36],[0,0,- a36,- a46]])
# transformMatrix03.m:929
    H_58=numpy.array([[a1,0,0,0,0],[0,- a46,a36,0,0],[0,a36,a46,0,0],[0,0,0,- a21,a52],[0,0,0,a52,a21]])
# transformMatrix03.m:933
    T1_59=numpy.array([[a46,- a36,0],[- a36,- a46,0],[0,0,- a1]])
# transformMatrix03.m:938
    T2_59=numpy.array([[- a21,- a52,0],[- a52,a21,0],[0,0,- a1]])
# transformMatrix03.m:941
    G_59=numpy.array([[a46,- a36,0,0],[- a36,- a46,0,0],[0,0,- a21,a52],[0,0,a52,a21]])
# transformMatrix03.m:944
    H_59=numpy.array([[a1,0,0,0,0],[0,a21,- a52,0,0],[0,- a52,- a21,0,0],[0,0,0,a46,a36],[0,0,0,a36,- a46]])
# transformMatrix03.m:948
    ##########construct the irreducible respresentation########
    A=numpy.ones([60,1,1])
# transformMatrix03.m:955
    
    #A
    T1=numpy.zeros([60,3,3])
# transformMatrix03.m:960
    T1[0,:,:]=numpy.array([[1,0,0],[0,1,0],[0,0,1]])
# transformMatrix03.m:961
    T1[1,:,:]=T1_1
# transformMatrix03.m:964
    T1[2,:,:]=T1_2
# transformMatrix03.m:965
    T1[3,:,:]=T1_3
# transformMatrix03.m:966
    T1[4,:,:]=T1_4
# transformMatrix03.m:967
    T1[5,:,:]=T1_5
# transformMatrix03.m:968
    T1[6,:,:]=T1_6
# transformMatrix03.m:969
    T1[7,:,:]=T1_7
# transformMatrix03.m:970
    T1[8,:,:]=T1_8
# transformMatrix03.m:971
    T1[9,:,:]=T1_9
# transformMatrix03.m:972
    T1[10,:,:]=T1_10
# transformMatrix03.m:973
    T1[11,:,:]=T1_11
# transformMatrix03.m:974
    T1[12,:,:]=T1_12
# transformMatrix03.m:975
    T1[13,:,:]=T1_13
# transformMatrix03.m:976
    T1[14,:,:]=T1_14
# transformMatrix03.m:977
    T1[15,:,:]=T1_15
# transformMatrix03.m:978
    T1[16,:,:]=T1_16
# transformMatrix03.m:979
    T1[17,:,:]=T1_17
# transformMatrix03.m:980
    T1[18,:,:]=T1_18
# transformMatrix03.m:981
    T1[19,:,:]=T1_19
# transformMatrix03.m:982
    T1[20,:,:]=T1_20
# transformMatrix03.m:983
    T1[21,:,:]=T1_21
# transformMatrix03.m:984
    T1[22,:,:]=T1_22
# transformMatrix03.m:985
    T1[23,:,:]=T1_23
# transformMatrix03.m:986
    T1[24,:,:]=T1_24
# transformMatrix03.m:987
    T1[25,:,:]=T1_25
# transformMatrix03.m:988
    T1[26,:,:]=T1_26
# transformMatrix03.m:989
    T1[27,:,:]=T1_27
# transformMatrix03.m:990
    T1[28,:,:]=T1_28
# transformMatrix03.m:991
    T1[29,:,:]=T1_29
# transformMatrix03.m:992
    T1[30,:,:]=T1_30
# transformMatrix03.m:993
    T1[31,:,:]=T1_31
# transformMatrix03.m:994
    T1[32,:,:]=T1_32
# transformMatrix03.m:995
    T1[33,:,:]=T1_33
# transformMatrix03.m:996
    T1[34,:,:]=T1_34
# transformMatrix03.m:997
    T1[35,:,:]=T1_35
# transformMatrix03.m:998
    T1[36,:,:]=T1_36
# transformMatrix03.m:999
    T1[37,:,:]=T1_37
# transformMatrix03.m:1000
    T1[38,:,:]=T1_38
# transformMatrix03.m:1001
    T1[39,:,:]=T1_39
# transformMatrix03.m:1002
    T1[40,:,:]=T1_40
# transformMatrix03.m:1003
    T1[41,:,:]=T1_41
# transformMatrix03.m:1004
    T1[42,:,:]=T1_42
# transformMatrix03.m:1005
    T1[43,:,:]=T1_43
# transformMatrix03.m:1006
    T1[44,:,:]=T1_44
# transformMatrix03.m:1007
    T1[45,:,:]=T1_45
# transformMatrix03.m:1008
    T1[46,:,:]=T1_46
# transformMatrix03.m:1009
    T1[47,:,:]=T1_47
# transformMatrix03.m:1010
    T1[48,:,:]=T1_48
# transformMatrix03.m:1011
    T1[49,:,:]=T1_49
# transformMatrix03.m:1012
    T1[50,:,:]=T1_50
# transformMatrix03.m:1013
    T1[51,:,:]=T1_51
# transformMatrix03.m:1014
    T1[52,:,:]=T1_52
# transformMatrix03.m:1015
    T1[53,:,:]=T1_53
# transformMatrix03.m:1016
    T1[54,:,:]=T1_54
# transformMatrix03.m:1017
    T1[55,:,:]=T1_55
# transformMatrix03.m:1018
    T1[56,:,:]=T1_56
# transformMatrix03.m:1019
    T1[57,:,:]=T1_57
# transformMatrix03.m:1020
    T1[58,:,:]=T1_58
# transformMatrix03.m:1021
    T1[59,:,:]=T1_59
# transformMatrix03.m:1022
    #T1
    
    
    T2=numpy.zeros([60,3,3])
# transformMatrix03.m:1026
    T2[0,:,:]=numpy.array([[1,0,0],[0,1,0],[0,0,1]])
# transformMatrix03.m:1027
    T2[1,:,:]=T2_1
# transformMatrix03.m:1030
    T2[2,:,:]=T2_2
# transformMatrix03.m:1031
    T2[3,:,:]=T2_3
# transformMatrix03.m:1032
    T2[4,:,:]=T2_4
# transformMatrix03.m:1033
    T2[5,:,:]=T2_5
# transformMatrix03.m:1034
    T2[6,:,:]=T2_6
# transformMatrix03.m:1035
    T2[7,:,:]=T2_7
# transformMatrix03.m:1036
    T2[8,:,:]=T2_8
# transformMatrix03.m:1037
    T2[9,:,:]=T2_9
# transformMatrix03.m:1038
    T2[10,:,:]=T2_10
# transformMatrix03.m:1039
    T2[11,:,:]=T2_11
# transformMatrix03.m:1040
    T2[12,:,:]=T2_12
# transformMatrix03.m:1041
    T2[13,:,:]=T2_13
# transformMatrix03.m:1042
    T2[14,:,:]=T2_14
# transformMatrix03.m:1043
    T2[15,:,:]=T2_15
# transformMatrix03.m:1044
    T2[16,:,:]=T2_16
# transformMatrix03.m:1045
    T2[17,:,:]=T2_17
# transformMatrix03.m:1046
    T2[18,:,:]=T2_18
# transformMatrix03.m:1047
    T2[19,:,:]=T2_19
# transformMatrix03.m:1048
    T2[20,:,:]=T2_20
# transformMatrix03.m:1049
    T2[21,:,:]=T2_21
# transformMatrix03.m:1050
    T2[22,:,:]=T2_22
# transformMatrix03.m:1051
    T2[23,:,:]=T2_23
# transformMatrix03.m:1052
    T2[24,:,:]=T2_24
# transformMatrix03.m:1053
    T2[25,:,:]=T2_25
# transformMatrix03.m:1054
    T2[26,:,:]=T2_26
# transformMatrix03.m:1055
    T2[27,:,:]=T2_27
# transformMatrix03.m:1056
    T2[28,:,:]=T2_28
# transformMatrix03.m:1057
    T2[29,:,:]=T2_29
# transformMatrix03.m:1058
    T2[30,:,:]=T2_30
# transformMatrix03.m:1059
    T2[31,:,:]=T2_31
# transformMatrix03.m:1060
    T2[32,:,:]=T2_32
# transformMatrix03.m:1061
    T2[33,:,:]=T2_33
# transformMatrix03.m:1062
    T2[34,:,:]=T2_34
# transformMatrix03.m:1063
    T2[35,:,:]=T2_35
# transformMatrix03.m:1064
    T2[36,:,:]=T2_36
# transformMatrix03.m:1065
    T2[37,:,:]=T2_37
# transformMatrix03.m:1066
    T2[38,:,:]=T2_38
# transformMatrix03.m:1067
    T2[39,:,:]=T2_39
# transformMatrix03.m:1068
    T2[40,:,:]=T2_40
# transformMatrix03.m:1069
    T2[41,:,:]=T2_41
# transformMatrix03.m:1070
    T2[42,:,:]=T2_42
# transformMatrix03.m:1071
    T2[43,:,:]=T2_43
# transformMatrix03.m:1072
    T2[44,:,:]=T2_44
# transformMatrix03.m:1073
    T2[45,:,:]=T2_45
# transformMatrix03.m:1074
    T2[46,:,:]=T2_46
# transformMatrix03.m:1075
    T2[47,:,:]=T2_47
# transformMatrix03.m:1076
    T2[48,:,:]=T2_48
# transformMatrix03.m:1077
    T2[49,:,:]=T2_49
# transformMatrix03.m:1078
    T2[50,:,:]=T2_50
# transformMatrix03.m:1079
    T2[51,:,:]=T2_51
# transformMatrix03.m:1080
    T2[52,:,:]=T2_52
# transformMatrix03.m:1081
    T2[53,:,:]=T2_53
# transformMatrix03.m:1082
    T2[54,:,:]=T2_54
# transformMatrix03.m:1083
    T2[55,:,:]=T2_55
# transformMatrix03.m:1084
    T2[56,:,:]=T2_56
# transformMatrix03.m:1085
    T2[57,:,:]=T2_57
# transformMatrix03.m:1086
    T2[58,:,:]=T2_58
# transformMatrix03.m:1087
    T2[59,:,:]=T2_59
# transformMatrix03.m:1088
    #T2
    
    G=numpy.zeros([60,4,4])
# transformMatrix03.m:1091
    G[0,:,:]=numpy.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# transformMatrix03.m:1092
    G[1,:,:]=G_1
# transformMatrix03.m:1096
    G[2,:,:]=G_2
# transformMatrix03.m:1097
    G[3,:,:]=G_3
# transformMatrix03.m:1098
    G[4,:,:]=G_4
# transformMatrix03.m:1099
    G[5,:,:]=G_5
# transformMatrix03.m:1100
    G[6,:,:]=G_6
# transformMatrix03.m:1101
    G[7,:,:]=G_7
# transformMatrix03.m:1102
    G[8,:,:]=G_8
# transformMatrix03.m:1103
    G[9,:,:]=G_9
# transformMatrix03.m:1104
    G[10,:,:]=G_10
# transformMatrix03.m:1105
    G[11,:,:]=G_11
# transformMatrix03.m:1106
    G[12,:,:]=G_12
# transformMatrix03.m:1107
    G[13,:,:]=G_13
# transformMatrix03.m:1108
    G[14,:,:]=G_14
# transformMatrix03.m:1109
    G[15,:,:]=G_15
# transformMatrix03.m:1110
    G[16,:,:]=G_16
# transformMatrix03.m:1111
    G[17,:,:]=G_17
# transformMatrix03.m:1112
    G[18,:,:]=G_18
# transformMatrix03.m:1113
    G[19,:,:]=G_19
# transformMatrix03.m:1114
    G[20,:,:]=G_20
# transformMatrix03.m:1115
    G[21,:,:]=G_21
# transformMatrix03.m:1116
    G[22,:,:]=G_22
# transformMatrix03.m:1117
    G[23,:,:]=G_23
# transformMatrix03.m:1118
    G[24,:,:]=G_24
# transformMatrix03.m:1119
    G[25,:,:]=G_25
# transformMatrix03.m:1120
    G[26,:,:]=G_26
# transformMatrix03.m:1121
    G[27,:,:]=G_27
# transformMatrix03.m:1122
    G[28,:,:]=G_28
# transformMatrix03.m:1123
    G[29,:,:]=G_29
# transformMatrix03.m:1124
    G[30,:,:]=G_30
# transformMatrix03.m:1125
    G[31,:,:]=G_31
# transformMatrix03.m:1126
    G[32,:,:]=G_32
# transformMatrix03.m:1127
    G[33,:,:]=G_33
# transformMatrix03.m:1128
    G[34,:,:]=G_34
# transformMatrix03.m:1129
    G[35,:,:]=G_35
# transformMatrix03.m:1130
    G[36,:,:]=G_36
# transformMatrix03.m:1131
    G[37,:,:]=G_37
# transformMatrix03.m:1132
    G[38,:,:]=G_38
# transformMatrix03.m:1133
    G[39,:,:]=G_39
# transformMatrix03.m:1134
    G[40,:,:]=G_40
# transformMatrix03.m:1135
    G[41,:,:]=G_41
# transformMatrix03.m:1136
    G[42,:,:]=G_42
# transformMatrix03.m:1137
    G[43,:,:]=G_43
# transformMatrix03.m:1138
    G[44,:,:]=G_44
# transformMatrix03.m:1139
    G[45,:,:]=G_45
# transformMatrix03.m:1140
    G[46,:,:]=G_46
# transformMatrix03.m:1141
    G[47,:,:]=G_47
# transformMatrix03.m:1142
    G[48,:,:]=G_48
# transformMatrix03.m:1143
    G[49,:,:]=G_49
# transformMatrix03.m:1144
    G[50,:,:]=G_50
# transformMatrix03.m:1145
    G[51,:,:]=G_51
# transformMatrix03.m:1146
    G[52,:,:]=G_52
# transformMatrix03.m:1147
    G[53,:,:]=G_53
# transformMatrix03.m:1148
    G[54,:,:]=G_54
# transformMatrix03.m:1149
    G[55,:,:]=G_55
# transformMatrix03.m:1150
    G[56,:,:]=G_56
# transformMatrix03.m:1151
    G[57,:,:]=G_57
# transformMatrix03.m:1152
    G[58,:,:]=G_58
# transformMatrix03.m:1153
    G[59,:,:]=G_59
# transformMatrix03.m:1154
    #G
    
    H=numpy.zeros([60,5,5])
# transformMatrix03.m:1157
    H[0,:,:]=numpy.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
# transformMatrix03.m:1158
    H[1,:,:]=H_1
# transformMatrix03.m:1163
    H[2,:,:]=H_2
# transformMatrix03.m:1164
    H[3,:,:]=H_3
# transformMatrix03.m:1165
    H[4,:,:]=H_4
# transformMatrix03.m:1166
    H[5,:,:]=H_5
# transformMatrix03.m:1167
    H[6,:,:]=H_6
# transformMatrix03.m:1168
    H[7,:,:]=H_7
# transformMatrix03.m:1169
    H[8,:,:]=H_8
# transformMatrix03.m:1170
    H[9,:,:]=H_9
# transformMatrix03.m:1171
    H[10,:,:]=H_10
# transformMatrix03.m:1172
    H[11,:,:]=H_11
# transformMatrix03.m:1173
    H[12,:,:]=H_12
# transformMatrix03.m:1174
    H[13,:,:]=H_13
# transformMatrix03.m:1175
    H[14,:,:]=H_14
# transformMatrix03.m:1176
    H[15,:,:]=H_15
# transformMatrix03.m:1177
    H[16,:,:]=H_16
# transformMatrix03.m:1178
    H[17,:,:]=H_17
# transformMatrix03.m:1179
    H[18,:,:]=H_18
# transformMatrix03.m:1180
    H[19,:,:]=H_19
# transformMatrix03.m:1181
    H[20,:,:]=H_20
# transformMatrix03.m:1182
    H[21,:,:]=H_21
# transformMatrix03.m:1183
    H[22,:,:]=H_22
# transformMatrix03.m:1184
    H[23,:,:]=H_23
# transformMatrix03.m:1185
    H[24,:,:]=H_24
# transformMatrix03.m:1186
    H[25,:,:]=H_25
# transformMatrix03.m:1187
    H[26,:,:]=H_26
# transformMatrix03.m:1188
    H[27,:,:]=H_27
# transformMatrix03.m:1189
    H[28,:,:]=H_28
# transformMatrix03.m:1190
    H[29,:,:]=H_29
# transformMatrix03.m:1191
    H[30,:,:]=H_30
# transformMatrix03.m:1192
    H[31,:,:]=H_31
# transformMatrix03.m:1193
    H[32,:,:]=H_32
# transformMatrix03.m:1194
    H[33,:,:]=H_33
# transformMatrix03.m:1195
    H[34,:,:]=H_34
# transformMatrix03.m:1196
    H[35,:,:]=H_35
# transformMatrix03.m:1197
    H[36,:,:]=H_36
# transformMatrix03.m:1198
    H[37,:,:]=H_37
# transformMatrix03.m:1199
    H[38,:,:]=H_38
# transformMatrix03.m:1200
    H[39,:,:]=H_39
# transformMatrix03.m:1201
    H[40,:,:]=H_40
# transformMatrix03.m:1202
    H[41,:,:]=H_41
# transformMatrix03.m:1203
    H[42,:,:]=H_42
# transformMatrix03.m:1204
    H[43,:,:]=H_43
# transformMatrix03.m:1205
    H[44,:,:]=H_44
# transformMatrix03.m:1206
    H[45,:,:]=H_45
# transformMatrix03.m:1207
    H[46,:,:]=H_46
# transformMatrix03.m:1208
    H[47,:,:]=H_47
# transformMatrix03.m:1209
    H[48,:,:]=H_48
# transformMatrix03.m:1210
    H[49,:,:]=H_49
# transformMatrix03.m:1211
    H[50,:,:]=H_50
# transformMatrix03.m:1212
    H[51,:,:]=H_51
# transformMatrix03.m:1213
    H[52,:,:]=H_52
# transformMatrix03.m:1214
    H[53,:,:]=H_53
# transformMatrix03.m:1215
    H[54,:,:]=H_54
# transformMatrix03.m:1216
    H[55,:,:]=H_55
# transformMatrix03.m:1217
    H[56,:,:]=H_56
# transformMatrix03.m:1218
    H[57,:,:]=H_57
# transformMatrix03.m:1219
    H[58,:,:]=H_58
# transformMatrix03.m:1220
    H[59,:,:]=H_59
# transformMatrix03.m:1221
    #H
    Am=numpy.copy(A)
# transformMatrix03.m:1223
    #######################construct the rotation matrix########
    A=numpy.dot(63.43,pi) / 180
# transformMatrix03.m:1225
    B=numpy.dot(37.38,pi) / 180
# transformMatrix03.m:1226
    C=numpy.dot(79.18,pi) / 180
# transformMatrix03.m:1227
    D=numpy.dot(31.72,pi) / 180
# transformMatrix03.m:1228
    E=numpy.dot(58.29,pi) / 180
# transformMatrix03.m:1229
    #rot=[]
# transformMatrix03.m:1230
    rot=numpy.array([[0,0,1,numpy.dot(2,pi)],[0,0,1,numpy.dot(2,pi) / 5],[0,0,1,numpy.dot(- 2,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(2,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(- 2,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(2,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(- 2,pi) / 5],[- numpy.sin(A),0,numpy.cos(A),numpy.dot(2,pi) / 5],[- numpy.sin(A),0,numpy.cos(A),numpy.dot(- 2,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(2,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(- 2,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(2,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(- 2,pi) / 5],[0,0,1,numpy.dot(4,pi) / 5],[0,0,1,numpy.dot(- 4,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(4,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(- 4,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(4,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(- 4,pi) / 5],[- numpy.sin(A),0,numpy.cos(A),numpy.dot(4,pi) / 5],[- numpy.sin(A),0,numpy.cos(A),numpy.dot(- 4,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(4,pi) / 5],[numpy.dot(- numpy.sin(A),numpy.cos(numpy.dot(72,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(72,pi) / 180)),numpy.cos(A),numpy.dot(- 4,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(4,pi) / 5],[numpy.dot(numpy.sin(A),numpy.cos(numpy.dot(36,pi) / 180)),numpy.dot(- numpy.sin(A),numpy.sin(numpy.dot(36,pi) / 180)),numpy.cos(A),numpy.dot(- 4,pi) / 5],[numpy.sin(B),0,numpy.cos(B),numpy.dot(2,pi) / 3],[numpy.sin(B),0,numpy.cos(B),numpy.dot(- 2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(- 2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(- 2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(- 2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(B)),numpy.cos(B),numpy.dot(- 2,pi) / 3],[numpy.sin(C),0,numpy.cos(C),numpy.dot(2,pi) / 3],[numpy.sin(C),0,numpy.cos(C),numpy.dot(- 2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(- 2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(- 2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(2,pi) / 3],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(- 2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(C)),numpy.cos(C),numpy.dot(- 2,pi) / 3],[numpy.dot(numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(D)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(D)),numpy.cos(D),pi],[numpy.dot(- numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(D)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(D)),numpy.cos(D),pi],[- numpy.sin(D),0,numpy.cos(D),pi],[numpy.dot(- numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(D)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(D)),numpy.cos(D),pi],[numpy.dot(numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(D)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(D)),numpy.cos(D),pi],[numpy.sin(E),0,numpy.cos(E),pi],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(E)),numpy.dot(numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(E)),numpy.cos(E),pi],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(E)),numpy.dot(numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(E)),numpy.cos(E),pi],[numpy.dot(- numpy.cos(numpy.dot(36,pi) / 180),numpy.sin(E)),numpy.dot(- numpy.sin(numpy.dot(36,pi) / 180),numpy.sin(E)),numpy.cos(E),pi],[numpy.dot(numpy.cos(numpy.dot(72,pi) / 180),numpy.sin(E)),numpy.dot(- numpy.sin(numpy.dot(72,pi) / 180),numpy.sin(E)),numpy.cos(E),pi],[numpy.sin(numpy.dot(72,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180),0,pi],[numpy.sin(numpy.dot(36,pi) / 180),numpy.cos(numpy.dot(36,pi) / 180),0,pi],[0,1,0,pi],[- numpy.sin(numpy.dot(36,pi) / 180),numpy.cos(numpy.dot(36,pi) / 180),0,pi],[- numpy.sin(numpy.dot(72,pi) / 180),numpy.cos(numpy.dot(72,pi) / 180),0,pi]])
# transformMatrix03.m:1231
    R=numpy.zeros([60,3,3])
# transformMatrix03.m:1293
    for i in range(0,60):
        R[i,:,:]=rotationmatrix02.rotationmatrix(rot[i,0],rot[i,1],rot[i,2],rot[i,3])
# transformMatrix03.m:1295
    
    #R
##########################
#####################construct the mutual matrix##########
    P=numpy.zeros([60,60])
# transformMatrix03.m:1300
    
    op=numpy.zeros([60,1])
# transformMatrix03.m:1301
    
    P[0,0]=1
# transformMatrix03.m:1302
    op[0]=1
# transformMatrix03.m:1303
    P[1,1]=1
# transformMatrix03.m:1304
    op[1]=2
# transformMatrix03.m:1305
    P[4,2]=1
# transformMatrix03.m:1306
    op[2]=5
# transformMatrix03.m:1307
    P[24,3]=1
# transformMatrix03.m:1308
    op[3]=25
# transformMatrix03.m:1309
    P[48,4]=1
# transformMatrix03.m:1310
    op[4]=49
# transformMatrix03.m:1311
    P[42,5]=1
# transformMatrix03.m:1312
    op[5]=43
# transformMatrix03.m:1313
    P[31,6]=1
# transformMatrix03.m:1314
    op[6]=32
# transformMatrix03.m:1315
    P[49,7]=1
# transformMatrix03.m:1316
    op[7]=50
# transformMatrix03.m:1317
    P[7,8]=1
# transformMatrix03.m:1318
    op[8]=8
# transformMatrix03.m:1319
    P[32,9]=1
# transformMatrix03.m:1320
    op[9]=33
# transformMatrix03.m:1321
    P[23,10]=1
# transformMatrix03.m:1322
    op[10]=24
# transformMatrix03.m:1323
    P[8,11]=1
# transformMatrix03.m:1324
    op[11]=9
# transformMatrix03.m:1325
    P[41,12]=1
# transformMatrix03.m:1326
    op[12]=42
# transformMatrix03.m:1327
    P[2,13]=1
# transformMatrix03.m:1328
    op[13]=3
# transformMatrix03.m:1329
    P[3,14]=1
# transformMatrix03.m:1330
    op[14]=4
# transformMatrix03.m:1331
    P[27,15]=1
# transformMatrix03.m:1332
    op[15]=28
# transformMatrix03.m:1333
    P[11,16]=1
# transformMatrix03.m:1334
    op[16]=12
# transformMatrix03.m:1335
    P[14,17]=1
# transformMatrix03.m:1336
    op[17]=15
# transformMatrix03.m:1337
    P[38,18]=1
# transformMatrix03.m:1338
    op[18]=39
# transformMatrix03.m:1339
    P[36,19]=1
# transformMatrix03.m:1340
    op[19]=37
# transformMatrix03.m:1341
    P[58,20]=1
# transformMatrix03.m:1342
    op[20]=59
# transformMatrix03.m:1343
    P[56,21]=1
# transformMatrix03.m:1344
    op[21]=57
# transformMatrix03.m:1345
    P[54,22]=1
# transformMatrix03.m:1346
    op[22]=55
# transformMatrix03.m:1347
    P[52,23]=1
# transformMatrix03.m:1348
    op[23]=53
# transformMatrix03.m:1349
    P[29,24]=1
# transformMatrix03.m:1350
    op[24]=30
# transformMatrix03.m:1351
    P[20,25]=1
# transformMatrix03.m:1352
    op[25]=21
# transformMatrix03.m:1353
    P[40,26]=1
# transformMatrix03.m:1354
    op[26]=41
# transformMatrix03.m:1355
    P[43,27]=1
# transformMatrix03.m:1356
    op[27]=44
# transformMatrix03.m:1357
    P[47,28]=1
# transformMatrix03.m:1358
    op[28]=48
# transformMatrix03.m:1359
    P[45,29]=1
# transformMatrix03.m:1360
    op[29]=46
# transformMatrix03.m:1361
    P[30,30]=1
# transformMatrix03.m:1362
    op[30]=31
# transformMatrix03.m:1363
    P[33,31]=1
# transformMatrix03.m:1364
    op[31]=34
# transformMatrix03.m:1365
    P[6,32]=1
# transformMatrix03.m:1366
    op[32]=7
# transformMatrix03.m:1367
    P[9,33]=1
# transformMatrix03.m:1368
    op[33]=10
# transformMatrix03.m:1369
    P[22,34]=1
# transformMatrix03.m:1370
    op[34]=23
# transformMatrix03.m:1371
    P[51,35]=1
# transformMatrix03.m:1372
    op[35]=52
# transformMatrix03.m:1373
    P[12,36]=1
# transformMatrix03.m:1374
    op[36]=13
# transformMatrix03.m:1375
    P[26,37]=1
# transformMatrix03.m:1376
    op[37]=27
# transformMatrix03.m:1377
    P[39,38]=1
# transformMatrix03.m:1378
    op[38]=40
# transformMatrix03.m:1379
    P[13,39]=1
# transformMatrix03.m:1380
    op[39]=14
# transformMatrix03.m:1381
    P[59,40]=1
# transformMatrix03.m:1382
    op[40]=60
# transformMatrix03.m:1383
    P[35,41]=1
# transformMatrix03.m:1384
    op[41]=36
# transformMatrix03.m:1385
    P[50,42]=1
# transformMatrix03.m:1386
    op[42]=51
# transformMatrix03.m:1387
    P[55,43]=1
# transformMatrix03.m:1388
    op[43]=56
# transformMatrix03.m:1389
    P[25,44]=1
# transformMatrix03.m:1390
    op[44]=26
# transformMatrix03.m:1391
    P[44,45]=1
# transformMatrix03.m:1392
    op[45]=45
# transformMatrix03.m:1393
    P[46,46]=1
# transformMatrix03.m:1394
    op[46]=47
# transformMatrix03.m:1395
    P[34,47]=1
# transformMatrix03.m:1396
    op[47]=35
# transformMatrix03.m:1397
    P[5,48]=1
# transformMatrix03.m:1398
    op[48]=6
# transformMatrix03.m:1399
    P[21,49]=1
# transformMatrix03.m:1400
    op[49]=22
# transformMatrix03.m:1401
    P[28,50]=1
# transformMatrix03.m:1402
    op[50]=29
# transformMatrix03.m:1403
    P[10,51]=1
# transformMatrix03.m:1404
    op[51]=11
# transformMatrix03.m:1405
    P[37,52]=1
# transformMatrix03.m:1406
    op[52]=38
# transformMatrix03.m:1407
    P[57,53]=1
# transformMatrix03.m:1408
    op[53]=58
# transformMatrix03.m:1409
    P[53,54]=1
# transformMatrix03.m:1410
    op[54]=54
# transformMatrix03.m:1411
    P[19,55]=1
# transformMatrix03.m:1412
    op[55]=20
# transformMatrix03.m:1413
    P[18,56]=1
# transformMatrix03.m:1414
    op[56]=19
# transformMatrix03.m:1415
    P[17,57]=1
# transformMatrix03.m:1416
    op[57]=18
# transformMatrix03.m:1417
    P[16,58]=1
# transformMatrix03.m:1418
    op[58]=17
# transformMatrix03.m:1419
    P[15,59]=1
# transformMatrix03.m:1420
    op[59]=16
# transformMatrix03.m:1421
    ############representation in Cartian Coordinates########
    T=numpy.zeros([60,180,3])
# transformMatrix03.m:1424
    for i in range(0,60):
        T[i,:,:]=numpy.kron(P[:,i,None],R[i,:,:])
# transformMatrix03.m:1426
    return Am, T1, T2, G, H, T, P, R, op#, normAm, normT1, normT2, normG, normH 