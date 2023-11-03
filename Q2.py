import time
import matplotlib.pyplot as plt
import random


def sumPairs(S,a):
    pairs=[]
    #first sort
    mergeSort(S)

    #perform binary search
    index= binarySearch(S,a) 

    #index is last index with value=a or value<a
    #everything else in list is excluded as it's > a

    first=0
    last=index

    while(first<last):


         sum= S[first] + S[last]

         if (sum==a):
             pairs.append((S[first], S[last]))
             first+=1
             last-=1
    
         if (sum<a):
              first+=1
         if(sum>a):
              last-=1

    return pairs


    






def mergeSort(S):
    length= len(S)

    #base case, stop when i have 1 element in list
    if (length>1):
        mid= length//2
        left= S[:mid] #will include all elements excluding the one at middle index
        right= S[mid:] #mid inclusive, until last element


        #next call mergeSort on left and right halves
        mergeSort(left)
        mergeSort(right)

        merge(S,left,right) #actually merging the sorted lists together

def merge(S, left, right):
    i=0
    j=0
    k=0 #indices starting from 0

    while(i<len(left) and j<len(right)): #sorting left and right into S
        if (left[i] >= right[j]): #taking smaller value of the two lists and sorting it into S
            S[k]= right[j]
            j+=1
        else:
            S[k]= left[i]
            i+=1
        
        k+=1

    #checking if either of 2 halves still have values

    while(i<len(left)):
        S[k]= left[i]
        i+=1
        k+=1

    while(j<len(right)):
        S[k]=right[j]
        j+=1
        k+=1


def binarySearch(S, a):
    left=0
    right= len(S)-1

    mid= left + (right-left)//2

    while(left<=right):
        mid= left + (right-left)//2


        if(left==right):
            if (S[mid]>a):
                return mid-1
            else:
                return mid

        if (S[mid]>a):
            right=mid-1

        elif (S[mid]<a):
            left=mid+1

        else:
            return mid

        





def plotting():
    range_start=1
    range_end=100
    values= [1, 100, 1000, 10000, 100000, 400000, 700000, 800000, 900000, 950000, 1000000]
    
    #values= [1,50,100,1000,5000,10000,80000,100000,300000,700000,900000,1000000]

    duration=[]

    for i in range(len(values)):
        random_values= [random.randint(range_start, range_end) for _ in range(values[i])]
        sum= random.randint(range_start, range_end)

        start_time= time.perf_counter()
        sumPairs(random_values, sum)
        end_time= time.perf_counter()
        elapsed= end_time-start_time
        duration.append(elapsed)
        time.sleep(0.6)

    
    plt.plot(values, duration)

    plt.title('Sum-Pairs')
    plt.xlabel('n-value')
    plt.ylabel('time in seconds')
        
    plt.show()



    

    
