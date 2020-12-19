import re


class Node:

    def __init__(self, no, rule, edges):
        self.no = no
        self.rule = rule
        self.edges = edges
        self.re_rule = None

    def __repr__(self):
        return str(self.no)


filename = 'input.txt'

V = []
visited = set()
no2node = dict()

with open(filename) as file:
    for line in file:
        if line == '\n':
            break
        rule_no, rule = line.strip().split(':')
        rule_no = int(rule_no)
        match_lst = re.findall(r'\d+', rule)
        edges = list({int(match) for match in match_lst})
        node = Node(rule_no, rule, edges)
        V.append(node)
        no2node[rule_no] = node

    message_lst = [line.strip() for line in file]


# Reverse topological sort
def visit(u):

    if u in visited:
        return

    for v_no in u.edges:
        v = no2node[v_no]
        visit(v)
    visited.add(u)
    order.insert(0, u)


order = []
for node in V:
    visit(node)

order.reverse()

#

for node in order:
    rule = node.rule
    if not node.edges:
        node.re_rule = re.match(r' "(\w)"', rule)[1]
    else:
        node.re_rule = rule

        node.edges.sort(reverse=True)

        for v_no in node.edges:
            v = no2node[v_no]

            node.re_rule = node.re_rule.replace(' {}'.format(v_no), '({})'.format(v.re_rule))
        node.re_rule = node.re_rule.replace(' ', '')


print(no2node[0].re_rule)

matcher = re.compile(no2node[0].re_rule)

count = 0
for message in message_lst:
    res = matcher.fullmatch(message)
    if res:
        count += 1
print(count)
