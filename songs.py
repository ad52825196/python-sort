def main():
    k = int(input())
    separator = input()
    data = []
    try:
        while True:
            line = input().split(separator)
            data.append((line[0], line[1], line[2]))
    except EOFError:
        pass
    data = sorted(data, key = lambda line: line[1])
    data = sorted(data, key = lambda line: line[0])
    data = sorted(data, key = lambda line: -int(line[2]))
    for i in range(k):
        print(separator.join(data[i]))

main()
