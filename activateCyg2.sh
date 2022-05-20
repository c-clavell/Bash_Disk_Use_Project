#!/usr/bin/bash

echo
files=$(find . -type f -path '*Scripts*/*' -name  activate)
final=""

if [ -z "$files" ];  ##checking if files were found 
then
    echo "No files found"
else
    echo "Scripts/activate files found:";
    echo $files | tr " " "\n"
    echo
    echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    for f in $files; 
    do 
        
        
        echo "Copying activate and creating activateCyg file:"
        cp ${f} ${f}Cyg;

        echo ">> "${f}Cyg
        echo
        #echo "Converting activateCyg to unix format using dos2unix:"
        dos2unix -n ${f}Cyg ${f}Cyg
        echo
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        
        final+="${f}Cyg "
        


    done;
    echo "Locations of the unix modified activateCyg files:" 
    echo $final | tr " " "\n"
fi