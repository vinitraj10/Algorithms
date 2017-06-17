'''this solution is uses sorting method to check whether the to given strings are anagram or not...
	Time complexity = O(nlog(n))


'''
def isAnagram(str1,str2):
	str1_list=list(str1)
	str1_list.sort()
	str2_list=list(str2)
	str2_list.sort()

	return (str1_list==str2_list)

if isAnagram(input("Enter first string\n"),input("Enter second string\n")):
	print("The given inputs are anagram")
else:
	print("Not Anagram")