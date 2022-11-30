#!python3

"""
There are 2 important pieces of data that are going to be used for this assignment:
curValue : (an integer)
data: a List that specifies whether the item should be skipped or not
False indicates it should be skipped, True indicates it should not be skipped.

Create a funtion that receives 2 input paramters, the curValue and the list Data
Return the index of the next item to be used
"""

from ast import Index


def next(current , myList):
  '''
  determine the next item from the list. The list contains False/True Boolean values
  that indicate whether the current item can be used
  '''
  if True in myList:
    bin=len(myList)-1
    con=True
    while con==True:
      current=current+1

      if current>bin:
        current=0
      ifcan=myList[current]
      print(ifcan , current, myList)
      if ifcan == True:
        con=False
        return current 
  else:
    return None
      


def main():
  data = [False, True, True, False, True, False]
  print(next( 3 , data ))
  assert next( 3 , data ) == 4

  assert next( 4 , data ) == 1
  assert next( 1 , data ) == 2
  data = [True, True, False, False, True, False, True]
  assert next( 1 , data ) == 4
  assert next( 6 , data ) == 0
  assert next( 0 , data ) == 1
  assert next( 3 , data ) == 4
  data = [True, True, False]
  assert next( 1 , data ) == 0
  assert next( 0 , data ) == 1
  data = [False, False, False]
  assert next( 1, data ) == None
  
  
  
  
  
  
  

if __name__ == "__main__":
  main()
