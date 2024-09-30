class Node:
    def __init__(self, nbChildren, nbMetadata):
        self.nbChildren = nbChildren
        self.nbMetadata = nbMetadata
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, metadata):
        self.metadata.append(metadata)

    def __repr__(self):
        children = ("[\n   " + '\n   '.join([str(child) for child in self.children]) + "\n]") if self.children else "[]"
        return f"Node(metadata={self.metadata}, children={children}])"
    

def get_nodes(data):
    current_node = Node(data[0], data[1])
    if current_node.nbChildren == 0:
        current_node.metadata = data[2:2+current_node.nbMetadata]
        return [current_node, data[2+current_node.nbMetadata:]]
    
    else:
        left_data = data[2:]
        for _ in range(current_node.nbChildren):
            child, left_data = get_nodes(left_data)
            current_node.add_child(child)

        current_node.metadata = left_data[:current_node.nbMetadata]
        return [current_node, left_data[current_node.nbMetadata:]]
    

def count_metadata(node):
    return sum(node.metadata) + sum(count_metadata(child) for child in node.children)


def count_value(node):
    if node.children:
        value = 0
        for metadata in node.metadata:
            if (metadata > 0) and (metadata <= len(node.children)):
                value += count_value(node.children[metadata-1])
        return value
    else:
        return count_metadata(node)




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = list(map(int, [line.split() for line in open(f"2018/day8/{fichier}.txt", "r") if line.strip() != ""][0]))

    print("\033[93m--- Part One ---\033[0m")

    root_node, _ = get_nodes(data)
    totalSomme = count_metadata(root_node)

    print(f"Somme des métadonnées : {totalSomme}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    rootNodeValue = count_value(root_node)

    print(f"Valeur du root node : {rootNodeValue}")
    

