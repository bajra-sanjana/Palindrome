def checkPalindrome(s):		
	length = len(s)	
	for i in range(length/2):
		if s[i] != s[length-i-1]:
			return False
	return True

def findNextPalindrome(n):
	length = len(n)
	nextPalin = [ int(num) for num in n ]
	n_ = int(''.join(str(n)))	
	mid = length/2	
	
	#all digits are 9
	if pow(10,length)-1 == n_:
		temp = str(n_ + 2)
		return temp
				
	#number of digits = 1
	if length == 1:
		temp = str(nextPalin[0] + 1)
		return temp
		
	#number of digits = odd
	if length%2 != 0:		
		if nextPalin[mid-1] <= nextPalin[mid+1]:
			addWithCarry(mid,nextPalin)	
			
	#number of digits = even
	elif length%2 == 0:		
			if nextPalin[mid-1] < nextPalin[mid]:
				addWithCarry(mid-1,nextPalin)
			elif nextPalin[mid-1] == nextPalin[mid]:
				#for number of digits = 2 and the digits are same, this case needs to be handled separately
				if length != 2:				
					if nextPalin[mid-2] <= nextPalin[mid+1]:
						addWithCarry(mid-1,nextPalin)
				else:
					nextPalin[mid-1] += 1
					nextPalin[mid] += 1
			else:	
				nextPalin[mid] = nextPalin[mid-1]		
					
	#copy the first half to second half
	for i in range(mid):			
			nextPalin[length-i-1] = nextPalin[i]
	
	return ''.join([str(num) for num in nextPalin])	
	
#Digit-wise addition
def addWithCarry(start,array):
	digit = 1	
	carry = 0
	for i in range(start,-1,-1):
		temp = array[i] + digit + carry
		if temp > 9:
			carry = 1
			temp -= 10
		else:
			carry = 0
		array[i] = temp						
		digit = 0
	return array
	
if __name__ == 	"__main__":		
	s = raw_input('Enter a number: ')
	if checkPalindrome(s):
		print 'The given number is a palindrome'
	else:
		print 'The given number is not a palindrome'
	print 'The next palindrome number is ',findNextPalindrome(s) 