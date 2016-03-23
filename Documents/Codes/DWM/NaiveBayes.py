from __future__ import division
from math import log
import operator
import csv
import copy
from sys import argv
d = []
d = [['Outlook','Temperature','Humidity','Wind','PlayTennis'],\
	 ['Sunny'	,'Hot'	,'High'		,'Weak'		,'No'],\
	 ['Sunny'	,'Hot'	,'High'		,'Strong'	,'No'],\
	 ['Overcast','Hot'	,'High'		,'Weak'		,'Yes'],\
	 ['Rain'	,'Mild'	,'High'		,'Weak'		,'Yes'],\
	 ['Rain'	,'Cool'	,'Normal'	,'Weak'		,'Yes'],\
	 ['Rain'	,'Cool'	,'Normal'	,'Strong'	,'No'],\
	 ['Overcast','Cool'	,'Normal'	,'Strong'	,'Yes'],\
	 ['Sunny'	,'Mild'	,'High'		,'Weak'		,'No'],\
	 ['Sunny'	,'Cool'	,'Normal'	,'Weak'		,'Yes'],\
	 ['Rain'	,'Mild'	,'Normal'	,'Weak'		,'Yes'],\
	 ['Sunny'	,'Mild'	,'Normal'	,'Strong'	,'Yes'],\
	 ['Overcast','Mild'	,'High'		,'Strong'	,'Yes'],\
	 ['Overcast','Hot'	,'Normal'	,'Weak'		,'Yes'],\
	 ['Rain'	,'Mild'	,'High'		,'Strong'	,'No']]
#GLOBALS
tl = []
t_titles = d[0]
cls = {}
classes = {}
n = len(d)-1
ctitle = t_titles[len(d[0])-1]
init = 1
tree = {}
trap = 0
classes = {}
sample = {}
pCi = {}
pSi = {}	

def init_classes(dset):
	global n,trap
	cls = {}
	dataset = copy.copy(dset)
	title = dataset[0]
	del dataset[0]
	for p in title:
		index = title.index(p)
		ii = title.index(ctitle)
		cld = {}
		cnt = {}
		cl = []
		count = []
		countYN = []
		m = 0
		for lists in dataset:
			ts = lists[index]
			if ts not in cl:
				cl.append(ts)
				i = cl.index(ts)
				if lists[ii] in ['yes','Yes','YES']:
					countYN.append([1,0])
				elif lists[ii] in ['no','No','NO']:
					countYN.append([0,1])
				count.append(1)
				i = cl.index(ts)	
			else:
				for val in cl:
					ind = cl.index(val)
					if ts == val:
						count[ind] += 1
						if lists[ii] in ['yes','Yes','YES']:
							countYN[ind][0] += 1
						elif lists[ii] in ['no','No','NO']:
							countYN[ind][1] += 1
					
			q = cl.index(ts)	
			m += 1 
	 	for x in range(len(cl)):
			cnt[count[x]]  = countYN[x]
			tcls = cl[x]
			cld[tcls] = cnt[count[x]]
		cls[p] = cld
		if n < m:
			n = m
	return cls

def prob_classifier():
	global classes 
	pCi = {}
	tmp = {}
	classes = init_classes(d)
	for cls in classes[ctitle]:
		if 0 in classes[ctitle][cls]:
			j = 0
			for i in classes[ctitle][cls]:
				j += i
			tmp[cls] = j/n
	pCi[ctitle] = tmp
	return pCi

def prob_sample():
	global classes,sample
	pSi = {}
	for k,cls in enumerate(classes[ctitle]):
		if 0 in classes[ctitle][cls]:
			j = 0
			for i in classes[ctitle][cls]:
				j += i
		tmp2 = {}
		for title in sample:
			tmp2[title] = classes[title][sample[title]][k]/j
		pSi[cls] = tmp2
	return pSi

def prob_X():
	global pSi
	pXi = {}
	for val in pSi:
		j = 1
		for p in pSi[val]:
			j = j*pSi[val][p]
		pXi[val] = j
	return pXi	

def print_prediction():
	ls = []
	for val in pXi:
		ls.append(pXi[val])
	inv_dict = {v: k for k ,v in pXi.items()}
	print "Prediction is :",inv_dict[max(ls)]
	

if __name__ == "__main__":
	dataset = copy.copy(d)
	title = dataset[0]
	del dataset[0]
	sample = {'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Strong'} #Sample Dataset as Input
	pCi = prob_classifier()
	print pCi,"\n"
	pSi = prob_sample()
	print pSi,"\n"
	pXi = prob_X()
	print pXi,"\n"
	print_prediction()





