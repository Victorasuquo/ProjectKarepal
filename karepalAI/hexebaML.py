from datetime import datetime
import os
import random
import requests
import sqlite3,time
from sqlite3 import Error
from dotenv import load_dotenv
load_dotenv(".env")
clicktablename = os.getenv("CLICK_TABLE_NAME")
password = os.getenv("SERVER2_PASSWORD")
url = os.getenv("URL")
# import pandas as pd
def update_file_in_parent_folder(content,filename,filetype):
    hedgefile = open(str("{}.{}".format(filename,filetype)),"w+")
    hedgefile.write(content)
    hedgefile.close()
    
def read_brain_data(brain_data):
    
    datax =  brain_data
    var = []
    ld = len(datax)
    data = ""
    for i in range(ld):
        dv =  datax[i]
        
        if((dv!=",")and(dv!="")):
            data = data + dv
        if((dv==",")or(i==ld-1)):
            if(data != ""):
                var.append(data)
                data = ""
    return var
def delete_file_in_folder(filename,foldername,filetype):
    v ="f"
    try:
        v=""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        check = read_file(filename,foldername)
    except Exception:
        v=""
    try:

     
        os.remove(str("{}/{}.{}".format(foldername,filename,filetype)))
    except Exception:
        pass
def delete_parent_file(filename,filetype):
    try:
        os.remove(str("{}.{}".format(filename,filetype)))
    except Exception:
        pass
def read_file_in_parent_folder(filename,filetype):
    v ="f"
    try:
        v = ""
        dir = os.getcwd()
       
    except Exception:
        v=""
    try:
        hedgefile = open(str("{}.{}".format(filename,filetype)),"r")
    except Exception:
        hedgefile = open(str("{}.{}".format(filename,filetype)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}.{}".format(filename,filetype)),"r")
    brain = hedgefile.read()
    return brain

def read_file_by_filetype(filename,foldername,filetype):
    v ="f"
    try:
        v = ""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
       
    except Exception:
        v=""
    try:
        hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"r")
    brain = hedgefile.read()
    return brain


def read_file(filename,foldername):
    v ="f"
    try:
        v = ""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
       
    except Exception:
        v=""
    try:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    brain = hedgefile.read()
    return brain

def read_file_line(lineid,filename,foldername):
    v ="f"
    try:
        v = ""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
       
    except Exception:
        v=""
    try:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    lines = ""


    with open(str("{}/{}.txt".format(foldername,filename)),"r") as hedgefile:
        lines = hedgefile.readlines()

    return lines[lineid]

    

def total_file_lines(filename,foldername):
    v ="f"
    try:
        v = ""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
       
    except Exception:
        v=""
    try:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    lines = ""
    with open(str("{}/{}.txt".format(foldername,filename))) as hedgefile:
        lines = hedgefile.readlines()
    
    return len(lines)


def update_file_by_type(content,filename,foldername,filetype):
    v ="f"
    try:
        v=""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        check = read_file_by_filetype(filename,foldername,filetype)
    except Exception:
        v=""
    try:
        content = str(content)
    except Exception:
        content = content
    try:

        hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.{}".format(foldername,filename,filetype)),"w+")
    hedgefile.write(content)
    hedgefile.close()


def update_file(content,filename,foldername):
    v ="f"
    try:
        v=""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        check = read_file(filename,foldername)
    except Exception:
        v=""
    try:
        content = str(content)
    except Exception:
        content = content
    try:

        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
    hedgefile.write(content)
    hedgefile.close()

def append_file(content,filename,foldername):
    v ="f"
    try:
        v=""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        check = read_file(filename,foldername)
    except Exception:
        v=""
    try:
        content = str(content)
    except Exception:
        content = content
    try:

        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    con = read_file(filename,foldername)
    if(con == ""):
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"a+")
        hedgefile.write("{}".format(content.rstrip()))
        hedgefile.close()
    else:
        hedgefile = open(str("{}/{}.txt".format(foldername,filename)),"a+")
        hedgefile.write("\n{}".format(content.rstrip()))
        hedgefile.close()




def set_time(time,filename,foldername):
    v ="f"
    try:
        v = read_file(filename,foldername)
    except Exception as e:
        update_file("",filename,foldername)
    dt = str(time)
    ldt = len(dt)
    n = ""
    v = "start"
    for i in range(ldt):
        ch = dt[i]
        if(ch == "."):
            v = "end"
        if(v=="start"):
            n=n+ch
    timex = n 
    fw_1 = open("{}/{}.txt".format(foldername,filename),"w+")
    fw_1.write(timex)
    fw_1.close()

def set_now_time(filename,foldername):
    v ="f"
    time = datetime.now()
    try:
        v = read_file(filename,foldername)
    except Exception as e:
        update_file("",filename,foldername)
    dt = str(time)
    ldt = len(dt)
    n = ""
    v = "start"
    for i in range(ldt):
        ch = dt[i]
        if(ch == "."):
            v = "end"
        if(v=="start"):
            n=n+ch
    timex = n 
    fw_1 = open("{}/{}.txt".format(foldername,filename),"w+")
    fw_1.write(timex)
    fw_1.close()
def clean_time(time):
    v ="f"
    dt = str(time)
    ldt = len(dt)
    n = ""
    v = "start"
    for i in range(ldt):
        ch = dt[i]
        if(ch == "."):
            v = "end"
        if(v=="start"):
            n=n+ch
    timex = n 
    return timex

def read_brain(foldername,part):
    v ="f"
    try:
        v=""
        dir = os.getcwd()
        foldername = foldername
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        data = data
        check = read_brain(foldername,part)
    except Exception:
        v=""

    try:

        hedgefile = open(str("{}/{}.txt".format(foldername,part)),"r")
    except Exception:
        hedgefile = open(str("{}/{}.txt".format(foldername,part)),"w+")
        hedgefile.write(str(""))
        hedgefile.close()
    hedgefile = open(str("{}/{}.txt".format(foldername,part)),"r")
    brain = hedgefile.read()
    datax =  brain
    var = []
    ld = len(datax)
    data = ""
    for i in range(ld):
        dv =  datax[i]
        
        if((dv!=",")and(dv!="")):
            data = data + dv
        if((dv==",")or(i==ld-1)):
            if(data != ""):
                var.append(data)
                data = ""
    return var
def learn_brain(data,part,folder):
    try:
        data = str(data)
    except Exception:
        data = data
    v ="f"

    try:
        v="x"
        data = data
        check = read_brain(folder,part)
    except Exception:
        v="x"
        dir = os.getcwd()
        foldername = folder
        path = os.path.join(dir,foldername)
        os.mkdir(path)
        data = data
        check = read_brain(folder,part)

    l = len(check)
    a = 0
    b=0
    n = 0
    for i in range(l):
        datay = check[i]
    
        if((datay != data)):
            n=n+1
        if((datay == data)):
            b = 1
        if((i==(l-1))):
            a = 1
        if((data != datay)and(b==0)and(a==1)):

            fw_2 = open(str("{}/{}.txt".format(folder,part)),"a+")
            fw_2.write(str(",{}".format(data)))
            fw_2.close()
            return 0
    if(l==0):
        fw_1 = open(str("{}/{}.txt".format(folder,part)),"a+")
        fw_1.write(",{}".format(data))
        fw_1.close()
        return 0

        
