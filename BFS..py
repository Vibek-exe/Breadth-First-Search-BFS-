graph = { 1:[2,3],
          2:[1,4,7,5],
          3:[1,6,4],
          4:[2,3,5],
          5:[2,4],
          6:[3,7],
          7:[6,2]
        }
    
visited = []
queue = []

def BFS(node,visited,graph):   #BFS fuction
    
    if node not in graph:   #Checking input is present in graph or not
        return print("Node is not present")
    
    visited.append(node)           #add 1st node into queue and make it visited 
    queue.append(node)
    
    while queue:                   #Create loop to visited each node
        m = queue.pop(0)
        print(m,end=" ")
        
        for i in graph[m]:         # i in graph[m] will give value of adjacent i.e {1 :[2,3]} it give 2,3 for 1
            if i not in visited:
                visited.append(i)
                queue.append(i)
                
                
node = int(input("Enter first node: "))    #input starting node
BFS(node,visited,graph)