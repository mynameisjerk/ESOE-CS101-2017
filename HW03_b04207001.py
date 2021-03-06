# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:16:11 2017

@author: rjlin
"""
#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 繳交日期：2016.10.17

# 作業內容：
# 1. 請閱讀 Wikipedia 維基百科 IEEE754 條目 (https://zh.wikipedia.org/wiki/IEEE_754)

# 2. 請試玩 http://armorgames.com/play/17826/logical-element

# 3. 請利用以下空白範本設計一支程式。程式可輸入一段字串，並自動計算出字串中包括空白字元出現的機率。
#    並由高排到低。

def tenToTwo(x):
    integer = abs(int(x))
    floating = abs(x - int(x))
    intList=[]
    floatList=[]
    while integer != 0:
        intList.insert(0, integer % 2)
        integer = int(integer / 2)
    while floating != 0:
        floatList.append(int(floating * 2))
        floating = floating * 2 - int(floating * 2)
    if x < 0:
        intList.insert(0, '-')
    return intList + ['.'] + floatList

def IEEE32(x):
    output = [0] * 32
    if x[0] == '-':
        output[0] = 1
        x.remove('-')
    exponent = 0
    small = False
    for index, value in enumerate(x):
        if value == '.':
            x.remove('.')
            if index != 0:
                exponent = index - 1
            else:
                small = True
                exponent = -1
        elif small:
            if value == 0:
                exponent += -1
            else:
                small = False
                
    print (exponent)
    biExponent = tenToTwo(exponent + 127)
    biExponent.remove('.')
    print (biExponent)
    if biExponent[0] == '-' or exponent + 127 > 255:
        return 'overflow'
    for index, value in enumerate(biExponent):
        output[index+1] = value
              
    x = x + [0]*23
    for index in range(len(output[9::])):
        output[index+9] = x[index+1]
    return output
    
# calculate the 0.XXXX numbers got wrong number



def joinNum(inputList):
    string = ''
    for i in inputList:
        string += str(i)
    return string
        
def pipeLine(x):
    a = tenToTwo(x)
    b = IEEE32(a)  
    c = joinNum(b)
    return c
    

def charFreqLister(inputSTR):
    resultLIST = []
    freq = {}
    
    for x in inputSTR:
        freq[x] = inputSTR.count(x) 
        freq[x]=  freq[x]/len(inputSTR)   
    for y in freq:
        resultLIST.append((freq[y], y))
    
    resultLIST.sort(key=lambda input:input[0], reverse=True)
    return resultLIST

def charList(inputStr):
    dictionary={}
    for i in inputStr:
        if i in dictionary:
            dictionary[i]+=1.0/len(inputStr)
        else:
            dictionary[i]=1.0/len(inputStr)
    return dictionary

# 3.1 加分題 (有做有加分，沒做不扣分)：請用課堂中提到的「霍夫曼編碼]
#     (https://zh.wikipedia.org/wiki/霍夫曼編碼) 為你之前設計的
#     程式加上轉碼壓縮的功能。
# e.g.,
#def huffmanTranslater(inputSTR):
#resultLIST = [(freq, char, code), (freq, char, code), (freq, char, code),...]

#return resultLIST

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
    Ch3P3_20a = "01000000111001100000000000000000"
    Ch3P3_20b = "11000001010010100100000000000000"
    Ch3P3_20c = "01000001001101101000000000000000"
    Ch3P3_20d = "10111110110000000000000000000000"
    print("========")
    Ch3P3_28a = "765"
    Ch3P3_28b = "439"
    Ch3P3_28c = "124"
    Ch3P3_28d = "110"
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
