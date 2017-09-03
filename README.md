# Python Sort Example
Examples of how to sort data in Python

## songs.py
The program reads an integer `k` and a separator. Then it reads a bunch of lines where each line contains the title, composer and length of a song separated by the separator. Finally, it outputs the first `k` songs with longest running times in descending order. If songs have the same running time, then we use lexicographic order on the title, and then on the composer, to get a total ordering.

### Sample Input
```
10
|
%z,VwA)IeWe Lqy,JNC(| %iIbNVTU;;P(IVuqGMx|7004
HIcX hx!msCGjUKgv lT|FBUjObOH#uqYZhaoF n)|-72257
;xV^RjhglwHqRWn NrYd|JSu!SGO,jKiJwFKRpWDV|33928
xsKWCAX^rSaZNLsKr*#%|;U,; TrBBbxoL(tvyEQp|-90986
!VhD(awHLgSCcuF;DW$L|qqicTaHXJUtEGboz#YT*|-52638
Nw%FNX$ydEZEcPkWw nP|K$XDSv^()Sy*VPG(cxZf|16842
huI$g,(%!wqQVFNipGhM|aN@i$ztS$RcdMHIdljk!|-28055
KNh$iOHaK!uhr*oDOn$n|N)RW*nr#H;iGFaQp;Rmg|28489
aTPalOKbftnkVonWuYRs|f,dZWVgk@(^LmVOLG%u)|96239
wsPSE!%gCPHwLrrKtycZ|FGozJGNpZJCnuXMq#beI|26540
Ax k(xCF$f@Gw!bYSRP)|$DHWrPoqFJ;PcL*TXdli|-21780
KHJolkgMbKtJ%uoaom@@|HV#BkdgE*LGIwXYLwLLm|89474
qWnx*!)ebcdCv@rKQIYh|GuSRSwgc))dVlHas)W;O|76946
eBoF%*Hl!DdE,C^mbOHa|yWXRYIfNktBX$wyHWLuk|64311
QMq aVzZzoN sr%!LfQK|e%mva%!XwiU@ukHXDcwR|80472
IZ#Sxd$VozVbyNpqoPiF|yufB;xvWIFTpBSqgqJzL|-82368
LGtxx@Z;i@xWDkEsX)uU|R$ENR@vDkyxKZ ;m$ouY|-94180
olNf;uZ,UkmhA#w,mfKC|w*$F#XIidS);FgCuPIbR|30658
toc xp@GmfYj$OVYn#dE|gUqB(O csCCx^#)sHTEd|-39774
WqyOeV@GGConf J PcQL|f,M^ssZrLuUvoM Ifq^p|48800
```

### Sample Output
```
aTPalOKbftnkVonWuYRs|f,dZWVgk@(^LmVOLG%u)|96239
KHJolkgMbKtJ%uoaom@@|HV#BkdgE*LGIwXYLwLLm|89474
QMq aVzZzoN sr%!LfQK|e%mva%!XwiU@ukHXDcwR|80472
qWnx*!)ebcdCv@rKQIYh|GuSRSwgc))dVlHas)W;O|76946
eBoF%*Hl!DdE,C^mbOHa|yWXRYIfNktBX$wyHWLuk|64311
WqyOeV@GGConf J PcQL|f,M^ssZrLuUvoM Ifq^p|48800
;xV^RjhglwHqRWn NrYd|JSu!SGO,jKiJwFKRpWDV|33928
olNf;uZ,UkmhA#w,mfKC|w*$F#XIidS);FgCuPIbR|30658
KNh$iOHaK!uhr*oDOn$n|N)RW*nr#H;iGFaQp;Rmg|28489
wsPSE!%gCPHwLrrKtycZ|FGozJGNpZJCnuXMq#beI|26540
```
