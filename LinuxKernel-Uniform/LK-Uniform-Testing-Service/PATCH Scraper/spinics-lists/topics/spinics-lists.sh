#! /bin/bash
input="spinics-lists"
#reading url line by line from spinics-lists
while IFS= read -r line
do 
    #trimming *https://www.spinics.net/lists/* from url and making text file per mailing list
    linkt="$line" 
    string2=${linkt#"https://www.spinics.net/lists/"}
    string2=${string2%"/"}
    echo "$string2"
    #currently accepting all the urls of a page
    lynx -width=1000 -list_inline -dump "$line" | grep "PATCH" > "$string2.txt"
done < "$input"
