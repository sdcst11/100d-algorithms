#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
  sec=""
  a4=a
  b4=b
  a2=str(a)
  b2=str(b)
  x2=a2+b2
  sec=sec+x2
  con=True
  
  while con==True:
    x=a+b
    if x>10:
      x=str(x)
      a=x[0]
      b=x[1]
      a=int(a[0])
      b=int(b[0])
      x=a+b
    if x==10:
      x=1
    x=str(x)
    sec=sec+x
    a=int(sec[-1])
    b=int(sec[-2])
    s=[sec[-1],sec[-2]]
    a3=int(s[0])
    b3=int(s[1])
    if a3==b4 and b3==a4:
      return sec

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
