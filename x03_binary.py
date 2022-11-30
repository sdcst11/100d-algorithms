#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""

def toBinary(value):
  '''
  input: value (int)
  return : list of values
  '''
  check=bin(value)
  bir=[]
  a=2
  b=1
  if check=='0b0':
    a0=[0,0,0,0,0,0,0,0]
    return a0
  for i in range(len(check)-2):
    b=b+1
    ape=int(check[b])
    
    bir.append(ape)
    if0=bir[0]
  mal = int(len(bir))
  mal=mal-1
  lai=bir[mal]
  if lai==0:
    bir.insert(0,0)
    del bir[-1]
  if len(bir)==8:
    return bir
  elif if0=='0':
    a0=[0,0,0,0,0,0,0,0]
    return a0
  else:
    num0=len(bir)
    ad0=8-num0
    for i in range(ad0):
      bir.append(0)
  return bir


def toDecimal(myList):
  '''
  input: list of values
  return int
  convert binary to decimal
  '''
  o1=myList[0]
  o2=myList[1]
  o3=myList[2]
  o4=myList[3]
  o5=myList[4]
  o6=myList[5]
  o7=myList[6]
  o8=myList[7]
  ans= (o1 * 2**0)+(o2 * 2**1)+(o3 * 2**2)+(o4 * 2**3)+(o5 * 2**4)+(o6 * 2**5)+(o7 * 2**6)+(o8 * 2**7)
  return ans

def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