def unlearn_brain(data,part,folder):
    try:
        data = str(data)
    except Exception:
        data = data
    v ="f"
    data = data
    check = read_brain(folder,part)
    l = len(check)
    #prfloat(l)
#    time.sleep(2)
    a=0
    b=0
    for i in range(l):
        datay = check[i]

     #   if((data == datay)and(i==(l-1))):
        if((datay == data)):
            b = 1
        if((i==(l-1))):
            a = 1
        if((b==1)and(a==1)):
            hedgefile = open(str("{}/{}.txt".format(folder,part)),"r")
            txt = hedgefile.read()
            data = data
            
            try:

                txt = txt.replace(data,"")
            except Exception:
                v=""
            try:

                txt = txt.replace(",,",",")
            except Exception:
                v=""

            fw_1 = open(str("{}/{}.txt".format(folder,part)),"w+")
            fw_1.write(txt)
            fw_1.close()

def check_brain(data,filename,folder):
    v="x"
    n = 0
    a=0
    b=0
    response = 2
    vx = read_brain(folder,filename)
    l = len(vx)
    for i in range(l):
        vy = vx[i]
        # vx = vy*2

        if((str(vy) == str(data))):
            b = 1
        if((i==(l))):
            a = 1

        if((b == 1)and(a==0)):
            response = 1   

        if((b==0)and((a==1))):
            response = 0
        
    if(response==2):
        return 0
    if(l>0):
        return response


def fetch_brain_id(data,filename,folder):
    v="x"
    n = 0
    a=0
    b=0
    response = 2
    vx = read_brain(folder,filename)
    l = len(vx)
    for i in range(l):
        vy = vx[i]
        # vx = vy*2

        if((float(vy) == float(data))):
            b = i
        if((i==(l))):
            a = 1



        
    if(l>0):
        return b

def rand(a,b,filename,foldername):
    a = a
    b = b
    p=0
    val = random.randint(a,b)
    valcheck = check_brain(str(val),filename,foldername)
    valmem = read_brain(foldername,filename)
    n = read_file("{}randtotal".format(filename),foldername)
    if(n==""):
        n=0
    else:
        n=float(n)
    lent = len(valmem)
    rangex = (b-a)+1
    if((valcheck==0)or(lent==0)):
        learn_brain(str(val),filename,foldername)
        n=float(n)+1
        update_file(str(n),"{}randtotal".format(filename),foldername)
        p = 1
        
    if(n==rangex):
        update_file("",filename,foldername)
        update_file("","{}randtotal".format(filename),foldername)
    if(p==1):
        return val
    if(p==0):
        return rand(a,b,filename,foldername)


def c_rand(foldername,filename,a,b):
    a = a
    b = b
    p=0
    val = random.randint(a,b)
    valcheck = check_brain(str(val),filename,foldername)
    valmem = read_brain(foldername,filename)
    n = read_file("{}randtotal".format(filename),foldername)
    if(n==""):
        n=0
    else:
        n=float(n)
    lent = len(valmem)
    rangex = (b-a)+1
    if((valcheck==0)or(lent==0)):
        learn_brain(str(val),filename,foldername)
        n=float(n)+1
        update_file(str(n),"{}randtotal".format(filename),foldername)
        p = 1
        
    if(n==rangex):
        update_file("",filename,foldername)
        update_file("","{}randtotal".format(filename),foldername)
    if(p==1):
        return val
    if(p==0):
        return c_rand(foldername,filename,a,b)

def c_choice(foldername,filename,choice):

    p=0
    val = random.choice(choice)
    valcheck = check_brain(str(val),filename,foldername)
    valmem = read_brain(foldername,filename)
    n = read_file("{}randtotal".format(filename),foldername)
    if(n==""):
        n=0
    else:
        n=float(n)
    lent = len(valmem)
    rangex = len(choice)
    if((lent==0)):
        learn_brain(str(val),filename,foldername)
        n=float(n)+1
        update_file(str(n),"{}randtotal".format(filename),foldername)
        p = 1
    if((valcheck==0)and(lent!=0)):
        learn_brain(str(val),filename,foldername)
        n=float(n)+1
        update_file(str(n),"{}randtotal".format(filename),foldername)
        p = 1  
    if(n>=rangex):
        update_file("",filename,foldername)
        update_file("","{}randtotal".format(filename),foldername)
    if(p==1):
        return val
    if(p==0):

        return c_choice(foldername,filename,choice)





def time_difference(timefile,foldername):
    v = "TEST"
    tstop_time = read_file(timefile,foldername)
    timern = datetime.now()
    tstop_time = datetime.strptime(tstop_time, '%Y-%m-%d %H:%M:%S')
    time_delta1 = (timern - tstop_time)
    total_seconds1 = time_delta1.total_seconds()
    tstop_secs = total_seconds1
    return tstop_secs


def read_precision(value):
    strx = str(value)
    inx = 0
    a = 0
    b = 0
    precision = 0
    l = len(strx)
    for i in range(l):
        vx = strx[i]
        if(vx == "."):
            a = inx + 1
        if(a==1):
            b=b+1
    precision = b-1
    return precision


def reduce_precision(value,precision):
    val = round(value,precision)
    return val


def adjust_precision(outputk,inputk):
    inputval = read_precision(inputk)
    outputval = read_precision(outputk)
    newval = reduce_precision(inputk,outputval)
    return newval


def update_brain(location,newdata,part,folder):

    data_x = read_brain(folder,part)
    braindata = data_x
    braindata[location]=newdata
    update_file(braindata,part,folder)
    rawdata = read_file(part,folder)
    lent = len(rawdata)
    newstr = ""
    for i in range(lent):
        char = rawdata[i]
        if((char != "[")and(char != "]")and(char != "'")and(char != " ")):
            newstr = newstr+char
    update_file(newstr,part,folder)
    return "Brain updated Successfully"

def readbrain_with_id(id,file,folder):
    data = read_brain(folder,file)
    data_of_id = data[id]
    return data_of_id
def readbrain_with_idname(idname,file,folder):
    data = read_brain(folder,"{}id".format(file))
    datax = read_brain(folder,"{}".format(file))
    ind = data.index(idname)
    data_of_id = datax[ind]
    return data_of_id
def free_learn_brain(data,filename,folder):
    lastdata = read_file(filename,folder)
    newdata = str(lastdata) + ",{}".format(data)
    update_file(newdata,filename,folder)
    return "DONE!"

def free_learn_brain_with_id(data,filename,folder):
    lastdata = read_file(filename,folder)
    newdata = str(lastdata) + ",{}".format(data)
    update_file(newdata,filename,folder)
    
    filenameid = "{}id".format(filename)
    datalength = len(read_brain(folder,filename))
    lastiddata = read_file("{}id".format(filename),folder)
    newdataid = str(lastiddata) + ",data{}".format(datalength)
    update_file(newdataid,filenameid,folder)
    return "DONE!"

def read_last_braindata(modulename,foldername):
    alldata = read_brain(foldername,modulename)
    l = len(alldata)
    return alldata[l-1]

def read_first_braindata(modulename,foldername):
    alldata = read_brain(foldername,modulename)
    l = len(alldata)
    return alldata[0]

def read_last_braindata_ignore_result(modulename,foldername):
    allid = read_brain(foldername,"{}id".format(modulename))
    alldata = read_brain(foldername,modulename)
    l = len(allid)
    if(l>0):
        
        if(allid[l-1]=="result"):
            lastdata = alldata[l-2]
        else:
            lastdata = alldata[l-1]
        return lastdata
    else:
        l = len(alldata)
        lastdata = alldata[l-1]
        return lastdata

