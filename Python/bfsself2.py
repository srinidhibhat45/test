from treelib import Tree

tree = Tree()

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

visited = []
queue = []

def bfs(graph,node,goal):
    queue.append(node)
    visited.append(node)
    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                tree.create_node(neighbour,neighbour,parent=m)
                visited.append(neighbour)
                queue.append(neighbour)
                if(neighbour==goal):
                    tree.show()
                    print("Node Found")
                    exit(0)
                tree.show()
tree.create_node('1','1')
tree.show()
bfs(graph,'1','7')
            