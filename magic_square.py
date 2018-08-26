#for nxn magic square, m=n*(n^2+1)/2

#Step 1: is alwyas in the middle row and last column(n/2,n-1)(n starting from 0)

#Step 2: If position of 1 is now taken as(p,q) then the position of 2 is at (p-1,q+1).
#And if the calculated row position becomes equal to -1, then make it n-1 and if column position becomes equal to n, then make it 0.

#Step 3: If the calculated position already contains a number, then decrement the column by 2 and increment the row by 1 .

#Step 4: If anytime row position becomes-1 and column becomes n, switch to (0,n-2).

#y=input("What is the value if N?")
#x=int(y)

def magic_square(n):
    #to make a nxn matrix
    magicSquare=[]
    for i in range(n):
        l=[]
        for i in range(n):
            l.append(0)
        magicSquare.append(l)
        
        # to print a nxn matrix
   # for i in range(n):
    #    for j in range(n):
     #       print(magicSquare[i][j], end=" ")
      #  print()
        
#another cool way using python
# magic=[[0 for i in range(3)] for i range(3)]
      
    i=n//2
    j=n-1
    num=n*n
    count=1
      #magicSquare[i][j]=1
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        i=i-1
        j=j+1
            
          
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
 


y=input("What is the value if N?")
x=int(y)     
magic_square(x)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      