def learn_brain_with_id(idname,folder,filename,inputdata):
    brain = read_brain(folder,"{}id".format(filename))
    brainmain = read_brain(folder,"{}".format(filename))
    if((brain==[])and(brainmain==[])):
        learn_brain(inputdata,filename,folder)
        learn_brain(idname,"{}id".format(filename),folder)

    else:

        try:
            
            nameid = brain.index(idname)
    #        lastdata = readbrain_with_id(nameid,filename,folder)
            update_brain(nameid,inputdata,filename,folder)
            return "DONE!"
        except Exception as e:
            free_learn_brain(inputdata,filename,folder)
            learn_brain(idname,"{}id".format(filename),folder)
            return e
        
def update_brain_with_idname(idname,newdata,part,folder):
    newdata = str(newdata)
    brain = read_brain(folder,"{}id".format(part))
    location = brain.index(idname)
    data_x = read_brain(folder,part)
    braindata = data_x
    braindata[location]=newdata
    update_file(braindata,part,folder)
    rawdata = read_file(part,folder)
    lent = len(rawdata)
    newstr = ""
    for i in range(lent):
        char = rawdata[i]
        if((char != "[")and(char != "]")and(char != "'")and(char != " ")and(char != '"')):
  # if the is an issue uncomment the top and comment the down
    #    if((char != "[")and(char != "]")and(char != "'")and(char != '"')):
            newstr = newstr+char
    newstr = newstr.replace("\\n","")
    update_file(newstr,part,folder)
    return "Brain updated Successfully"

def store_in_module(inputdata,iddata,filename,folder):
    append_file(inputdata,filename,folder)
    update_file(iddata,"{}id".format(filename),folder)
    return "DONE!"

def update_module(name_of_module,folder,data_total_no):
    res = ""
    for i in range(data_total_no):
        dataid = input("WHAT'S THE ID OF DATA {}?".format(i))
        dataval = input("WHAT'S THE {} VALUE?".format(dataid))
        learn_brain_with_id(dataid,folder,name_of_module,dataval)
    return "DONE!"

def read_storage_by_lineid(lineid,filename,folder):
    tt = total_file_lines(filename,folder)
    data = read_file_line(lineid,filename,folder)
    iddata = read_file("{}id".format(filename),folder)
    update_file(data,"temporaryvirtual",folder)
    update_file(iddata,"temporaryvirtualid",folder)
    braindata = read_brain(folder,"temporaryvirtual")
    try:

        if(braindata==["\n"]):
            lineid=lineid+1
            update_file(lineid,"temporaryvirtualline",folder)
            return read_storage_by_lineid(lineid,filename,folder)
    except Exception:

        
        if(braindata==[]):
            lineid=lineid+1
            update_file(lineid,"temporaryvirtualline",folder)
            return read_storage_by_lineid(lineid,filename,folder)
        
    return braindata

def read_storage_by_lineid_raw(lineid,filename,folder):
    data = read_file_line(lineid,filename,folder)
    iddata = read_file("{}id".format(filename),folder)
    update_file(data,"temporaryvirtual",folder)
    update_file(iddata,"temporaryvirtualid",folder)
    braindata = read_brain(folder,"temporaryvirtual")
    return braindata

def read_storage_with_idname_lineid(idname,lineid,filename,folder):
    idbrain = read_brain(folder,"{}id".format(filename))
    id = idbrain.index(idname)
    data = read_file_line(lineid,filename,folder)
    iddata = read_file("{}id".format(filename),folder)
    update_file(data,"temporaryvirtual",folder)
    update_file(iddata,"temporaryvirtualid",folder)
    braindata = read_brain(folder,"temporaryvirtual")

    try:

        if(braindata==["\n"]):
            lineid=lineid+1
            update_file(lineid,"temporaryvirtualline",folder)
            return read_storage_with_idname_lineid(idname,lineid,filename,folder)
    except Exception:

        
        if(braindata==[]):
            lineid=lineid+1
            update_file(lineid,"temporaryvirtualline",folder)
            return read_storage_with_idname_lineid(idname,lineid,filename,folder)



    return str(braindata[id]).rstrip()

def update_full_module(name_of_module,folder,data_total_no):
    d = read_file(name_of_module,folder)
    if(d==""):
        return reprogram_full_module(name_of_module,folder,data_total_no)

    else:
        
        for i in range(data_total_no):
            idbrain = read_brain(folder,"{}id".format(name_of_module))
            dataid = idbrain[i]
            dataval = input("WHAT'S THE {} VALUE?".format(dataid))
            learn_brain_with_id(dataid,folder,name_of_module,dataval)
    return "DONE!"
def update_full_module_with_list(module_name,id_list,data_list,folder):
    d1 = id_list
    d2 = data_list
    newid = list_to_braindata_converter(id_list)
    newdata = list_to_braindata_converter(data_list)
    update_file(newid,"{}id".format(module_name),folder)
    update_file(newdata,"{}".format(module_name),folder)

def update_line_in_file(inputdata,linenumber,filename,folder):
    hedgefile = open(str("{}/{}.txt".format(folder,filename)),"r")
    lines = ""
    with open(str("{}/{}.txt".format(folder,filename)),'r') as hedgefile:
        lines = hedgefile.readlines()
    if linenumber <0 or linenumber>len(lines):
        print("INVALID")
        return
    lines[linenumber] = inputdata + "\n"
    with open(str("{}/{}.txt".format(folder,filename)),'w') as hedgefile:
        hedgefile.writelines(lines)
    return "DONE!"

def update_storage_by_line_and_idname(idname,linenumber,newdata,part,folder):
    brain = read_brain(folder,"{}id".format(part))
    location = brain.index(idname)
    data_x = read_storage_by_lineid(linenumber,part,folder)
    braindata = data_x
    braindata[location]=newdata

    rawdata = str(braindata)
    lent = len(rawdata)
    newstr = ""
    for i in range(lent):
        char = rawdata[i]
        if((char != "[")and(char != "]")and(char != "'")and(char != " ")):
            newstr = newstr+char
    newstr = newstr.replace("\\n","")
    update_line_in_file(newstr,linenumber,part,folder)
    return "Brain updated Successfully"


def purify_storage(filename,folder):
    remove_empty_line(filename,folder)
    remove_duplicate_lines(filename,folder)

    return "DONE!"


def list_to_braindata_converter(rawdata):
    sdata = rawdata
    lent = len(sdata)
    newstr = ""
    st = ""
    for i in range(lent):
        char = sdata[i]
        if(i<lent-1):
            newstr = newstr+","+str(char)
        if(i==lent-1):

            l = lent
            last = str(sdata[l-1])
            # print(last)
            lx = len(last)
            
            nx = 0
            for i in range(lx):
                dchr = last[i]
                data = ord(last[i])
                if(data == 92):
                    nx=nx+1
                if(nx==0):
                    st=st+dchr
                
            newstr = newstr+","+st

            

    return newstr



