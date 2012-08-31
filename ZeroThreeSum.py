# File name: ZeroThreeSum.py

def zeroTriple(numList):
   # make sanity checks on numList 
   if len(numList) < 3:
      return []

   # dictionary for storing (sum, [index pair])
   pairSum = {}

   # init pairSum
   key = numList[0] + numList[1]
   pairSum[key] = [0, 1]

   # iterate over indices 2...
   for nn in range(2, len(numList)):
      nextNum = numList[nn]

      # check if nextNum makes a zeroSumTriple with a pre-existing pair          
      if pairSum.has_key(-nextNum):
         return pairSum.get(-nextNum) + [nn]
      else:
         # add pairs (0..nn - 1, nn) 
         for x in range(0, nn):
            pairSum[numList[x] + nextNum] = [x, nn]
            
   return []

#--------- main { -------------

#------ test cases { ----------
# givenList = []
# givenList = [3, 5]
# givenList = [3, 5, -4, 0, 0, 9, -1, -2, 8, 4]

givenList = [3, 5, -78, 0, 70, 9, 8, -2, 8, 4]
#--------- } test cases ------------

ansTriple = zeroTriple(givenList)

if ansTriple == []:
   print '*** NOT_FOUND: No zero triple ****'
else:
   print '==== FOUND: zeroSumTriple: ', ansTriple, ' ===='

#---------- } main -----------
