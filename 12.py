input_str = input()

str_collection = {}
for char in input_str:
	if char not in str_collection:
		str_collection[char] = 1
	else:
		str_collection[char] += 1

if len(str_collection) == 1:
	print(input_str)
	quit()

odd = ""
for char in str_collection:
	if str_collection[char] % 2 != 0:
		if odd != "":
			print("NO SOLUTION")
			quit()
		odd = char

palindrome = ""
for char in str_collection:
	if char != odd:
		for _ in range(0, str_collection[char] // 2):
			palindrome += char

emordnilap = ""
count = len(palindrome)
for i in range(count - 1, -1, -1):
	emordnilap += palindrome[i]

if odd == "":
 	print(palindrome + emordnilap)
else:
	odds = ""
	for _ in range(0, str_collection[odd]):
		odds += odd
	print(palindrome + odds + emordnilap)
