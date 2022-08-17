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
        m = queue.pop()
        for neighbour in graph[m]:
            tree.create_node(neighbour,neighbour,parent=m)
            visited.append(neighbour)
            queue.append(neighbour)
            tree.show()
            if(neighbour==goal):
                print("Node Found")
                exit(0)

goal = '6'
tree.create_node('1','1')
tree.show()
bfs(graph,'1',goal)
if goal not in visited:
    print("Node not found")