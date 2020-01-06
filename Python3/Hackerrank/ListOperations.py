if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        curr = input().split(' ')
        command = curr[0]

        if 'insert' == command:
            l.insert(int(curr[1]),int(curr[2]))
        
        elif 'print' == command:
            print(l)

        elif 'remove' == command:
            l.remove(int(curr[1]))

        elif 'append' == command:
            l.append(int(curr[1]))

        elif 'sort' == command:
            l.sort()

        elif 'pop' == command:
            l.remove(l[len(l)-1])

        elif 'reverse' == command:
            l = [ele for ele in reversed(l)]