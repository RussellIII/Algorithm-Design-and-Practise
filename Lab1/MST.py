Edges_and_Weights = [(0,1,3),(0,2,9),(0,5,6),(1,2,9),(1,3,9),(1,4,2),(1,5,4),(2,3,8),(2,9,18),(3,4,8),(3,6,7),(3,8,9),(3,9,10),(4,5,2),(4,6,9),(5,6,9),(6,7,4),(6,8,5),(7,8,1),(7,9,4),(8,9,3)]
import random
import time
import pygame

def creat(N,M):
    G = []
    E_set = set()
    random.seed(time.process_time)
    for i in range(0,N-1):
        G.append((i, i + 1, random.randint(1,M)))
        E_set.add((i,i + 1))
        E_set.add((i + 1,i))
    i = 0
    while(i <= M-N):
        u = random.randint(0,N-1)
        v = random.randint(0,N-1)
        if(u != v and (u,v) not in E_set):
            G.append((u, v, random.randint(1,M)))
            E_set.add((u,v))
            E_set.add((v,u))
            i += 1        
    return G

def Kruskal(Edges_and_Weights, Num_of_Nodes):
	Nodes_and_Group = {}
	TotalWeight = 0
	EdgeSet = []
	Edges_and_Weights = sorted(Edges_and_Weights, key = lambda x: x[2])

	for i in range(0,Num_of_Nodes):
		Nodes_and_Group[i] = i

	for Edge_and_Weight in Edges_and_Weights:
		if find(Edge_and_Weight[0], Edge_and_Weight[1], Nodes_and_Group):
			#if 2 nodes are already connected
			EdgeSet.append((Edge_and_Weight[0], Edge_and_Weight[1]))#add this edge to MST
			TotalWeight += Edge_and_Weight[2]#add the weight to the MST
	return [EdgeSet,TotalWeight]

def find(i, j, Nodes_and_Group):
	wait_to_change = 0
	goal_of_change = 0

	if root_node(Nodes_and_Group,i) == root_node(Nodes_and_Group,j):
		#if node i and j are already connected:
		return False
	else:
		#change the group number to the smaller one
		if root_node(Nodes_and_Group,i) < root_node(Nodes_and_Group,j):
			Nodes_and_Group[root_node(Nodes_and_Group,j)] = root_node(Nodes_and_Group,i)
		else:
			Nodes_and_Group[root_node(Nodes_and_Group,i)] = root_node(Nodes_and_Group,j)

	return True
    

def root_node(Nodes_and_Group, i):
    if Nodes_and_Group[i] == i:
        return i
    else:
        return root_node(Nodes_and_Group, Nodes_and_Group[i])


def Prim(Edges_and_Weights, Num_of_Nodes):
	Nodes_in_MST = [0]
	EdgeSet = []
	TotalWeight = 0

	while len(EdgeSet) < Num_of_Nodes - 1:
		MinEdgeWeight = 65535
		for Edge_and_Weight in Edges_and_Weights:
			if ((Edge_and_Weight[0] not in Nodes_in_MST and Edge_and_Weight[1] in Nodes_in_MST) or\
						(Edge_and_Weight[0] in Nodes_in_MST and Edge_and_Weight[1] not in Nodes_in_MST) )and\
			Edge_and_Weight[2] < MinEdgeWeight:
				MinEdgeWeight = Edge_and_Weight[2]
				CandidatePair = (Edge_and_Weight[0], Edge_and_Weight[1])		
		EdgeSet.append(CandidatePair)
		TotalWeight += MinEdgeWeight
		if CandidatePair[0] not in Nodes_in_MST:
			#check which node not in Nodes_in_MST, and add this node into Nodes_in_MST
			Nodes_in_MST.append(CandidatePair[0])
		else:
			Nodes_in_MST.append(CandidatePair[1])
	return [EdgeSet,TotalWeight]

def CorrectnessTest():
	Result = []
	Result = Kruskal(Edges_and_Weights, 10)
	print("Kruskal Algorithm:")
	print('\tThe edges of the MST:', Result[0])
	print('\tSum of the weight of MST:', Result[1])
	Result = Prim(Edges_and_Weights, 10) 
	print("Kruskal Algorithm:")
	print('\tThe edges of the MST:', Result[0])
	print('\tSum of the weight of MST:', Result[1])

def AbilityTest():
	v_e = [(500,1000)]
	count = 0
	clock = pygame.time.Clock()
	for i in v_e:
		count += 1
		G = creat(i[0],i[1])
		print('Turn' , count )
		Edges_and_Weights_for_sort = G.copy()

		start_time = pygame.time.get_ticks()
		Kruskal(Edges_and_Weights_for_sort, i[0])
		Kruskal_time = pygame.time.get_ticks()-start_time
		Edges_and_Weights_for_sort = Edges_and_Weights.copy()

		start_time = pygame.time.get_ticks()
		Prim(Edges_and_Weights_for_sort, i[0]) 
		Prim_time = pygame.time.get_ticks()-start_time
		print('Time:\n\tKruskal:', Kruskal_time, "ms")
		print('Time:\n\tPrim:', Prim_time, "ms")

if __name__ == '__main__':
	CorrectnessTest()#正确性测试
	AbilityTest()#性能测试

