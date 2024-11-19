import pickle


def load_module():
    # unpickle header and tree in tree.p 
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile) # unpack tuple back into header and tree
    infile.close()
    return header, tree

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tdidt_predict(header, value_list[2], instance)

if __name__ == "__main__":
    header, tree = load_module()
    print(header)
    print(tree)