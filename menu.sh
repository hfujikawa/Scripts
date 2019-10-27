#!/bin/bash

SELNO=0
while :
do
#
# determine the attribute of selected line
#
    for ((i=0 ; i<=5; i++)){
        if [ "$i" -eq "$SELNO" ] ; then
            attbl[$i]="tput rev"
        else
            attbl[$i]=""
        fi
    }
#
# display menu
#
    clear
    tput cup  2 ; echo "`tput rev`    main menu     `tput sgr0`"
    tput cup  5 ; echo " 1)  `{$attbl[1]}`  initial proc     `tput sgr0`"
    tput cup  7 ; echo " 2)  `{$attbl[2]}`  master register proc     `tput sgr0`"
    tput cup  9 ; echo " 3)  `{$attbl[3]}`  master edit proc     `tput sgr0`"
    tput cup 11 ; echo " 4)  `{$attbl[4]}`  master delete proc     `tput sgr0`"
    tput cup 13 ; echo " 5)  `{$attbl[5]}`  end proc     `tput sgr0`"
#
# input proc when not inputted select no
#
    if [ "$SELNO" -eq 0 ] ; then
        tput cup  18 ; echo -n "   please input proc no.: "
        read ANS
        if [ "$ANS" -lt 1 -o "$ANS" -gt 5 ] ; then
            SELNO=0
        else
            SLENO=$ANS
        fi
    else
        tput cup  18 ; echo -n "   proceed the selected proc?(y): "
        read ANS
        if [ "$ANS" = "y" -o "$ANS" = "Y" ] ; then
            clear
            exit 0
        else
            SELNO=0
        fi
    fi
       
done