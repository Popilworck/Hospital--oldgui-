import csv
def remdoc(doc):
            temp1 = []
            with open("logindata.csv",'r') as f:
                reader = csv.reader(f)
                for i in reader:
                    if doc in i and i[3]=='doctor':
                        continue
                    else:
                        temp1.append(i)
            with open("logindata.csv",'w',newline = '') as f:
                writer = csv.writer(f)
                writer.writerows(temp1)
            print("Success")
def showdoc():
    c=''
    with open("logindata.csv",'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if i[3]=='doctor':
                for j in range(2):
                    c+=i[j]
                    if j==0:
                        c+=' : ' 
                c+='\n'
    return(c)
def showstaff():
        c=''
        with open("logindata.csv",'r') as f:
            reader = csv.reader(f)
            for i in reader:
                if i[3]!='doctor':
                    for j in range(2):
                        c+=i[j]
                        if j==0:
                            c+=' : ' 
                    c+='\n'
        return(c)
            
def updoc(a,c,b):
        temp1 = []
        with open("logindata.csv",'r') as f:
            reader = csv.reader(f)
            for i in reader:
                if a in i:
                    i[b-1]= c
                    temp1.append(i)
                else:
                    temp1.append(i)
        with open("logindata.csv",'w',newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(temp1)
        print("Success")
def sdp(a):
    with open((a+'.txt'),'r') as f:
        return((f.read()))
def addpat(doci,a):
    with open(doci+'.txt','a') as f:
        # a=input("Enter patient name:\t")
        f.write(a)
        with open(a+'.csv','x') as g:
            pass

if __name__=='__main__':
    showstaff()