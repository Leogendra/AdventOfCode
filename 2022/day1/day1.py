top1 = 0
top2 = 0
top3 = 0
with open("2022/day1/input.txt", "r") as f:
	elf = 0
	for line in f.readlines():
		if line != "\n":
			elf += int(line)
		else:
			if elf > top1:
				top3 = top2
				top2 = top1
				top1 = elf
			elif elf > top2:
				top3 = top2
				top2 = elf
			elif elf > top3:
				top3 = elf
			elf = 0

print(top1+top2+top3)