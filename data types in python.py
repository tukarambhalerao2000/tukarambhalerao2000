#Write a program to manipulate List data

A=['tukaram','shubham','siddeshwar','kunal','Yash','abc',64,44,29,66,00]

print("\n\nList A :",A[:])

print("List A : 2 to 5",A[2:6])

print("List A In Reverse:",A[::-1])

A.append('shubham')
print("List A After Appending  :",A[:])

A.insert(4,'siddeshwar')
print("List A After Inserting  :",A[:])

A.pop(4)
print("List A After Poping :",A[:])

A.remove('abc')
print("List A After Removing :",A[:])

del A[0]
print("List A After Deleteing :",A[:])

A.clear()
print("List A After Clearing :",A[:])

#Write a program to manipulate Tuple data

B=("tukaram","shubham","siddeshwar","kunal","Yash","abc","suyash",64,44,29,0)

print("\n\nTuple B:",B)

print("Tuple B: 2 to 5",B[2:6])

print("Tuple B in Reverse:",B[::-1])

print("Count of shubham is :",B.count('shubham'))
print("Index of shubham",B.index('shubham'))