def delete_line_with_id(linenumber,filename,folder):
    hedgefile = open(str("{}/{}.txt".format(folder,filename)),"r")
    
    with open(str("{}/{}.txt".format(folder,filename)),'r') as hedgefile:
        lines = hedgefile.readlines()
    with open(str("{}/{}.txt".format(folder,filename)),'w') as hedgefile:
        for i,line in enumerate(lines):
            if i !=linenumber:
                hedgefile.write(line)
    return "DONE!"

def remove_empty_line(filename,folder):
    slen = total_file_lines(filename,folder)
    slen = slen
    update_file("","{}aux".format(filename),folder)
    for i in range(slen):
        lin = read_storage_by_lineid(i,filename,folder)
        line = list_to_braindata_converter(lin)
        if((lin==[])or(line=="")or(line == "\n")or(lin==["\n"])):
            pass
        else:
            append_file(line,"{}aux".format(filename),folder)
    adata = read_file("{}aux".format(filename),folder)
    update_file(adata,filename,folder)
    return "DONE!"
                                                           
def remove_duplicate_lines(filename,folder):
    lines_seen = set()
    output_lines = []                          
    with open(str("{}/{}.txt".format(folder,filename)),'r') as file:
        for line in file:
            if line not in lines_seen:
                lines_seen.add(line)
                output_lines.append(line)
    with open(str("{}/{}.txt".format(folder,filename)),'w') as file:
        file.writelines(output_lines)
def reprogram_full_module(name_of_module,folder,data_total_no):
    update_file("",name_of_module,folder)
    update_file("","{}id".format(name_of_module),folder)
    for i in range(data_total_no):
        idbrain = input("WHAT'S THE ID{} NAME?".format(i+1))
        dataid = idbrain
        dataval = input("WHAT'S THE {} VALUE?".format(dataid))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        learn_brain_with_id(dataid,folder,name_of_module,dataval)
    return "DONE!"


def pattern_check(new_data,parent_data,total_to_check,nature,individual_percentage,collective_percentage):
    i_percentage = individual_percentage
    c_percentage = collective_percentage
    ln = len(new_data)
    lp = len(parent_data)
    if((ln >= total_to_check)and(lp >= total_to_check)):
        ln = total_to_check
        cp = 0
        cc = []
        xc = []
        cond_met = 0
        result = ""
        for i in range(ln):
            d1 = float(new_data[i])
            p1 = float(parent_data[i])
            difference = 0
            ipattern = 0
            nipattern = 0
            if(nature=="strict"):
                if(abs(d1)>=abs(p1)):
                    difference = d1-p1
                if(abs(p1)>abs(d1)):
                    difference = p1-d1
                nipattern = (difference/p1)*100
                ipattern = 100 - nipattern
                xc.append(ipattern)
                if((ipattern >= i_percentage)and(ipattern<=100)):
                    cp = cp+1
                    cc.append(i)
            if(nature == "flexible"):
                if(abs(d1)>=abs(p1)):
                    difference = abs(d1)-abs(p1)
                if(abs(p1)>abs(d1)):
                    difference = abs(p1)-abs(d1)
                nipattern = (difference/abs(p1))*100
                
                
                if((d1>0)and(p1>0)and(nipattern<=100)):
                    ipattern = 100 - nipattern
                elif((d1>0)and(p1>0)and(nipattern>=100)):
                    ipattern = nipattern - 100
                elif((d1<0)and(p1>0)and(nipattern<=100)):
                    ipattern = (100 - nipattern)*-1
                elif((d1<0)and(p1>0)and(nipattern>=100)):
                    ipattern = (nipattern - 100)*-1                   
                elif((d1>0)and(p1<0)and(nipattern<=100)):
                    ipattern = (100 - nipattern)*-1
                elif((d1>0)and(p1<0)and(nipattern>=100)):
                    ipattern = (nipattern - 100)*-1
                elif((d1<0)and(p1<0)and(nipattern<=100)):
                    ipattern = 100 - nipattern
                elif((d1<0)and(p1<0)and(nipattern>=100)):
                    ipattern = nipattern - 100                
                xc.append(ipattern)
                if((ipattern >= i_percentage)):
                    cp = cp+1
                    cc.append(i)
        cond_met = (cp/lp)*100
        if((cond_met >= c_percentage)and(cond_met<=100)):
            result = "yes"
        else:
            result = "no"
        total_that_met_condition = cp
        positions_that_met_condition = cc
        all_percentage = xc
        return result,total_that_met_condition,positions_that_met_condition,all_percentage
    else:
        result = "DATA LENGTH DOES NOT MATCH"
        return result
    
def string_to_list(string_to_convert):
    rawdata = string_to_convert
    lent = len(rawdata)
    newstr = ""
    for i in range(lent):
        char = rawdata[i]
        if((char != "[")and(char != "]")and(char != "'")and(char != " ")and(char != '"')):
            newstr = newstr+char
    newstr = newstr.replace("\\n","")
    brain = newstr
    datax =  brain
    var = []
    ld = len(datax)
    data = ""
    for i in range(ld):
        dv =  datax[i]
        
        if((dv!=",")and(dv!="")):
            data = data + dv
        if((dv==",")or(i==ld-1)):
            if(data != ""):
                var.append(data)
                data = ""
    return var


def mass_pattern_check(new_data,storage_name,start_position,end_position,folder,total_to_check,nature,individual_percentage,collective_percentage):
    tx = total_file_lines(storage_name,folder)
    print(tx)
    full_cond_met = 0
    lines_that_met_cond = []
    i_percentage = individual_percentage
    c_percentage = collective_percentage
    result = "no"
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    parent_x = []
    ln = len(new_data)
    for k in range(tx):
        parent_e = read_storage_by_lineid(k,storage_name,folder)
        parent_x = string_to_list(str(parent_e))

        if((ln >= total_to_check)):
            ln = total_to_check
            parent_data = parent_x
            
           # lp = len(parent_data)
            lp = end_position - start_position
            cp = 0
            cc = []
            xc = []
            cond_met = 0
           
            for i in range(start_position,end_position):
                # try:
                    
                d1 = float(new_data[i])
                d1 = d1*(1/1000)
                p1 = float(parent_data[i])
                p1 = p1*(1/1000)
                print("{} and {}".format(p1,d1))
                # except Exception as e:
                #     print(e)
                #     i=i+1
                #     try:
                        
                #         d1 = float(new_data[i])
                #         p1 = float(parent_data[i])
                #     except Exception as e:
                #         print(e)
                #         i=i+1

                #         try:
                            
                #             d1 = float(new_data[i])
                #             p1 = float(parent_data[i])
                #         except Exception as e:
                #             print(e)
                #             i=i+1
                #             try:
                                
                #                 d1 = float(new_data[i])
                #                 p1 = float(parent_data[i])
                #             except Exception as e:
                #                 print(e)
                #                 i=i+1
                #                 d1 = float(new_data[i])
                #                 p1 = float(parent_data[i])
                difference = 0
                ipattern = 0
                nipattern = 0
                difcoef = d1*(1/1000)
                if(nature=="strict"):
                    if(abs(d1)>=abs(p1)):
                        difference = d1-p1
                    if(abs(p1)>abs(d1)):
                        difference = p1-d1
                    nipattern = ((difference+difcoef)/p1)*100
                    ipattern = 100 - nipattern
                    xc.append(ipattern)
                    if((ipattern >= i_percentage)and(ipattern<=100)):
                        cp = cp+1
                        cc.append(i)
                if(nature == "flexible"):
                    if(abs(d1)>=abs(p1)):
                        difference = abs(d1)-abs(p1)
                    if(abs(p1)>abs(d1)):
                        difference = abs(p1)-abs(d1)
                    nipattern = ((difference+difcoef)/abs(p1))*100
                    if((d1>0)and(p1>0)and(nipattern<=100)):
                        ipattern = 100 - nipattern
                    elif((d1>0)and(p1>0)and(nipattern>=100)):
                        ipattern = nipattern - 100
                    elif((d1<0)and(p1>0)and(nipattern<=100)):
                        ipattern = (100 - nipattern)*-1
                    elif((d1<0)and(p1>0)and(nipattern>=100)):
                        ipattern = (nipattern - 100)*-1                   


                    elif((d1>0)and(p1<0)and(nipattern<=100)):
                        ipattern = (100 - nipattern)*-1
                    elif((d1>0)and(p1<0)and(nipattern>=100)):
                        ipattern = (nipattern - 100)*-1
                    elif((d1<0)and(p1<0)and(nipattern<=100)):
                        ipattern = 100 - nipattern
                    elif((d1<0)and(p1<0)and(nipattern>=100)):
                        ipattern = nipattern - 100                
                    xc.append(ipattern)
                    if((ipattern >= i_percentage)):
                        cp = cp+1
                        cc.append(i)
            cond_met = (cp/lp)*100
            if((cond_met >= c_percentage)and(cond_met<=100)):
                result = "yes"
                full_cond_met = full_cond_met + 1
                lines_that_met_cond.append(k)
        else:
            pass
    return result,full_cond_met,lines_that_met_cond

