import timeit
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



#scoring matrix given, consider row string1 and col string2

#for each value, get s1 with s2, compare with s1 with dash, and s2 with dash,
#highest val, add character to string
#looping on scoring matrix? adds complexity




def memoize(s1,s2,scoring_matrix):
    #row, column
    #initialize matrix of zeroes with len(s2)+1 rows and len(s1)+1 columns (+1 for '-')
    max_matrix= np.zeros((len(s2)+1 ,len(s1)+1))

   
    max_matrix[0][0]=0
    #first row, score of aligning first string with string of gaps
    for i in range(1,len(s1)+1):
        max_matrix[0][i]= round(max_matrix[0][i-1] + scoring_matrix[s1[i-1]]['-'],2)

    #first column, score of aligning second string with string of gaps
    for j in range(1, len(s2)+1):
        max_matrix[j][0]= round(max_matrix[j-1][0] + scoring_matrix['-'][s2[j - 1]],2)
    

    #rest of matrix
    for i in range(1, len(s2)+1): #rows
        for j in range(1, len(s1)+1): #columns
            match_score = scoring_matrix[s1[j - 1]][s2[i - 1]]
            max_matrix[i][j] = max(
               round((max_matrix[i - 1][j - 1] + match_score),2),
                round((max_matrix[i - 1][j] + scoring_matrix['-'][s2[i - 1]]),2),
                round((max_matrix[i][j - 1] + scoring_matrix[s1[j - 1]]['-']),2)
            )

    return max_matrix
    
def highest_alignment(s1, s2, scoring_matrix):

    max_matrix= memoize(s1,s2,scoring_matrix)

    #constructing the string that gets highest alignment score
    string1=  '' #start with empty strings
    string2 = ''
    i= len(s2)
    j = len(s1)
    while i > 0 and j > 0:
        if max_matrix[i][j] ==  round(scoring_matrix[s1[j - 1]][s2[i - 1]] + max_matrix[i - 1][j - 1],2):
            string1 = s1[j - 1] + string1
            string2 = s2[i - 1] + string2
            i -= 1
            j -= 1
        elif max_matrix[i][j] == round(scoring_matrix['-'][s2[i - 1]] + max_matrix[i-1][j],2):
            string1 = '-' + string1
            string2 = s2[i-1] + string2
            i -= 1
        else:
            string1 = s1[j - 1] + string1
            string2 = '-' + string2
            j -= 1

    #filling rest of strings with gaps/string characters
    if j > 0:
        while j>0:
            string1 = s1[j - 1] + string1
            string2 = '-' + string2
            j -=1
    elif i>0:
        while i>0:
            string1 = '-' + string1
            string2 = s2[i-1] + string2
            i -=1

    return string1, string2




scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': -5}
}

# s1= 'ATGCC'
# s2= 'TACGCA'
s1= 'TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC'
s2= 'AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC'

memoized_matrix= memoize(s1,s2,scoring_matrix)

for i in (memoized_matrix):
    print(i)


alignment_x, alignment_y = highest_alignment(s1, s2, scoring_matrix)
print("Alignment of x and y:")
print(alignment_x)
print(alignment_y)




