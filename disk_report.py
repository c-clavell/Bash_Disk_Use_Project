#!/usr/bin/env python



import sys
import os
import subprocess ##Execute Shell Commands with Python
import pandas as pd


def get_size(path,numSubs=0,numfiles=0):

    listTotal=[]
    total = 0
    
    
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                
                numSubs+=1
                total += get_size(entry.path,numSubs)[0] ## getting total value
                
                
            else:  ## if the entry is a file
                
                total += entry.stat(follow_symlinks=False).st_size
                numfiles+=1

        except Exception as err:
            print("error: ",err)
            total+=0

    listTotal= [total,numfiles,numSubs]

    return listTotal




if __name__ == '__main__':

    pwd = subprocess.run("pwd", stdout=subprocess.PIPE, shell=True)
    pwd =pwd.stdout.decode('utf-8')
    print(pwd)
    
   

    # path = './'
    #path ='/home'
    path= '../BASH_DISK_USAGE_PROJECT'
    # path= '../BASH_DISK_USAGE_PROJECT/aa'   ## used for testing
    # print('total arguments passed: ', len(sys.argv)) 
   
    directory= sys.argv[1] if len(sys.argv) >= 2 else path

    usage=[]
    paths=[]
    total_files=[]
    total_subs=[]
    

    # for entry in os.scandir(directory):
    #     print(entry.path)
    #     if entry.is_dir(follow_symlinks=False):
    #         print (entry.path + " is a directory")
    #         print("Total size of directory: ", get_size(entry.path),"bytes")
    #         print()
    #     if entry.is_file(follow_symlinks=False):
    #         print (entry.path + " is a file with a size of: ",entry.stat().st_size,"bytes")
    #         print()
    


    for entry in os.scandir(directory):
        if entry.is_dir(follow_symlinks=False):

            total_size, files_number, num_Subs = get_size(entry.path)

            

            paths.append(entry.path)
            usage.append(total_size)
            total_files.append(files_number)
            total_subs.append(num_Subs)
            
        
    usage_dict={'directory':paths,'num_subs':total_subs, 'num_files':total_files,'usage':usage}
    df=pd.DataFrame(usage_dict)
    print(df)
    df.to_csv("disk_usage.csv")
