# 알고리즘 #1: 왕실의 나이트
# vin/zik 2020/12/04

boardSize = 8
def checkPos (x, y):
    if x < 0 or x >= boardSize or y < 0 or y >= boardSize:
        return 0
    return 1

# LUT for available movement offsets
LUTBoardMovesets = [
    (-2, -1),
    (-2, -2),
    (-2, 1),
    (-2, 2),
    (2, -1),
    (2, -2),
    (2, 1),
    (2, 2),
    ]

# Get input & convert to simpler form
posInput = input()
pos = (ord(posInput[0]) - ord("a"), ord(posInput[1]) - ord("0") - 1)

# Calculate number of possible movements
numMoves = 0
for off in LUTBoardMovesets:
    numMoves += checkPos(pos[0] + off[0], pos[1] + off[1])

print(numMoves)
