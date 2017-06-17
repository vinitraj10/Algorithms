'''
In this method we will be finding the anagram in O(n) time by using counting the elements of array.



'''
no_of_characters=256

def isAnagram(str1,str2):
	check_1=[0]*no_of_characters
	check_2=[0]*no_of_characters

	for i in str1:
		check_1[ord(i)]+=1
	for i in str2:
		check_2[ord(i)]+=1

	return check_1==check_2

print("Enter the first String")
first_string=input()
print("Enter the second String")
second_string=input()

if isAnagram(first_string,second_string):
	print("The given strings are anagram of each other ")
else:
	print("Not Anagram")