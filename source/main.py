from sys import argv
from NetworkLoader import load_network


def main():
    path = argv[1]
    nw = load_network(path)
    nw.relabel_to_front()
    nw.print()

if __name__ == "__main__":
    main()
