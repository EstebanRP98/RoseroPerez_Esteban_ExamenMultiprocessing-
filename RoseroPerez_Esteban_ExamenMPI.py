# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:03:00 2020

@author: EstebanRM
"""

import random
from mpi4py import MPI
import time
import concurrent.futures

MASTER = 0
FROM_MASTER = 1
FROM_WORKER = 2  
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
worldSize = comm.Get_size()
numworkers = worldSize-1

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

def how_many_max_values_parallel(ar):
    
    if(rank == MASTER):
        maxValue = 0
        mtype = FROM_MASTER
        for i in range(len(ar)):
            if i == 0:
                maxValue = ar[i]
            else:
                if ar[i] > maxValue:
                    maxValue = ar[i]
                
        comm.send(maxValue,dest=1,tag=mtype)  
        mtype = FROM_WORKER
       
        for i in range(numworkers):
            source = i
            final = comm.recv(source=source+1,tag=mtype)
            
    #find how many max values are in the list
        
    if(rank > MASTER):
        mtype = FROM_MASTER
        contValue = 0
        maxValue = comm.recv(source=MASTER,tag=mtype)
        for i in range(len(ar)):
            if ar[i] == maxValue:
                contValue += 1
        print("paralelo")
        print(contValue)
        
        
        mtype = FROM_WORKER
        comm.send(contValue,dest=MASTER,tag=mtype)
    #implement your solution
    
    return contValue
 

if __name__ == '__main__':

    ar_count = 1000

    #Generate ar_count random numbers between 1 and 30

    ar = [random.randrange(1,4) for i in range(ar_count)]
    

    inicioSec = time.time()

    resultSec = how_many_max_values_sequential(ar)
    print("resultado")
    print(resultSec)

    finSec =  time.time()

   

    inicioPar = time.time()   

    resultPar = how_many_max_values_parallel(ar)
    print(resultPar)

    finPar = time.time()   

    

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))