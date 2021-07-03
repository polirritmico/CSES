# t = int(input())
test_input = open("test_input.txt", "r")
test_output = open("test_output.txt", "r")
t = int(test_input.readline())
print("{} test en cola.".format(t))


for i in range(t):
	# input_str = input().split()
	# input_str = "90000 90000".split()
	input_str = test_input.readline().rstrip()
	ua, ub = input_str.split()
	ua, ub = int(ua), int(ub)
	r = False
	if ub > ua:
		ua, ub = ub, ua
	if not ua > 2 * ub:
		a, b = ua % 3, ub % 3
		if b > a:
			a, b = b, a
		if a + b == 0:
			r = True
		elif a == 2 * b:
			r = True
	# if r:
	# 	print("YES")
	# else:
	# 	print("NO")

	test = test_output.readline().strip()
	check = True if test == "YES" else False

	if r != check:
		print("Error en test {} con valores: ua = {} y ub = {}".format(
			i, ua, ub))
		print("Línea {} dice {}, pero {} fue el resultado.".format(
			i, check, r))

		test_input.close()
		test_output.close()
		quit()