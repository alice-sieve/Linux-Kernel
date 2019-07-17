#! /bin/bash
input="2.txt"
#reading url line by line from 2.txt
while IFS= read -r line
do 
    #trimming *https://www.spinics.net/lists/* from url and making text file per mailing list
    linkt="$line" 
    string2=${linkt#"https://www.spinics.net/lists/"}
    string2=${string2%"/"}
    #currently accepting all the urls of a page
    lynx -listonly -dump "$line" >> "$string2.txt"
done < "$input"
