import timeit
import time
import matplotlib
import matplotlib.pyplot as plt


def iterative(a, n):
    r= 1
    for i in range(n):
        r= r*a
    
    return r





def divandconq(a, n):
    #base case
    if (n==0):
        return 1
    if (n%2==1): #multiply a and decrement power so it's divisible by 2
        sub_problem= divandconq(a, (n-1)//2) 
        return (sub_problem**2) * a #a^1 multiplied by both halves/subproblems

    else:
        sub_problem= divandconq(a, n//2)
        return sub_problem**2 #same without multiplying by 'a' again because power is even






def plotting():
    values= [1, 100, 1000, 10000, 100000, 400000, 700000, 800000, 900000, 950000, 1000000]
    duration=[]

    for i in range(len(values)):
        start= time.perf_counter()
        divandconq(2,values[i])
        end= time.perf_counter() 
        elapsed_time= end-start
        duration.append(elapsed_time)
        time.sleep(0.9)

    plt.plot(values, duration)

    plt.title('Divide and Conquer')
    plt.xlabel('n-value')
    plt.ylabel('time in seconds')
        
    plt.show()






plotting()












