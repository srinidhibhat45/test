from treelib import Tree

tree =Tree()

graph = {
            '1' : ['2','3','4'],
            '2' : ['5','6'],
            '3' : ['7'],
            '4' : ['8','9'],
            '5' : [],
            '6' : [],
            '7' : ['10','11'],
            '8' : [],
            '9' : [],
            '10' : [],
            '11' : []
}

visited = set()

def dfs(graph,node,goal):
    if node not in visited:
        visited.add(node)
    if(node==goal):
        print("Node Found")
        exit(0)
    for neighbour in graph[node]:
        tree.create_node(neighbour,neighbour,parent=node)
        tree.show()
        dfs(graph,neighbour,goal)

tree.create_node('1','1')
tree.show()
dfs(graph,'1','7')