filename = 'input.txt'


class Node:
    def __init__(self, name):
        self.name = name
        self.edge_lst = []  # edge is a tuple of (node, weight)
        self.parent_lst = []

    def add_node(self, node, weight):
        self.edge_lst.append((node, weight))
        node.parent_lst.append((self, weight))


rhs_set = set()
lhs_set = set()
name2node = dict()

with open(filename) as file:
    for line in file:
        line = line.strip()
        lhs, rest = line.split(' contain ')

        if rest == 'no other bags.':
            continue

        lhs_set.add(lhs)
        if lhs not in name2node:
            name2node[lhs] = Node(lhs)

        lhs_node = name2node[lhs]

        rest = rest[:-1].split(', ')
        for bag_info in rest:
            count, rhs = bag_info.split(maxsplit=1)
            count = int(count)

            if count == 1:
                rhs = rhs + 's'

            rhs_set.add(rhs)
            if rhs not in name2node:
                name2node[rhs] = Node(rhs)

            rhs_node = name2node[rhs]
            lhs_node.add_node(rhs_node, count)


root_set = lhs_set - rhs_set


lookup = dict()  # name to count of bags it must contain


def find_count_bags(name):

    if name in lookup:
        return lookup[name]

    node = name2node[name]

    total = 0

    for child_node, child_weight in node.edge_lst:
        total += (find_count_bags(child_node.name) + 1) * child_weight

    lookup[name] = total
    return total


result = find_count_bags('shiny gold bags')
print(result)

print(lookup)