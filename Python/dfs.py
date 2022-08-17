from treelib import Tree;
Tree = Tree()
graph={ '1' : ['2','3'],
        '2' : ['4','5'],
        '3' : [],
        '4' : [],
        '5' : ['6','7','8'],
        '6' : [],
        '7' : [],
        '8' : []
}

visited = set();

def dfs(graph,node,goal):
    if node not in visited:
        visited.add(node)
        if(node == goal):
            exit(0);
        for neighbour in graph[node]:
            Tree.create_node(neighbour,neighbour,parent=node)
            Tree.show()
            dfs(graph,neighbour,goal)
Tree.create_node('1','1')
Tree.show()
dfs(graph,'1','6')