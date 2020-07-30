def print1(a, n): 
  
    for i in range(0,n+1): 
        print(a[i],end=" ")  
    print("") 
    
def sort(a, n): 
  
    for i in range(n,0,-1):  
        for j in range(n, n - i,-1):  
            if (a[j] > a[j - 1]):  
                a[j], a[j-1]=a[j-1], a[j] 
    print1(a,n) 
  
n = 12
a = [2, 100, 5, 39, 18, 20 ,7283, 2, 9, 5, 2, 0] 
  
sort(a, n-1) 
  