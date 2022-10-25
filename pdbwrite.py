
import numpy

def pdbwrites(writefile,bildfile,postnL,pdb_storenL,n2,correx,correy,correz):
    fw1=open('pdb_b.pdb','w')

    for i in range(0,n2):
        fw1.write('%27s%11.3f%8.3f%8.3f%26s' % (pdb_storenL[i][0:27],postnL[i,0],postnL[i,1],postnL[i,2],pdb_storenL[i][54:80])+'\r\n')
        #(str(pdb_storenL[i][0:26])+' '+str(postnL[i,0])+' '+str(postnL[i,1])+' '+str(postnL[i,2])+' '+str(pdb_storenL[i][54:79])+'\r\n')
    fw1.close()
    postaddnL=numpy.zeros([n2,3])

    for i in range(0,n2):
        postaddnL[i,0] = postnL[i,0] + numpy.dot(250,correx[i])
        postaddnL[i,1] = postnL[i,1] + numpy.dot(250,correy[i])
        postaddnL[i,2] = postnL[i,2] + numpy.dot(250,correz[i])
    
    fw2=open(writefile,'w')
    for i in range(0,n2):
        fw2.write('%27s%11.3f%8.3f%8.3f%26s' % (pdb_storenL[i][0:27],postaddnL[i,0],postaddnL[i,1],postaddnL[i,2],pdb_storenL[i][54:80])+'\r\n')
    fw2.close()
    
    fw3=open(bildfile,'w')
    for i in range(0,n2):
        #fw3.write('.arrow  '+str(postnL[i,0])+' '+str(postnL[i,1])+' '+str(postnL[i,2])+' '+str(postaddnL[i,0])+' '+str(postaddnL[i,1])+' '+str(postaddnL[i,2])+' 0.1 0.4 0.75\r\n')
        fw3.write('%6s%11.3f%11.3f%11.3f%11.3f%11.3f%11.3f%13s\n' % ('.arrow',postnL[i,0],postnL[i,1],postnL[i,2],postaddnL[i,0],postaddnL[i,1],postaddnL[i,2],' 0.1 0.4 0.75\n'))
    fw3.close()    