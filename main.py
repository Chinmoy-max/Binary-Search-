#Binary search happens in sorted array......

def binarySearch(arr,l,u,k):
    if l<u:
        mid=l+(u-l)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            return binarySearch(arr,mid+1,u,k)
        else:
            return binarySearch(arr,l,mid-1,k)
    else:
        return -1 

arr1=[2,6,5,9,8,5]
arr1.sort()
for i in range(len(arr1)):
    print(arr1[i],end=" ")
x=5
result=binarySearch(arr1,0,len(arr1)-1,x)
if result !=1:
    print('\nElement is present at %d'%result)
else:
    print('Not found')

    
