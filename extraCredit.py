import sys
import math
#
# Collecting Variables
#
print "Enter coordinates by time they recieved the signal in increasing order"
print "FORMAT: X Y"
print "---------------------------------"
print "coordinate one:"
coordOne = raw_input().split(' ')
print "the time when sound was recieved should be zero"
print "---------------------------------"
print "coordinate two:"
coordTwo = raw_input().split(' ')
print "time between first point and second point for signal reception, decimal form:"
T2 = float(raw_input())*1481.0
print "---------------------------------"
print "coordinate three:"
coordThree = raw_input().split(' ')
print "time between first point and third point for signal reception, decimal form:"
T3 = float(raw_input())*1481.0
print "---------------------------------"

#
# Assigning variables 
#
X1 = float(coordOne[0])
Y1 = float(coordOne[1])
X2 = float(coordTwo[0])
Y2 = float(coordTwo[1])
X3 = float(coordThree[0])
Y3 = float(coordThree[1])

#
# Calculations for X, Y(coordinates of transmitter) relation;
# X = m*Y + n
# linear form
#
m = (2*T2*(Y1-Y3)-2*T3*(Y1-Y2))/(2*T2*(X3-X1)-2*T3*(X2-X1))
n = (T2*(X3**2+Y3**2-X1**2-Y1**2-T3**2)-T3*(X2**2+Y2**2-X1**2-Y1**2-T2**2))\
/(2*T2*(X3-X1)-2*T3*(X2-X1))

#
# D represents coefficients;
# D1X + D2Y + D3 = sqrt( (X-X1)^2 + (Y-Y1)^2 ) 
# (calculated from equation describing relation of B to C and A to C in problem 4)
# Generically, it would be point 2 to point 1 and point 3 to point 1 
#
D1 = (-2*(X3-X1))/(2*T3)
D2 = (2*(Y1-Y3))/(2*T3)
D3 = (X3**2+Y3**2-X1**2-Y1**2-T3**2)/(2*T3)

#
# Three coefficients in quadratic formula to solve for Y;
# A*Y^2+B*Y+C = 0
# Derived from (D1X + D2Y + D3)^2 =  (X-X1)^2 + (Y-Y1)^2 
# (look to previous 2 comments)
# A represents values with coefficients of Y^2
# B represents values with coefficients of Y
# C represents values without coefficients(constant)
#
A = (D1*m+D2)**2 - m**2 - 1
B = 2*(D1*m+D2)*(D1*n+D3) - 2*m*(n-X1) + 2*Y1
C = (D1*n+D3)**2 - (n-X1)**2 - Y1**2

#
# If "B**2 - 4*A*C" (of the quadratic equation) is negative,
# there is no solution. This deals with that scenario.
#
if B**2 - 4*A*C < 0:
	sys.exit("No solution")

#
# Implement quadratic formula to find solution(s) Y
#
YSolution1 = (-B + math.sqrt(B**2-4*A*C))/(2*A)
YSolution2 = (-B - math.sqrt(B**2-4*A*C))/(2*A)

#
# Uses X = m*Y + n (see comments above)
# to solve for X with Y.
#
XSolution1 = m*YSolution1+n
XSolution2 = m*YSolution2+n

#
# Checks if each solution(X, Y) works with each equation
# describing the relation of B to C and A to C
# (in the scenario of problem 4, being listed as an example)
#
print "Apporximate solution(s):"

if round(math.sqrt((XSolution1-X2)**2 + (YSolution1-Y2)**2)\
- math.sqrt((XSolution1-X1)**2+(YSolution1-Y1)**2), 4) == round(T2, 4):
	if round(math.sqrt((XSolution1-X3)**2+(YSolution1-Y3)**2)\
	- math.sqrt((XSolution1-X1)**2+(YSolution1-Y1)**2), 4) == round(T3, 4):
		print XSolution1, YSolution1

if round(math.sqrt((XSolution2-X2)**2 + (YSolution2-Y2)**2)\
- math.sqrt((XSolution2-X1)**2+(YSolution2-Y1)**2), 4) == round(T2, 4):
	if round(math.sqrt((XSolution2-X3)**2+(YSolution2-Y3)**2)\
	- math.sqrt((XSolution2-X1)**2+(YSolution2-Y1)**2), 4) == round(T3, 4):
		if XSolution2 == XSolution1 and YSolution1 == YSolution2:
			sys.exit()
		else:
			print XSolution2, YSolution2