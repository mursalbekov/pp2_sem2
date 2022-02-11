n = int(input())
a = [[ "." for i in range(n)]for j in range (n)]

if (n % 2 == 1) :
     for i in range(n):
      for j in range(n):
          if i + j < n-1:
              a[i][j] = '.'
          else:
              a[i][j] = '#'

        
          print(a[i][j] , end = '')
      print()
else:
   for i in range(n):
    for j in range(n):
          if i >= j:
              a[i][j] = '#'
          if i < j:
              a[i][j] = '.'

        
          print(a[i][j] , end = '')
    print()