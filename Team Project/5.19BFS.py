from queue import Queue

MAZE_SIZE = 6

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def BFS():
    que = Queue()
    que.put((0, 1))  
    print('BFS: ')

    while not que.empty():
        here = que.get()
        print(here, end='->')
        x, y = here

        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.put((x, y - 1))
            if isValidPos(x, y + 1): que.put((x, y + 1))
            if isValidPos(x - 1, y): que.put((x - 1, y))
            if isValidPos(x + 1, y): que.put((x + 1, y))

    return False


result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
