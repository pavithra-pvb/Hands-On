import sys, getopt
sys.argv = ['C:\\a.py', '-h', 'word1', 'word2']
options, arguments = getopt.getopt(sys.argv[1:], 's:t:h')
print(options)

"""
Ans:
A) ['word1', 'word2']
B) [('', '-h')]
C) [('-h', '')] - Ans
D) Error

"""