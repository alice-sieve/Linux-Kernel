#! /bin/bash
input="spinics-linux-fedora"
#reading url line by line from spinics-linux-fedora
while IFS= read -r line
do 
    #trimming *https://www.spinics.net/linux/fedora/* from url and making text file per mailing list
    linkt="$line"
    string2=${linkt#"https://www.spinics.net/linux/fedora/"}
    string2=${string2%"/"}
    #currently accepting all the urls of a page
    lynx -width=1000 -list_inline -dump "$line" | grep "PATCH" > "$string2.txt"
done < "$input"
