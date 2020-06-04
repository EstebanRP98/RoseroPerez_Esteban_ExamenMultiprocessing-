# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:00:56 2020

@author: EstebanRM
"""

import random

import time
import concurrent.futures
import multiprocessing

def how_many_max_values_sequential(ar):

    #find max value of the list

    maxValue = 0

    for i in range(len(ar)):

        if i == 0:

            maxValue = ar[i]

        else:

            if ar[i] > maxValue:

                maxValue = ar[i]

    #find how many max values are in the list

    contValue = 0

    for i in range(len(ar)):

        if ar[i] == maxValue:

            contValue += 1
    
    return contValue


# Complete the how_many_max_values_parallel function below.
def cuantos(ar):
        print("entra1")
        maxValue = 0
        maxValue = ar[i]
        for i in range(len(ar)):
            if i == 0:
                maxValue = ar[i]
            else:
                if ar[i] > maxValue:
                    maxValue = ar[i]
        return maxValue

def contar(maxValue,ar):
        print("entra2")
        contValue = 0
        for i in range(len(ar)):
            if ar[i] == maxValue:
                contValue += 1
        return contValue

def how_many_max_values_parallel():
    ar_count = 400000
    ar1 = [random.randrange(1,4) for i in range(int(ar_count/2))]
    ar2 = [random.randrange(1,4) for j in range(int(ar_count/2),ar_count)]
    maxValue = 0
    contValue = 0
    def cuantos(ar):
        print("entra1")
        maxValue = 0
        for i in range(len(ar)):
            if i == 0:
                maxValue = ar[i]
            else:
                if ar[i] > maxValue:
                    maxValue = ar[i]
    return maxValue
    
    def contar(maxValue):
        print("entra2")
        contValue = 0
        for i in range(len(ar)):
            if ar[i] == maxValue:
                contValue += 1
    return contValue
     
    
    #implement your solution
    return res


if __name__ == '__main__':
       
    ar_count = 1000
    ar1 = [random.randrange(1,4) for i in range(int(ar_count/2))]
    ar2 = [random.randrange(1,4) for j in range(int(ar_count/2),ar_count)]
    inicioPar = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future=executor.submit(cuantos,ar1)
        cuantos1=future.result()
        future2=executor.submit(contar,cuantos1,ar1)
        res1=future2.result()
        print(res1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future=executor.submit(cuantos,ar2)
        cuantos2=future.result()
        future2=executor.submit(contar,cuantos2,ar2)
        res2=future2.result()
        print(res2)
    
    res=res1+res2
    print(res)
   
    

    resultPar=res
    print(resultPar)

    finPar = time.time()   
    #Generate ar_count random numbers between 1 and 30

    #ar = [random.randrange(1,4) for i in range(ar_count)]
    
    ar=ar1+ar2
    inicioSec = time.time()

    resultSec = how_many_max_values_sequential(ar)
    print("respuesta")
    print(resultSec)

    finSec =  time.time()

   

    

    

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))