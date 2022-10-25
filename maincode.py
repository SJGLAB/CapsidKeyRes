# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:35:14 2022

@author: hp
"""

# -*- coding: utf-8 -*-
#calmainflow
import numpy
import groupanm02,calRgmsRg02,pdbread02,modesshow#,pdbwrite,transformMatrix03,rotationmatrix02,juli02
pdbfile='1POV.pdb'
postall,cutoff,eAm,vAm,eT1,vT1,eT2,vT2,eG,vG,eH,vH,Am,T1,T2,G,H,Digmatrix,R,resn_mon,nAm,nT1,nT2,nG,nH,op,n2 = groupanm02.groupanm(pdbfile)#,normAm_u,normT1_u,normT2_u,normG_u,normH_u
print('this is first step')
perturbation_sum,ms_r_PQ,Ueig = calRgmsRg02.calRgmsRg(postall,cutoff,eAm,vAm,eT1,vT1,eT2,vT2,eG,vG,eH,vH,Am,T1,T2,G,H,Digmatrix,R,resn_mon,nAm,nT1,nT2,nG,nH,op,n2)  
print('请调试到这里，之后找到cutresd值再算以下')
#if __name__=='__main__':
cutresd=float(input('请输入resd：'))
filename=pdbfile
numbers,c_id = pdbread02.repdbread(filename,perturbation_sum,cutresd)
print('c_id=',c_id)
print('numbers=',numbers)
print('you have finished calculation')
print('next one is modesshowdata')
modesshow.modesshows(pdbfile,Ueig)
print('The work is done')
