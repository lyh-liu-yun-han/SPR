n = int(input("n = "))
boards = []
for w in range(n):
    a = [input()for w in range(8)]
    boards.append(a)
    now = []
for w in range(len(boards)):
    chessboard1 = boards[w]
    now.append(chessboard1)
    number = 0
    for j in range(len(now)):
        chessboard2 = now[j]
        if chessboard1 == chessboard2:
            number += 1 
    print(number)