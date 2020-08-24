GraphMatrix = [[0, 3, 9, 0, 0, 6, 0, 0, 0, 0],
			   [0, 0, 9, 9, 2, 4, 0, 0, 0, 0],
			   [0, 0, 0, 8, 0, 0, 0, 0, 0,18],
			   [0, 0, 0, 0, 8, 0, 7, 0, 9,10],
			   [0, 0, 0, 0, 0, 2, 9, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 4, 5, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 1, 4],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def Kruskal(GraphMatrix, Num_of_Nodes):
	Nodes_and_Group = {}
	TotalWeight = 0
	EdgeSet = []
	for i in range(0,Num_of_Nodes):
		Nodes_and_Group[i] = i
	# print(Nodes_and_Group)
	while Nodes_in_Same_group(Nodes_and_Group, Num_of_Nodes):
		MinEdgeWeight = 65535
		for i in range(0,Num_of_Nodes):# i是行号
			for j in range(i,Num_of_Nodes):#j是列号
				if GraphMatrix[i][j] != 0 and GraphMatrix[i][j] < MinEdgeWeight:
					#if we find the current minimum edge weight
					MinEdgeWeight = GraphMatrix[i][j]#record the possible weight
					CandidatePair = (i, j)#record two nodes
		if find(CandidatePair[0], CandidatePair[1], Nodes_and_Group, Num_of_Nodes):
			#if 2 nodes are already connected
			EdgeSet.append(CandidatePair)#add this edge to MST
			TotalWeight += MinEdgeWeight#add the weight to the MST
			GraphMatrix[CandidatePair[0]][CandidatePair[1]] = 0
			#clean the weight to avoid being find as the min-weight edge again
		else:
			GraphMatrix[CandidatePair[0]][CandidatePair[1]] = 0
	print("Kruskal Algorithm:")
	print('\tThe edges of the MST:', EdgeSet)
	print('\tSum of the weight of MST:', TotalWeight)

def find(i, j, Nodes_and_Group, Num_of_Nodes):
	wait_to_change = 0
	goal_of_change = 0

	if Nodes_and_Group[i] == Nodes_and_Group[j]:
		#if node i and j are already connected:
		return False
	else:
		#change the group number to the smaller one
		if Nodes_and_Group[i] < Nodes_and_Group[j]:
			wait_to_change = Nodes_and_Group[j]
			goal_of_change = Nodes_and_Group[i]
			Nodes_and_Group[j] = Nodes_and_Group[i]
		else:
			wait_to_change = Nodes_and_Group[i]
			goal_of_change = Nodes_and_Group[j]
			Nodes_and_Group[j] = Nodes_and_Group[i]

	for k in range(0, Num_of_Nodes):
		#arrange other nodes in the bigger group number to smaller one
		if Nodes_and_Group[k] == wait_to_change:
			Nodes_and_Group[k] = goal_of_change
	return True

def Nodes_in_Same_group(Nodes_and_Group, Num_of_Nodes):
	for i in range(0, Num_of_Nodes):
		if Nodes_and_Group[i] != 0:
			#if nodes aren't in the same group
			return True
	return False

def Prim(GraphMatrix, Num_of_Nodes):
	Nodes_in_MST = [0]
	EdgeSet = []
	TotalWeight = 0

	while len(EdgeSet) < Num_of_Nodes - 1:
		MinEdgeWeight = 65535
		for i in Nodes_in_MST:
			for j in range(i,Num_of_Nodes):
				#search edges that at least have one node in Nodes_in_MST
				if GraphMatrix[i][j] != 0 and GraphMatrix[i][j] < MinEdgeWeight:
					MinEdgeWeight = GraphMatrix[i][j]#record the possible weight
					CandidatePair = (i, j)#record two nodes
		for j in Nodes_in_MST:
			for i in range(0,j):
				# print(i, j,GraphMatrix[i][j])
				if GraphMatrix[i][j] != 0 and GraphMatrix[i][j] < MinEdgeWeight:
					MinEdgeWeight = GraphMatrix[i][j]#record the possible weight
					CandidatePair = (i, j)#record two nodes
		if (CandidatePair[1] not in Nodes_in_MST and CandidatePair[0]  in Nodes_in_MST) or\
		(CandidatePair[0] not in Nodes_in_MST and CandidatePair[1] in Nodes_in_MST):
			#only when one node not in the Nodes_in_MST, can this edge be accepted.
			EdgeSet.append(CandidatePair)#add this edge to MST
			TotalWeight += MinEdgeWeight#add the weight to the MST
			GraphMatrix[CandidatePair[0]][CandidatePair[1]] = 0
			#clean the weight to avoid being find as the min-weight edge again
			if CandidatePair[0] not in Nodes_in_MST:
				#check which node not in Nodes_in_MST, and add this node into Nodes_in_MST
				Nodes_in_MST.append(CandidatePair[0])
			else:
				Nodes_in_MST.append(CandidatePair[1])
			# print(Nodes_in_MST)
		else:
			GraphMatrix[CandidatePair[0]][CandidatePair[1]] = 0
	print("Prim Algorithm:")
	print('\tThe edges of the MST:', EdgeSet)
	print('\tSum of the weight of MST:', TotalWeight)




if __name__ == '__main__':
	GraphMatrix_for_Run = [row[:] for row in GraphMatrix]
	Kruskal(GraphMatrix_for_Run, 10)
	GraphMatrix_for_Run = [row[:] for row in GraphMatrix]
	Prim(GraphMatrix_for_Run, 10) 