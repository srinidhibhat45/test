from treelib import Tree;

Tree = Tree();

graph = {   '1' : ['2','3'],
            '2' : ['4','5','6'],
            '3' : ['7'],
            '4' : ['8'],
            '5' : ['9','10'],
            '6' : [],
            '7' : [],
            '8' : [],
            '9' : [],
            '10' : []
}

visited = set()

def dfs(graph,node,count,l,goal):
    Tree.show()
    if node not in visited:
        visited.add(node)
    if(node==goal):
        Tree.show()
        print("Node found")
        exit(0);
    if(count<l):
        for neighbour in graph[node]:
            count+=1
            Tree.create_node(neighbour,neighbour,parent=node)
            dfs(graph,neighbour,count,l,goal)

goal='9';
l=3;
Tree.create_node('1','1')
Tree.show()
dfs(graph,'1',0,l,goal)
if goal not in visited:
    print("Node not found")
