
def createList(V,s):
    for i in range(0,V+1):
        s[i]=[]

def addEdge(x,y):
    s[x].append(y)
def BFS(s,node,queue,visited,dist,pred):
    visited[node]=1
    dist[node]=0
    queue.append(node)
    while(queue!=[]):
        v=queue.pop(0)
        for i in s[v]:
            if(visited[i]==0):
                visited[i]=1
                pred[i]=v
                dist[i]=dist[pred[i]]+1
                queue.append(i)
def SSSP(source,dest,path,pred):
    if(pred[dest]==-1):
        print(-1)
        return 0
    else:
        while(dest!=source):
            path.append(dest)
            dest=pred[dest]
        path.append(source)
        path=path.reverse()
        return 1

V=8 #No Of Vertices
s={}
createList(V,s)
queue=[]
visited=[0]*(V+1)
dist=[-1]*(V+1)
pred=[-1]*(V+1)
path=[]
addEdge(1,2) #Adding Edge
addEdge(2,4) #Adding Edge
addEdge(3,5) #Adding Edge
addEdge(3,4) #Adding Edge
addEdge(3,1) #Adding Edge
addEdge(4,3) #Adding Edge
addEdge(5,3) #Adding Edge
addEdge(4,7) #Adding Edge
addEdge(5,6) #Adding Edge
addEdge(6,7) #Adding Edge
BFS(s,1,queue,visited,dist,pred)
if(SSSP(1,5,path,pred)):
    for i in path:
        print(i,end=' ')
    print()

