#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。


def charFreqLister(inputSTR):
    resultLIST = []
    freq = {}
    
    for x in inputSTR:
        freq[x] = inputSTR.count(x) 
        freq[x]=  freq[x]/len(inputSTR)   
    for y in freq:
        resultLIST.append([freq[y], y])
    
    resultLIST.sort(key=lambda input:input[0], reverse=True)
    return resultLIST    

# 3.1 加分 \(*_*)/
# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST
def huffmanTranslater(L):
    L1=L
    def FIND(w):
        
        k=1
        a1=0
        value=w[0][0]
        while(k<len(w)):
            
            if(w[k][0]<value):
                value=w[k][0]
                a1=k
            k=k+1
        return a1
    def dic(dc,A,B):
        la=len(A)
        lb=len(B)
        k=1
        while(k<la):
            dc[A[k]]=dc[A[k]]+'0'
            k=k+1
        k=1
        while(k<lb):
            dc[B[k]]=dc[B[k]]+'1'
            k=k+1
        return dc
    
    long=len(L)
    k=0
    dict1={}
    while(k<long):
    
        dict1[L[k][1]]=""
        k=k+1

    tree=[]
    k=0
    while(k<long):
        tree.append(L[k])
        k=k+1

    while(len(tree)>1):
    
        A1=list(tree[FIND(tree)])
        tree.pop(FIND(tree))
        A2=list(tree[FIND(tree)])
        tree.pop(FIND(tree))
        dict1=dic(dict1,A1,A2)
        A1.insert(0,(A1[0]+A2[0]))
        A1.pop(1)
        A2.pop(0)
        A1=A1+A2
    
        tree.append(A1)

    L=len(L1)
    k=0
    while(k<L):
        g=dict1[L1[k][1]]
        g=g[::-1]
        L1[k].append(g)
        k=k+1
    return(L1)

if __name__ == '__main__':
    inputSTR=input('輸入一字串')
    L=charFreqLister(inputSTR)
    L1=huffmanTranslater(L)
    print(L1)



# 4 請參考以下 condNOT() 的例子，設計四個 func() 依以下條件，能算出 condition02 ~ 04 的值

#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    output= ""    
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="1" and y =="1":
            output = output + "1"
        else: 
            output = output + "0"
        
    
    return output

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    output = ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x=="0" and y=="0":
            output = output + "0"
        else:
            output = output + "1"
        
    
    
    
    return output

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    output = ""
    for (x,y) in zip(inputSTR_X,inputSTR_Y):
        if x == "0" and y =="0":
            output = output + "0"
        elif x == "1" and y == "1":
            output = output + "0"
        else: 
            output = output + "1"
            
    return output



if __name__== "__main__":
    condition00X = ""
    condition00Y = ""

    condition01 = condNOT(condition00X)
    print(condition01)

    # 5 請完成以下課本習題並將答案以字串型 (str or unicode) 填入。
    # Ch3 表示為第三章
    # P3_20a 表示為該章最後 Problem 處的 P3-20 題的第 a 小題。
    
    print("Ans:")
    Ch3P3_20a = ""
    Ch3P3_20b = ""
    Ch3P3_20c = ""
    Ch3P3_20d = ""
    print("========")
    Ch3P3_28a = ""
    Ch3P3_28b = ""
    Ch3P3_28c = ""
    Ch3P3_28d = ""
    print("========")
    Ch3P3_30a = ""
    Ch3P3_30b = ""
    Ch3P3_30c = ""
    Ch3P3_30d = ""
    print("========")
    Ch4P4_3a = ""
    Ch4P4_3b = ""
    Ch4P4_3c = ""
    Ch4P4_3d = ""
    print("========")
    Ch4P4_4a = ""
    Ch4P4_4b = ""
    Ch4P4_4c = ""
    Ch4P4_4d = ""
    print("========")
    Ch4P4_13a = ""
    Ch4P4_13b = ""
    Ch4P4_13c = ""
    Ch4P4_13d = ""
    print("========")
    Ch4P4_15a = ""
    Ch4P4_15b = ""
    Ch4P4_15c = ""
    Ch4P4_15d = ""
    print("========")
    Ch4P4_16a = ""
    Ch4P4_16b = ""
    Ch4P4_16c = ""
    Ch4P4_16d = ""
