# This Python file uses the following encoding: utf-8
# this file contain all functions used in the main
from __future__ import division
import numpy as np
from random import random,uniform
from math import floor, exp

def permutCol ( i , j , pt) :
    tmp = np.copy( pt[:, i] )
    pt[:, i] = pt[:, j]
    pt[:, j] = tmp
    return 0
def permutSeq (i , j , seq ) :
    tmp = seq[i]
    seq[i] = seq[j]
    seq[j] = tmp
    return 0

def solIni ( n , m , pt ) :
    # we are going to sort jobs according to its prcessing time in the first machine
    arrInst  =  pt
    m1 = np.array(np.sort(pt[0]))
    
    print m1[1]
    print arrInst[0,0]
    seq = [i for i in range(1,n+1)]
    for i in range(n):
        for j in range(n) :
            if  arrInst[0,j]== m1[i]:
                permutCol(i,j,arrInst)
                permutSeq(i,j,seq)
    return seq , arrInst

def solIni1 ( n , m , pt ):
    arrInst = pt
    seq = [i for i in range(1,n+1)]
    return seq , arrInst
def voisin( n , m , pt , seq) : 
    clonePt = pt
    cloneSeq = seq
    i = int( floor( (n-1)*random()) )
    j = 0
    prob = random()
    p = 0.5
    if i == 0 :
        j = n-1        
    elif i == n-1 :
        j = 0
    elif p > prob :
        j = i - 1
    else :
        j = i + 1
    permutCol( i , j , clonePt )
    permutSeq( i , j , cloneSeq )  
    return clonePt , cloneSeq
 
def voisin1( n , m , pt , seq) : 
    clonePt = pt
    cloneSeq = seq
    i = int( floor( (n-1)*random()) )
    j = 0
    prob = random()
    p = 0.5
    if i == 0 :
        j = n-2        
    elif i == n-1 :
        j = 1
    elif i == 1 :
        j = n-1
    elif i == n-2 :
        j = 0
    elif p > prob :
        j = i - 2
    else :
        j = i + 2
    permutCol( i , j , clonePt )
    permutSeq( i , j , cloneSeq )  
    return clonePt , cloneSeq   
     
def makeSpan( n , m , pt ) :
    startL = np.zeros(shape=(m,n))
    endL   = np.zeros(shape=(m,n))
    
    
    tmp = 0 
    for i in range( n-1 ) : 
        tmp = tmp + pt[0,i]
        startL[0, i+1 ] = tmp 
    tmp = 0 
    for i in range( m-1 ) :
        tmp = tmp + pt[i,0]
        startL[i+1 , 0] = tmp
    tmp = 0
    for i in range( n ) : 
        tmp = tmp + pt[0,i]
        endL[0, i ] = tmp
    tmp = 0
    for i in range( m ) :
        tmp = tmp + pt[i,0]
        startL[i , 0] = tmp
    for i in range( 1 , m ) :
        for j in range(1 , n ):
            startL[ i , j ] = max(endL[i-1 , j ],endL[i , j-1 ])
            endL[ i , j ]   = startL[ i , j ] + pt[ i , j ]
    makeS = endL[ m-1 , n-1 ]      
    return makeS
   
def simAnneal ( n, m, pt ) :
    
    ######## Les paramètres  ##########
    T0 = 70
    T  = T0
    Tmin = 0.0001
    alpha =0.85
    lPlateau = 40
    delta = 0
    mult = 0 
    ####################################

    seqSol , solutionIni = solIni ( n , m , pt )
    makeSIni = makeSpan(n , m , solutionIni )
    miniMakeS = makeSIni
    SeqOpt = seqSol
    while T >= Tmin :
        for leng in  range ( 1 , lPlateau ):
            # Ici choisir le type de voisin entre ( voisin , voisin1 , voisin2 , voisin3)
            voisinS , seqSol = voisin( n , m , solutionIni , seqSol )
            makeS = makeSpan( n , m , voisinS )
            delta = makeS - makeSIni
            makeSIni = makeS
            if delta <= 0 :
                solutionIni = voisinS
            else:
                proba = random()
                if proba <= exp(-delta/T) :
                    solutionIni = voisinS
            if makeS < miniMakeS :
                SeqOpt = seqSol
                miniMakeS = makeS
                
        T = T * alpha
        mult += mult
    return SeqOpt , miniMakeS

def saveDat(seqOpt , miniMakeSpan , resultSave ) :
    strSeq = map(str, seqOpt)
    string = "la sequence optimale est :  [" + ','.join(strSeq)+ "]"
    resultSave.write( string )
    resultSave.write("\nCmax  =  " +str(miniMakeSpan))
    return 0
