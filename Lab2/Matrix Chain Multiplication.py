import random
def MCM(Start, End, MatrixChain, record):
	for j in range(0, End - Start + 1):
		for i in range(0, End - j + 1):
			if j == 0:
				record[(i, i + j)] = [i + j, 0]
			elif j == 1:
				record[(i, i + j)] = [i + j, MatrixChain[i][0] * MatrixChain[i][1] * MatrixChain[i + j][1]]
			else:
				interium = [0,0]
				for k in range(i, i + j):
					interium[0] = k
					interium[1] = record[(i,k)][1] + record[(k + 1, i + j)][1] + MatrixChain[i][0] * MatrixChain[k][1] * MatrixChain[i + j][1]
					if (i, i + j) not in record.keys():
						record[(i, i + j)] = interium.copy()
					else:
						if record[(i, i + j)][1] > interium[1]:
							record[(i, i + j)] = interium.copy()
	print('At least have to multiply',record[(Start, End)][1], 'times')
	print(output(Start, End, record))
	
def output(Start, End, record):
	if Start == End:
		return 'M'+str(Start)
	elif Start == End - 1:
		return 'M'+str(Start) + '*' + 'M'+str(End)
	else:
		return '(' + output(Start, record[Start, End][0], record) + ')*('+ output(record[Start, End][0]+1, End, record) + ')'

def generate(number):
	MatrixChain = []
	m = random.randint(1,100)
	for i in range(0, number):
		n = random.randint(1,100)
		MatrixChain.append((m,n))
		m = n
	return MatrixChain


def AbilityTest():
	record = {}
	MatrixChain = generate(80)#自动生成一串矩阵
	MCM(0, len(MatrixChain) - 1, MatrixChain, record)

def CorrectnessTest():
	record = {}
	MatrixChain = [(10, 100), (100,5), (5,50)]
	MCM(0, len(MatrixChain) - 1, MatrixChain, record)

if __name__ == '__main__':
	CorrectnessTest()#正确性测试
	AbilityTest()#性能测试