# 코드 5.9
import queue

def isValidPos(x, y) :
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

# BFS(너비 우선 탐색, Breadth-First Search) : queue.Queue()
def BFS():
    que = queue.Queue()
    que.put((0,1))
    print('BFS: ')

    while not que.empty():
        here = que.get()
        print(here, end='->')
        x, y = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.put((x, y - 1))   # 상
            if isValidPos(x + 1, y): que.put((x + 1, y))   # 우
            if isValidPos(x, y + 1): que.put((x, y + 1))   # 하
            if isValidPos(x - 1, y): que.put((x - 1, y))   # 좌
        print(' 현재 큐  : ', list(que.queue))
    return False

# DFS(깊이 우선 탐색, Depth-First Search) : queue.LifoQueue()
def DFS():
    stack = queue.LifoQueue()
    stack.put((0,1))
    print('DFS: ')

    while not stack.empty():
        here = stack.get()
        print(here, end='->')
        x, y = here
        if map[y][x] == 'x':
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): stack.put((x, y - 1))   # 상
            if isValidPos(x + 1, y): stack.put((x + 1, y))   # 우
            if isValidPos(x, y + 1): stack.put((x, y + 1))   # 하
            if isValidPos(x - 1, y): stack.put((x - 1, y))   # 좌
        print(' 현재 스택  : ', list(stack.queue))
    return False
#--------------------------------------------------------------------------------------------------------

# BFS(너비우선 탐색) 출력
map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]
MAZE_SIZE = 6

result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

# DFS(깊이우선 탐색) 출력
map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]
result = DFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

