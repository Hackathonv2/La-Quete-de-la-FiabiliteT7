import sys


def find_nb(line):
    l = line.split(' ')
    rst = int(l[1]) * (int(l[2]) + int(l[3]))

    return (l[0], rst)

def main():
    contenu = sys.stdin.read().split('\n')
    output = []
    for i in contenu:
        output.append(find_nb(i))
    if output[0][1] < output[1][1]:
        print(output[0][0])
    else:
        print(output[1][0])

if __name__ == "__main__":
    exit(main())