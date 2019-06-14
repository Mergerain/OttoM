#The is an outline of the "BFS grouping"
def printcluster(graph):
    ds = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph))]
    cluster = {}
    count=0
    for i in range(len(graph)):
        #if count == 2: if the number of island is known
            #break
        for j in range(len(graph[0])):
            if visited[i][j] == 0 and graph[i][j] == 'B':
                count+=1
                cluster[count] = [[i,j]]
                queue=[[i,j]]
                visited[i][j] = 1
                while queue:
                    row,col = queue[0][0],queue[0][1]
                    queue.pop(0)
                    for d in ds:
                        newrow = row+d[0]
                        newcol = col+d[1]
                        if newrow>=0 and newrow<len(graph) and newcol>=0 and newcol<len(graph[0]):
                            if graph[newrow][newcol] == 'B' and visited[newrow][newcol] ==0:
                                cluster[count].append([newrow,newcol])
                                queue.append([newrow,newcol])
                                visited[newrow][newcol] = 1
                #if count == 2: if the number of island is known
                    #break
    return cluster 

