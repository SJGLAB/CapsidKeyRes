# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:24:03 2022

@author: hp
"""

# -*- coding: utf-8 -*-
print('this is pdbreadfunction')
import numpy

def str01(pdblist):
    pdbstr = ''.join(str(e) for e in pdblist)
    return pdbstr
def pdbread(filename=None):
    import numpy
    dictres = {
        'ALA': 'A', 'CYS': 'C', 'ASP': 'D', 'GLU': 'E',
        'PHE': 'F', 'GLY': 'G', 'HIS': 'H', 'LYS': 'K',
        'ILE': 'I', 'LEU': 'L', 'MET': 'M', 'ASN': 'N',
        'PRO': 'P', 'GLN': 'Q', 'ARG': 'R', 'SER': 'S',
        'THR': 'T', 'VAL': 'V', 'TYR': 'Y', 'TRP': 'W'}
    position = numpy.mat(([0.0,0.0,0.0]))
    resall = []
    resnames=[]
    rname = []
    posall = numpy.mat([[0.0,0.0,0.0]])
    pdb_store = []
    chain_id = []

    with open(filename,'r') as fid1:
         for pdb in fid1:
             if pdb[0] =='E' and pdb[1]=='N' and pdb[2]=='D' and pdb[3] ==' ' and pdb[4] ==' ':
                 break
             elif len(pdb) < 35:
                   continue
             elif (pdb[0:4] =='ATOM') and (pdb[13] =='C') and (pdb[14] =='A'):
                   if pdb[21]=='A' and (int(pdb[22:26]))<9:
                       continue
                   pdbname =pdb[17:20]
                   resname=dictres[pdbname]
                   resnames.append(resname)
                   position[0:3] = [float(str01(pdb[29:38])), float(str01(pdb[38:46])), float(str01(pdb[46:54]))]
                   resnumber = pdb[22:26]
                   resid = pdb[21]
                   resall.append(resnumber)
                   rname.append(pdbname)
                   posall =numpy.vstack((posall,position))
                   pdb_store.append(pdb)
                   chain_id.append(resid)
         posall=numpy.delete(posall,0,axis=0)
         numpy.save('resalldat.npy',resall)
         numpy.save('posalldat.npy',posall)
         numpy.save('pdbstore.npy',pdb_store)
    fid1.close()
    return posall,resall,rname,pdb_store,chain_id
...
#after the calculattins of above all,
...
def repdbread(filename,perturbation_sum,cutresd):#,*args,**kwargs):
    posall,resall,rname,pdb_store,chain_id = pdbread(filename)
    #perturbation_sum=numpy.load('perturbationsumdat.npy')
    key_res_id=[]
    for e in range(0,len(perturbation_sum)):
        if perturbation_sum[e] > cutresd:
           key_res_id.append(e)  
    numpy.save('key_res_iddat.npy',key_res_id)
    numbers = []
    c_id = []
    for i in range(0,len(key_res_id)):
        key_resii=int(key_res_id[i])
        number = resall[key_resii]
        numbers.append(number)
        c_id.append(chain_id[key_res_id[i]])
    numpy.save('numbers_dat.npy',numbers)
    numpy.save('c_id_dat.npy',c_id)
    #print('numbers=',numbers)
    return numbers,c_id