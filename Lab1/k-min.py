import random
import pygame

def CorrectnessTest():
	elements = [5, 10, 1, 6, 14, 8, 3, 25, 32, 11,
				9, 17, 21, 30, 19, 7, 0, 38, 28, 16,
				31, 42, 37, 26, 15, 24, 12, 27, 4, 20,29]
	k = 19
	K_MinResult = K_Min(elements,k)
	elements.sort()
	RightAns = elements[k-1]
	if(K_MinResult == RightAns):
		print("K_Min result is:", K_MinResult,'\nThe correct answer is:', RightAns, "\nAlgorith is correct");
	else:
		print("Algorith's answer is wrong")

def AbilityTest():
	clock = pygame.time.Clock()
	list = generate(random.randint(10,10000))#随机生成一个数列
		
	k = random.randint(1, len(list))#第k个
	start_time = pygame.time.get_ticks()
	K_MinResult = K_Min(list, k)#第k个数字
	time = pygame.time.get_ticks()-start_time

	list.sort()
	if K_MinResult == list[k-1]:
		print("\nK_Min result is:", K_MinResult,'\nThe correct answer is:', list[k-1], "\nAlgorith is correct");	
	else:
		print("Algorith's answer is wrong")
	print("Time:", time, 'ms')

def K_Min(elements, Kth):
	smaller_than_pivot = []
	bigger_than_pivot = []
	equal_pivot = []
	piovt = select(elements, 5)
	if Kth < 1 or Kth > len(elements):
		return 'Kth out of range'
	for element in elements:
		if element == piovt:
			equal_pivot.append(element)
		elif element < piovt:
			smaller_than_pivot.append(element)
		else:
			bigger_than_pivot.append(element)
	if len(smaller_than_pivot) + 1 == Kth:
		return equal_pivot[0]
	elif len(smaller_than_pivot) + 1 < Kth:
		return K_Min(bigger_than_pivot, Kth - len(smaller_than_pivot) - 1)
	else:
		return K_Min(smaller_than_pivot, Kth)
	
			

def select(elements, GroupNum):
	# level += 1
	Groups = []#用于将数列分组，每组最多GroupNum个
	MidNum_in_Groups = []
	i = 0
	while i * GroupNum < len(elements):
		#GroupNum个一组，分成二维数组
		if i * GroupNum < len(elements) - 1:
			Groups.append(elements[i * GroupNum: i * GroupNum + GroupNum])
		else:
			Groups.append(elements[i * GroupNum: len(elements)])
		i += 1
	# print('level', level,' group :\t', Groups)
	for group in Groups:
		#每一组排序找出中位数，加入中位数group
		group.sort()
		MidNum_in_Groups.append(group[int(len(group) / 2)])
	# print('level', level, 'MidNum_in_Groups :\t',MidNum_in_Groups)
	if len(MidNum_in_Groups) != 1:
		#若中位数group的长度大于GroupNum，递归寻找中位数
		return select(MidNum_in_Groups, GroupNum)
	else:
	 	#print('level', level, ' return num:\t', MidNum_in_Groups[int(len(MidNum_in_Groups) / 2)])
		#否则直接找出中位数并返回
		return MidNum_in_Groups[0]

def generate(n):
	list = []
	for i in range(0,n-1):
		ran = random.randint(0, n)
		if ran not in list:
			list.append(ran)
	return list

if __name__ == '__main__':
	CorrectnessTest()#正确性测试
	AbilityTest()#性能测试