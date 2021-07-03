inp = input()
out = 1
count = 1
prev = ""
for char in inp:
	if prev == char:
		count += 1
		if count > out:
			out = count
	else:
		count = 1
	prev = char
print(out)
