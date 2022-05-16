# -*- coding: UTF-8 -*-

def LoadFromFileAsDict(filename):
	f=open(filename,"r")
	dicts=f.readlines()
	fielddefs=dicts[0].strip("\r\n").split(",")
	dicts.pop(False)
	result=[]
	for row in dicts:
		values=row.strip("\r\n").split(",")
		dict={}
		for i in range(len(values)):
			dict[fielddefs[i]]=values[i]
		result.append(dict)
	f.close()
	return result

def SaveToFileAsDict(filename,dicts):
	f=open(filename,"w")
	fielddefs=list(dicts[0].keys())
	fieldcount=len(fielddefs)
	#f.write(str(fielddefs).strip("[]")+"\n")
	stmp=""
	for fname in fielddefs:
		stmp+=","+fname
	f.write(stmp[1:]+"\n")
	for row in dicts:
		stmp=""
		for fn in range(fieldcount):
			stmp+=","+str(row[fielddefs[fn]])
		stmp=stmp[1:]+"\n"
		f.write(stmp)
	f.close()


def SaveToFileAsList(filename,list,fielddefs=[]):
	f=open(filename,"w")
	fieldcount=len(fielddefs)
	#f.write(str(fielddefs).strip("[]")+"\n")
	stmp=""
	for fname in fielddefs:
		stmp+=","+fname
	f.write(stmp[1:]+"\n")
	for row in list:
		stmp=""
		for fn in range(fieldcount):
			stmp+=","+str(row[fn])
		stmp=stmp[1:]+"\n"
		f.write(stmp)
	f.close()













