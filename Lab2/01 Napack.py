import random


def Knap(Start, End, Weight, Items):
	if Start == End and Weight >= 0:
		return (0,[])
	elif Weight < 0:
		return (-9999, [])
	else:
		ChooseThisOne = Knap(Start + 1, End, Weight - Items[Start][0], Items)
		NotChooseThisOne = Knap(Start + 1, End, Weight, Items)
		if ChooseThisOne[0] + Items[Start][1] > NotChooseThisOne[0]:
			#if choose this one is better
			ChoosedItems = [Start]
			ChoosedItems.extend(ChooseThisOne[1])
			return (ChooseThisOne[0] + Items[Start][1], ChoosedItems)
		else:
			return NotChooseThisOne

def generate(number):
	Items = []
	for i in range(0, number):
		n = random.randint(1,100)
		m = random.randint(1,100)
		Items.append((n,m))
	return Items

def AbilityTest():
	number = 10
	Items = generate(number)
	print('Item list:',Items)
	Capacity = random.randint(1, number * 50)
	print('Capacity:', Capacity)
	result = Knap(0, len(Items), Capacity, Items)
	print('Maximun value:', result[0])
	print('Choices are:', result[1])

def CorrectnessTest():
	Items = [(2,3),(3,4),(4,5),(5,6)]#(weight, price)
	print('Item list:',Items)
	Capacity = 8
	result = Knap(0, len(Items), Capacity, Items)
	print('Maximun value:', result[0])
	print('Choices are:', result[1],'\n')

if __name__ == '__main__':
	CorrectnessTest()#正确性测试
	AbilityTest()#性能测试