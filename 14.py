class disk:
	def __init__(self, id, pos):
		self.id = id
		self.pos = pos
		self.first = 2 ** (id - 1) - 1
		self.step = (self.first + 1) * 2

	def move(self, stacks, is_odd):
		crrnt = self.pos
		self.pos = self.getNext(is_odd)
		if len(stacks[self.pos - 1]) > 0 and \
				stacks[self.pos - 1][0].id < self.id:
			self.pos = self.getNext(is_odd)

		stacks[crrnt - 1].pop(0)
		stacks[self.pos - 1].insert(0, self)

		print(str(crrnt)+" "+str(self.pos))

	def getNext(self, is_odd):
		next = -1 if is_odd else 1
		next += self.pos
		if next < 1: return 3
		elif next > 3: return 1
		return next

def getMovDisk(step, disks):
	if step % 2 == 0:
		return disks[0]
	for n in range(len(disks) - 1, 0, -1):
		if (step - disks[n].first) % disks[n].step == 0:
			return disks[n]

n = int(input())
odd = True if (n % 2 == 1) else False
moves = (2 ** n) - 1
print(moves)

disks = []
stacks = [[], [], []]
for i in range(1, n + 1):
	d = disk(i, 1)
	disks.append(d)
	stacks[0].append(d)

for i in range(moves):
	getMovDisk(i, disks).move(stacks, odd)
