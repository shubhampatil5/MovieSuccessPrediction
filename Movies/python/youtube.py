import string
from cmath import *

fi=open("final.tsv")
st=fi.read()
list1=st.split('\n')
list1.remove('')
list2=[]
for i in list1:
	buff1=i.split('\t')
	n=int(buff1[9])
	f=log10(n)
	s=i.replace(buff1[9],str(f).replace('+0j)','').replace('(',''))
	list2.append(s)

fi.close()
fi=open('final1.tsv','w')
for i in list2:
	fi.write(i+'\n')
fi.close()