def push_to_storage(list_data,storage_name,folder):
    d = list_to_braindata_converter(list_data)
    append_file(d,storage_name,folder)
    purify_storage(storage_name,folder)
    return "Done" 
def update_storageid_with_list(idlist,storagename,folder):
    dx = list_to_braindata_converter(idlist)
    update_file(dx,"{}id".format(storagename),folder)
def range_check(new_data,parent_data,range_percentage):
    i_percentage = 100 - range_percentage
    result = "no"
    nature1 = "strict"
    nature2 = "strict"
#     for i in range(ln):
    d1 = float(new_data)
    p1 = float(parent_data)
    if(nature1=="strict"):
        if(abs(d1)>=abs(p1)):
            difference = d1-p1
        if(abs(p1)>abs(d1)):
            difference = p1-d1
        nipattern = (difference/p1)*100
        ipattern = 100 - nipattern
   
        if((ipattern >= i_percentage)and(ipattern<=100)):
            result = "yes"
    if(nature2 == "flexible"):
        if(abs(d1)>=abs(p1)):
            difference = abs(d1)-abs(p1)
        if(abs(p1)>abs(d1)):
            difference = abs(p1)-abs(d1)
        nipattern = (difference/abs(p1))*100
        
        
        if((d1>0)and(p1>0)and(nipattern<=100)):
            ipattern = 100 - nipattern
        elif((d1>0)and(p1>0)and(nipattern>=100)):
            ipattern = nipattern - 100
        elif((d1<0)and(p1>0)and(nipattern<=100)):
            ipattern = (100 - nipattern)*-1
        elif((d1<0)and(p1>0)and(nipattern>=100)):
            ipattern = (nipattern - 100)*-1                   


        elif((d1>0)and(p1<0)and(nipattern<=100)):
            ipattern = (100 - nipattern)*-1
        elif((d1>0)and(p1<0)and(nipattern>=100)):
            ipattern = (nipattern - 100)*-1
        elif((d1<0)and(p1<0)and(nipattern<=100)):
            ipattern = 100 - nipattern
        elif((d1<0)and(p1<0)and(nipattern>=100)):
            ipattern = nipattern - 100                
       
        if((ipattern >= i_percentage)):
    
            result = "yes"
        print(ipattern)
        print(i_percentage)
    return result

def clean_brain(filename,folder):
    bdata = read_file(filename,folder)
    l = len(bdata)
    newdata = ""
    for i in range(l):
        char = bdata[i]
        check = str(char).isalnum()
        if((((char==".")or(char==","))and(check==False))or(check==True)):
            newdata =newdata + char
    update_file("",filename,folder)
    update_file(newdata,filename,folder)
    
    
class FindPattern:
    def __init__(self,brainfile,storagename,filename,trainingfile,foldername):
        self.storagename = storagename
        self.foldername = foldername
        self.brainfile = brainfile
        self.filename = filename
        self.trainingfile = trainingfile
    def clear_brains(self):
        update_file("",self.brainfile,self.foldername)
        update_file("",self.storagename,self.foldername)
        update_file("",self.filename,self.foldername)
    def clear_file(self,filename):
        update_file("",filename,self.foldername)
        
    def store_training_data(self,id_list,data_list):
        update_full_module_with_list(self.trainingfile,id_list,data_list,self.foldername)
        push_to_storage(data_list,self.storagename,self.foldername)
        update_file(id_list,"{}id".format(self.storagename),self.foldername)
        

class mysqlconnect:
    def __init__(self,url,passcode):
        self.url = url
        self.passcode = passcode
