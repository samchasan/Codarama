#ALL THIS IS ON LEONECKERT.COM IN BLOG


import sys, os
import random
print random.random()

a = [2,3,4,6,0]
print random.choice(a)
print random.sample(a,3)

print "\n Today we learned this:"

for f in os.listdir("."):
    print ">>>>> ", f

print " "

print " "
print sys.argv # returns a list with an argument
