graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
start=input("Enter Source Node:")
des=input("Enter Destination Node:")
def dfs(g,start,li,des):
 
    if start not in li:
        li.append(start)
        for i in g[start]:
         if li[-1] is des:
            break
         dfs(g,i,li,des)
    return li
print(dfs(graph,start,[],des))
            
