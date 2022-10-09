import collections
def bfs(graph,root):
    seen,queue = set([root]),collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in  seen:
                seen.add(node)
                queue.append(node)

#all path
def allpath(st,end,gr):
    todo=[(st,[st])]
    while len(todo):
        node,path=todo.pop(0)
        for next_node in gr[node]:
            if next_node in path:
                continue
                print("Ideal solution")
            elif next_node==end:
                yield path + [next_node]

            else:
                todo.append((next_node,path + [next_node]))

def visit(n):
    print(n)

def bfs_shortest_path(graph,source,destination):
    checked = []
    queue =[[source]]
    if source == destination:
        return "SOURCE IS DESTINATION : "
    while queue:
        path = queue.pop(0)
        node= path[-1]
        if node not in checked:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:
                    return new_path
            checked.append(node)
    return "PATH DOESNOT EXISTS : "

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


print("Graph traversal:")
bfs(graph,'5')
print("\n\n All paths are: ")
[print (x) for x in allpath('5','4',graph)]
print ("\n SHORTEST PATH OF GRAPH IS: ",bfs_shortest_path(graph,'5','4'))
