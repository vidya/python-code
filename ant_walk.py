#
#  There is an ant which can walk around on a planar grid. 
#  The ant can move one space at a time left, right, up or down. 
#  That is, from (x, y) the ant can go to (x+1, y), (x-1, y), 
#  (x, y+1), and (x, y-1). Points where the sum of the digits of 
#  the x coordinate plus the sum of the digits of the y coordinate 
#  are greater than 25 are inaccessible to the ant. For example, 
#  the point (59, 79) is inaccessible because 5 + 9 + 7 + 9 = 30, 
#  which is greater than 25. How many points can the ant access 
#  if it starts at (1000, 1000), including (1000, 1000) itself?
#

def point_valid(pt):
  x, y = pt

  ds = 0

  nn = x
  while (nn > 0):
    ds += nn % 10

    if (ds > 25):
      return False

    nn /= 10

  nn = y
  while (nn > 0):
    ds += nn % 10

    if (ds > 25):
      return False

    nn /= 10

  return True


def count_reachable():
  reachable = []
  reachable_set = set()

  reachable.append((1000, 1000))
  reach_count = 1

  reachable_set.add((1000, 1000))

  nn = 0
  while (nn < reach_count):
    x, y = reachable[nn]

    for pt in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
      if (not pt in reachable_set and point_valid(pt)):
        reachable_set.add(pt)

        reachable.append(pt)
        reach_count += 1

    nn += 1

  print 'the ant can access (', reach_count, ') points'

#------------------ main ----------------------
count_reachable()

