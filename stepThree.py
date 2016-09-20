#
# Note: When I read files, I don't usually use "f = open('input.txt', 'r')"
# I just execute
# python filename.py < input.txt 
# Just in case whoever is reading this doesn't know.  
#
import math
vectors = []
distanceCounter = 0

#
# While loop that collects all given xyz coordinates.
#
while True:
    try:
        vectors.append(raw_input().split(' '))
    except EOFError:
        break

f = open('output.txt', 'w')

#
# For loop that calculates the distance from the origin to each XYZ coordinate,
# as well as noting any distances above 200.
#
for x in range(len(vectors)):
    distance = math.floor(math.sqrt(int(vectors[x][0])**2 + int(vectors[x][1])**2 + int(vectors[x][2])**2))
    if distance > 200:
        distanceCounter += 1
    distance = int(distance)
    print >> f, distance

print >> f, distanceCounter
 
 

    
