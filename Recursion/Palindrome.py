st=input("Enter the String to check:\n")
def palindrome(arr,low=0,high=None):
    if high==None:
        high=len(arr)-1
    if low>=high:
        return 
    else:
        if arr[low]!=arr[high]:
            return False
    palindrome(arr,low+1,high-1)
    return True
print(f"The given string is a palindrome ?? = {palindrome(st)}")