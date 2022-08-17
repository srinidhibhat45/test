from treelib import Tree;

tree = Tree();

graph={ '1' : ['2','3'],
        '2' : ['4','5'],
        '3' : [],
        '4' : [],
        '5' : ['6','7','8'],
        '6' : [],
        '7' : [],
        '8' : []
}

visited = []
queue = []

def bfs(graph,node,goal):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                tree.create_node(neighbour,neighbour,parent=m)
                visited.append(neighbour)
                queue.append(neighbour)
                tree.show()
                if(neighbour==goal):
                    exit(0);
tree.create_node('1','1')
bfs(graph,'1','8')