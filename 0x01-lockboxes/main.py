#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[3]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1, 3], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1, 3], [3,5], [6], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