# columndatastring = "column1=val1&column2=val2&column3=val3&column4=val4&column5=val5"
# columnnumber = 5
# tablename = "neutral"
# password = "1iloveJesus"
# url = "127.0.0.1/hexeba/api.php"
#columnnumber = "5"
#columndatastring = "column1=algoname&column2=symbol&column3=coeficient&column4=position&column5=time"
    def create_table(self,tablename,columnnumber,columndatastring):
        msg = "createtable"
        respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}&columnnumber={}&{}'.format(self.url,self.passcode,msg,tablename,columnnumber,columndatastring))
        try:

            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1

    def update_table_data(self,tablename,dataname,data,idname,iddata):
        try:
            msg = "updatetabledata"
            respx1 = requests.post('http://{}?admincode={}&message={}&dataname={}&data={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,msg,dataname,data,idname,iddata,tablename))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)

    def track_click(self,tablename,button):
        
        try:
            msg = "trackclicks"
            respx1 = requests.get('https://{}?admincode={}&message={}&button={}&tablename={}'.format(self.url,self.passcode,msg,button,tablename))
      #      respx1 = requests.get('http://{}?admincode={}&message={}&button={}&tablename={}'.format(self.url,self.passcode,msg,button,tablename))
            try:
                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)


    def update_user_data(self,dataname,data,idname,iddata):
        try:
            msg = "updateuserdata"
            respx1 = requests.post('http://{}?admincode={}&message={}&dataname={}&data={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,dataname,data,idname,iddata))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)
    def update_bot_data(self,dataname,data,idname,iddata):
        try:
            msg = "updatebotdata"
            respx1 = requests.post('http://{}?admincode={}&message={}&dataname={}&data={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,dataname,data,idname,iddata))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)

    def read_table_data(self,tablename):
        try:

            msg = "readtabledata"
            respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}'.format(self.url,self.passcode,msg,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            
    def read_table_data_user(self,tablename,idname,iddata):
        try:
            msg = "readtabledatauser"
            respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,msg,idname,iddata,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            
    def read_user_data(self,idname,iddata):
        try:
            msg = "readuserdata"
            respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,idname,iddata))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)

    def read_bot_data(self,idname,iddata):
        try:
            msg = "readbotdata"
            respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,idname,iddata))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            
    def insert_table_data(self,tablename,idname,iddata):
        msg = "inserttabledata"
        respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,msg,idname,iddata,tablename))
        try:
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1
        
    def insert_user_data(self,idname,iddata):
        msg = "insertuserdata"
        respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,idname,iddata))
        try:
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1
        
    def insert_bot_data(self,idname,iddata):
        msg = "insertbotdata"
        respx1 = requests.post('http://{}?admincode={}&message={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,idname,iddata))
        try:
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1
        
    def time_difference(timedata):
        timern = datetime.now()
        tstop_time = datetime.strptime(timedata, '%Y-%m-%d %H:%M:%S')
        time_delta1 = (timern - tstop_time)
        total_seconds1 = time_delta1.total_seconds()
        tstop_secs = total_seconds1
        return tstop_secs

    def clean_time(time):
        dt = str(time)
        ldt = len(dt)
        n = ""
        v = "start"
        for i in range(ldt):
            ch = dt[i]
            if(ch == "."):
                v = "end"
            if(v=="start"):
                n=n+ch
        timex = n 
        return timex

    # def time_difference_user(timefile,idname,iddata):
    #     v = "TEST"
    #     tstop_time = read_user_data(timefile,idname,iddata)
    #     timern = datetime.now()
    #     tstop_time = datetime.strptime(tstop_time, '%Y-%m-%d %H:%M:%S')
    #     time_delta1 = (timern - tstop_time)
    #     total_seconds1 = time_delta1.total_seconds()
    #     tstop_secs = total_seconds1
    #     return tstop_secs
    
    def time_difference_bot(timefile,idname,iddata):
        v = "TEST"
        tstop_time = read_bot_data(timefile,idname,iddata)
        timern = datetime.now()
        tstop_time = datetime.strptime(tstop_time, '%Y-%m-%d %H:%M:%S')
        time_delta1 = (timern - tstop_time)
        total_seconds1 = time_delta1.total_seconds()
        tstop_secs = total_seconds1
        return tstop_secs
    
    def read_precision(value):
        strx = str(value)
        inx = 0
        a = 0
        b = 0
        precision = 0
        l = len(strx)
        for i in range(l):
            vx = strx[i]
            if(vx == "."):
                a = inx + 1
            if(a==1):
                b=b+1
        precision = b-1
        return precision

    def reduce_precision(value,precision):
        val = round(value,precision)
        return val


    def adjust_precision(outputk,inputk):
        inputval = read_precision(inputk)
        outputval = read_precision(outputk)
        newval = reduce_precision(inputk,outputval)
        return newval

    # def set_bot_time(dataname,time,idname,iddata):
    #     v ="f"
    #     try:
    #         v = read_bot_data(dataname,idname,iddata)
    #     except Exception as e:
    #         update_bot_data(dataname,time,idname,iddata)
    #     dt = str(time)
    #     ldt = len(dt)
    #     n = ""
    #     v = "start"
    #     for i in range(ldt):
    #         ch = dt[i]
    #         if(ch == "."):
    #             v = "end"
    #         if(v=="start"):
    #             n=n+ch
    #     timex = n 
    #     update_bot_data(dataname,timex,idname,iddata)

    def delete_table(self,tablename):
        msg = "deletetable"
        respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}'.format(self.url,self.passcode,msg,tablename))
        try:

            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1

    def delete_data(self,tablename,idname,iddata):
        msg = "deletedata"
        respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}&idname={}&iddata={}'.format(self.url,self.passcode,msg,tablename,idname,iddata))
        try:
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1
        
    def delete_all_table_data(self,tablename):
        msg = "deletealltabledata"
        respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}'.format(self.url,self.passcode,msg,tablename))
        try:
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            return respx1
        
    def viewcolumns(self,tablename):
        try:
            msg = "viewcolumns"
            respx1 = requests.post('http://{}/viewcolumns?admincode={}&message={}&tablename={}'.format(self.url,self.passcode,msg,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            
    def viewtables(self):
        try:
            msg = "viewtables"
            respx1 = requests.post('http://{}?admincode={}&message={}'.format(self.url,self.passcode,msg))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            
    def testconnection(self):
        try:
            msg = "test"
            # respx1 = requests.post('http://{}?admincode={}&message={}'.format(urlname,admincode,msg))
            respx1 = requests.request('GET', 'http://{}?admincode={}&message={}'.format(self.url,self.passcode,msg))
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            print(e)

    def testscript(self):
        try:
            msg = "testscript"
            respx1 = requests.post("http://{}?message={}&admincode={}".format(self.url,msg,self.passcode))
            # respx1 = requests.post("http://hexeba.unaux.com/api.php?admincode=1iloveJesus.&message=testscript")
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            print(e)
            

    def test(self):
        try:
            # msg = "testscript"
            respx1 = requests.post('http://{}?i=1'.format(self.url))
            dataxx = respx1.text
            return dataxx
        except Exception as e:
            print(e)
            
    def renametable(self,tablename,newtablename):
        try:
            msg = "renametable"
            respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}&newtablename={}'.format(self.url,self.passcode,msg,tablename,newtablename))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)

    def addcolumn(self,tablename,newcolumnname):
        try:
            msg = "addcolumn"
            respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}&newcolumnname={}'.format(self.url,self.passcode,msg,tablename,newcolumnname))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)


    def removecolumn(self,tablename,newcolumnname):
        try:
            msg = "removecolumn"
            respx1 = requests.post('http://{}?admincode={}&message={}&tablename={}&columnname={}'.format(self.url,self.passcode,msg,tablename,newcolumnname))
            try:

                dataxx = respx1.text
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)


class sqlite:
    def __init__(self,database_name,passcode):
        database = database_name
        conn = sqlite3.connect(database, check_same_thread=False)
        self.conn = conn


    def createtable(self,tablename,columnnamelist):

        column_number = len(columnnamelist)
        
        opendata = f"CREATE TABLE IF NOT EXISTS {tablename} (id integer PRIMARY KEY"
        coldata = ""
        closedata = ",datex text);"
        t=0
        for i in range(column_number):
            t = t+1
            columnname = columnnamelist[i]
            middata = f",{columnname} text"
            coldata = coldata+middata
        finaldata = opendata+coldata+closedata
        f = conn.cursor()
        f.execute(f"""{finaldata}""")
        conn.commit()
        datafetched = []
        dx = {
            "message" : "SUCCESSFULLY CREATED TABLE"
        }
        datafetched.append(dx)
        return datafetched

