import sys

def check(word, list):
    if word in list:
        return True
    else:
        return False

def find_machine(graph, contenu):
    l = contenu[0].split(' ')
    machine = int(l[0])
    for k in graph:
        if len(graph[k]) == 1 and graph[k][0] in graph and len(graph[graph[k][0]]) == machine - 2:
            print(k)


def find_nb(line, graph):
    l = line.split(' ')
    try:
        graph[l[0]].append(l[1])
    except:
        graph[l[0]] = []
        graph[l[0]].append(l[1])
    return graph

def main():
    contenu = sys.stdin.read().split('\n')
    graph = {}
    for i in contenu[1:]:
        graph = find_nb(i, graph)
    find_machine(graph, contenu)

if __name__ == "__main__":
    exit(main())