class sqliteconnect:
    def __init__(self,url,passcode):
        self.url = url
        self.passcode = passcode
        

    def read_all_data_user(self):
        respx1 = requests.get('http://{}/usersdata?admincode={}'.format(self.url,self.passcode))
        dataxx = respx1.json()
        return dataxx

    def read_all_data_bot(self):
        respx1 = requests.get('http://{}/hedgebotdata?admincode={}'.format(self.url,self.passcode))
        dataxx = respx1.json()
        return dataxx


    def read_user_data(self,dataname,idname,iddata):
        try:

            respx1 = requests.get('http://{}/userdata?admincode={}&idname={}&iddata={}'.format(self.url,self.passcode,idname,iddata))
            dataxx = respx1.json()
            return dataxx[0][dataname]
        except Exception as e:
            print(e)
            insert_user_data(idname,iddata)

    def read_bot_data(self,dataname,idname,iddata):
        try:

            respx1 = requests.get('http://{}/userhedgedata?admincode={}&idname={}&iddata={}'.format(self.url,self.passcode,idname,iddata))
            dataxx = respx1.json()
            return dataxx[0][dataname]
        except Exception as e:
            print(e)
            insert_bot_data(idname,iddata)

    def update_user_data(self,dataname,datasent,idname,iddata):
        try:

            respx1 = requests.get('http://{}/updateuser?admincode={}&dataname={}&data={}&idname={}&iddata={}'.format(self.url,self.passcode,dataname,datasent,idname,iddata))
            try:

                dataxx = respx1.json()
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)
            insert_user_data(idname,iddata)

    def update_bot_data(self,dataname,data,idname,iddata):
        try:

            respx1 = requests.get('http://{}/updatehedgedata?admincode={}&dataname={}&data={}&idname={}&iddata={}'.format(self.url,self.passcode,dataname,data,idname,iddata))
            try:

                dataxx = respx1.json()
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)
            insert_bot_data(idname,iddata)
    def insert_user_data(self,idname,iddata):
        respx1 = requests.get('http://{}/insertdata?admincode={}&idname={}&iddata={}'.format(self.url,self.passcode,idname,iddata))
        try:

            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            return respx1

    def insert_bot_data(self,idname,iddata):
        respx1 = requests.get('http://{}/inserthedgebotdata?admincode={}&idname={}&iddata={}'.format(self.url,self.passcode,idname,iddata))
        try:

            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            return respx1

    def time_difference_bot(self,timefile,idname,iddata):
        v = "TEST"
        tstop_time = read_bot_data(timefile,idname,iddata)
        timern = datetime.now()
        tstop_time = datetime.strptime(tstop_time, '%Y-%m-%d %H:%M:%S')
        time_delta1 = (timern - tstop_time)
        total_seconds1 = time_delta1.total_seconds()
        tstop_secs = total_seconds1
        return tstop_secs

    def time_difference_user(self,timefile,idname,iddata):
        v = "TEST"
        tstop_time = read_user_data(timefile,idname,iddata)
        timern = datetime.now()
        tstop_time = datetime.strptime(tstop_time, '%Y-%m-%d %H:%M:%S')
        time_delta1 = (timern - tstop_time)
        total_seconds1 = time_delta1.total_seconds()
        tstop_secs = total_seconds1
        return tstop_secs

    def read_precision(value):
        strx = str(value)
        inx = 0
        a = 0
        b = 0
        precision = 0
        l = len(strx)
        for i in range(l):
            vx = strx[i]
            if(vx == "."):
                a = inx + 1
            if(a==1):
                b=b+1
        precision = b-1
        return precision

    def reduce_precision(value,precision):
        val = round(value,precision)
        return val


    def adjust_precision(outputk,inputk):
        inputval = read_precision(inputk)
        outputval = read_precision(outputk)
        newval = reduce_precision(inputk,outputval)
        return newval

    def set_bot_time(dataname,time,idname,iddata):
        v ="f"
        try:
            v = read_bot_data(dataname,idname,iddata)
        except Exception as e:
            update_bot_data(dataname,time,idname,iddata)
        dt = str(time)
        ldt = len(dt)
        n = ""
        v = "start"
        for i in range(ldt):
            ch = dt[i]
            if(ch == "."):
                v = "end"
            if(v=="start"):
                n=n+ch
        timex = n 
        update_bot_data(dataname,timex,idname,iddata)

    def create_table(self,tablename,columnnumber,columndatastring):
        respx1 = requests.get('http://{}/createtable?admincode={}&tablename={}&columnnumber={}&{}'.format(self.url,self.passcode,tablename,columnnumber,columndatastring))
        try:

            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            return respx1

    def delete_table(self,tablename):
        respx1 = requests.get('http://{}/droptable?admincode={}&tablename={}'.format(self.url,self.passcode,tablename))
        try:
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            return respx1

    def insert_table_data(self,tablename,idname,iddata):
        respx1 = requests.get('http://{}/inserttabledata?admincode={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,idname,iddata,tablename))
        try:

            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            return respx1

    def update_table_data(self,tablename,dataname,data,idname,iddata):
        try:

            respx1 = requests.get('http://{}/updatetable?admincode={}&dataname={}&data={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,dataname,data,idname,iddata,tablename))
            try:

                dataxx = respx1.json()
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)
            

    def read_table_data(self,tablename):
        try:

            respx1 = requests.get('http://{}/tabledata?admincode={}&tablename={}'.format(self.url,self.passcode,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)

    def read_table_data_user(self,tablename,idname,iddata):
        try:
            respx1 = requests.get('http://{}/usertabledata?admincode={}&idname={}&iddata={}&tablename={}'.format(self.url,self.passcode,idname,iddata,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)
            

    def viewcolumns(self,tablename):
        try:
            respx1 = requests.get('http://{}/viewcolumns?admincode={}&tablename={}'.format(self.url,self.passcode,tablename))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)

    def viewtables(self):
        try:
            respx1 = requests.get('http://{}/viewtables?admincode={}'.format(self.url,self.passcode))
            dataxx = respx1.json()
            return dataxx
        except Exception as e:
            print(e)


    def renametable(self,tablename,newtablename):
        try:
            respx1 = requests.get('http://{}/renametable?admincode={}&tablename={}&newtablename={}'.format(self.url,self.passcode,tablename,newtablename))
            try:

                dataxx = respx1.json()
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)

    def addcolumn(self,tablename,newcolumnname):
        try:
            respx1 = requests.get('http://{}/addcolumn?admincode={}&tablename={}&newcolumnname={}'.format(self.url,self.passcode,tablename,newcolumnname))
            try:

                dataxx = respx1.json()
                return dataxx
            except Exception as e:
                return respx1
        except Exception as e:
            print(e)

    def clean_time(time):
        dt = str(time)
        ldt = len(dt)
        n = ""
        v = "start"
        for i in range(ldt):
            ch = dt[i]
            if(ch == "."):
                v = "end"
            if(v=="start"):
                n=n+ch
        timex = n 
        return timex

    def time_difference(timedata):
        timern = datetime.now()
        tstop_time = datetime.strptime(timedata, '%Y-%m-%d %H:%M:%S')
        time_delta1 = (timern - tstop_time)
        total_seconds1 = time_delta1.total_seconds()
        tstop_secs = total_seconds1
        return tstop_secs

def time_difference_file(filename,folder):
    timedata = read_file(filename,folder)
    if(timedata==""):
        set_time(datetime.now(),filename,folder)
        time_difference_file(filename,folder)
    timern = datetime.now()
    tstop_time = datetime.strptime(timedata, '%Y-%m-%d %H:%M:%S')
    time_delta1 = (timern - tstop_time)
    total_seconds1 = time_delta1.total_seconds()
    tstop_secs = total_seconds1
    return tstop_secs


# class submitToExcel:
#     def __init__(self,foldername,filename,list_keys):
#         self.foldername = foldername
#         self.filename = filename
#         self.list_keys = list_keys





class patternRecognition:
    def __init__(self,modulename,storagename,foldername,storageLength,analysisTime,threshold):
        self.modulename = modulename
        self.storagename = storagename
        self.digitalmodulename = "digital{}".format(modulename)
        self.analogmodulename = "analog{}".format(modulename)
        self.rawmodulename = "raw{}".format(modulename)
        self.digitalstoragename = "digital{}".format(storagename)
        self.analogstoragename = "analog{}".format(storagename)
        self.foldername = foldername
        self.storageLength = storageLength
        self.analysisTime = analysisTime
        self.timefile = "{}time".format(modulename)
        self.threshold = threshold
    
    def save_raw_data(self,rawdata):
        free_learn_brain_with_id(rawdata,self.rawmodulename,self.foldername)
        return "saved"

    def purge_modules(self):
        update_file("",self.analogmodulename,self.foldername)
        update_file("",self.rawmodulename,self.foldername)
        update_file("",self.digitalmodulename,self.foldername)
        update_file("","{}id".format(self.rawmodulename),self.foldername)
        update_file("","{}id".format(self.analogmodulename),self.foldername)
        update_file("","{}id".format(self.digitalmodulename),self.foldername)

    def purge_storage(self):
        update_file("",self.analogstoragename,self.foldername)
        update_file("",self.digitalstoragename,self.foldername)
        update_file("","{}id".format(self.analogstoragename),self.foldername)
        update_file("","{}id".format(self.digitalstoragename),self.foldername)

    def purge_all(self):
        update_file("",self.analogmodulename,self.foldername)
        update_file("",self.rawmodulename,self.foldername)
        update_file("",self.digitalmodulename,self.foldername)
        update_file("","{}id".format(self.rawmodulename),self.foldername)
        update_file("","{}id".format(self.analogmodulename),self.foldername)
        update_file("","{}id".format(self.digitalmodulename),self.foldername)
        update_file("",self.analogstoragename,self.foldername)
        update_file("",self.digitalstoragename,self.foldername)
        update_file("","{}id".format(self.analogstoragename),self.foldername)
        update_file("","{}id".format(self.digitalstoragename),self.foldername)



    def activate(self,newdata,result):
        time = datetime.now()
        timedata = read_file(self.timefile,self.foldername)
        if(timedata == ""):
            set_time(time,self.timefile,self.foldername)
        lastupdate = time_difference(self.timefile,self.foldername)
        if(lastupdate > self.analysisTime):
            set_time(time,self.timefile,self.foldername)
            
            
            dl = len(read_brain(self.foldername,self.analogmodulename))
            if((dl<self.storageLength)):
                self.analogize_data(newdata)
                self.digitize_data(newdata)
                self.save_raw_data(newdata)
                print(newdata)

            else:
                learn_brain_with_id("result",self.foldername,self.digitalmodulename,result)
                learn_brain_with_id("result",self.foldername,self.analogmodulename,result)
                
                
                digital_list_data = read_brain(self.foldername,self.digitalmodulename)
                analog_list_data = read_brain(self.foldername,self.analogmodulename)
                if((result != "unknown")and(result != "")):
                    self.pass_to_digital_storage(digital_list_data)
                    self.pass_to_analog_storage(analog_list_data)
                    self.purge_modules()
                    dl = self.storageLength + 1

    def analogize_data(self,newdata):
        rawbrainlength = len(read_brain(self.foldername,self.rawmodulename))
        if(rawbrainlength>=1):
          #  lastdata = read_last_braindata_ignore_result(self.rawmodulename,self.foldername)
            lastdata = float(read_last_braindata_ignore_result(self.rawmodulename,self.foldername))
            newdata = float(newdata)
            Analogfiledata = read_file(self.analogmodulename,self.foldername)
            analogdata = ((newdata-lastdata)/newdata)*100
          #  print("NEW DATA:{} LAST DATA:{}".format(newdata,lastdata))
                
            if(Analogfiledata == ""):
                update_file(round(analogdata,1),self.analogmodulename,self.foldername)
                update_file("data1","{}id".format(self.analogmodulename),self.foldername)
            else:

                if(lastdata>=newdata):
                    n = ((newdata-lastdata)/newdata)*100
                    #print(n)
                    if(n<=-(self.threshold)):
                        analogdata = n
                    else:
                        analogdata = 0
                    
                if(newdata>=lastdata):
                    n = ((newdata-lastdata)/newdata)*100
                    if(n>=(self.threshold)):
                        analogdata = n
                    else:
                        analogdata = 0

                free_learn_brain_with_id(round(analogdata,1),self.analogmodulename,self.foldername)
              #  self.save_raw_data(newdata)


        else:
            self.save_raw_data(newdata)
        #    self.analogize_data(newdata)

    def digitize_data(self,newdata):
        rawbrainlength = len(read_brain(self.foldername,self.rawmodulename))
        if(rawbrainlength>=1):
          #  lastdata = read_last_braindata_ignore_result(self.rawmodulename,self.foldername)
            lastdata = float(read_last_braindata_ignore_result(self.rawmodulename,self.foldername))
            newdata = float(newdata)
            Analogfiledata = read_file(self.digitalmodulename,self.foldername)
            analogdata = ((newdata-lastdata)/newdata)*100
          #  print("NEW DATA:{} LAST DATA:{}".format(newdata,lastdata))
                
            if(Analogfiledata == ""):
                update_file(round(analogdata,1),self.digitalmodulename,self.foldername)
                update_file("data1","{}id".format(self.digitalmodulename),self.foldername)
            else:

                if(lastdata>=newdata):
                    n = ((newdata-lastdata)/newdata)*100
                    #print(n)
                    if(n<=-(self.threshold)):
                        analogdata = -1
                    else:
                        analogdata = 0
                    
                if(newdata>=lastdata):
                    n = ((newdata-lastdata)/newdata)*100
                    if(n>=(self.threshold)):
                        analogdata = 1
                    else:
                        analogdata = 0

                free_learn_brain_with_id(round(analogdata,1),self.digitalmodulename,self.foldername)
              #  self.save_raw_data(newdata)


        else:
            self.save_raw_data(newdata)
        #    self.analogize_data(newdata)
        
    def pass_to_digital_storage(self,list_data):
        push_to_storage(list_data,self.digitalstoragename,self.foldername)
        
    def pass_to_analog_storage(self,list_data):
        push_to_storage(list_data,self.analogstoragename,self.foldername)

    def search_for_digital_pattern(self,):
        moduledata = read_brain(self.foldername,self.digitalmodulename)



        newdata = read_brain(self.foldername,self.digitalmodulename)
        new_data = string_to_list(str(newdata))
        storage_name = "mainstorage"
        total_to_check = len(new_data)
        nature = "strict"
        start_position = 1
        end_position = total_to_check-2
        individual_percentage = 90
        collective_percentage = 100
      #  result,full_cond_met,lines_that_met_cond = mass_digital_pattern_check(new_data,storage_name,start_position,end_position,folder,total_to_check,collective_percentage)


        
        pass
    def search_for_analog_pattern(self,):
        pass

def get_highest_and_ID__from_list(listdata,filename,folder):

    lx = len(listdata)
    for ix in range(lx):
        d = float(listdata[ix])
        if(ix == 0):
            update_file(d,filename,folder)
            update_file(ix,"{}_id".format(filename),folder)
        last = float(read_file(filename,folder))
        lastid = float(read_file("{}_id".format(filename),folder))
        if(d>=last):
            update_file(d,filename,folder)
            update_file(ix,"{}_id".format(filename),folder)
        if(ix == lx-1):
            last = float(read_file(filename,folder))
            lastid = int(read_file("{}_id".format(filename),folder))
    return last,lastid