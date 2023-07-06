#!/usr/bin/python3
"""
1-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box and
            contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    stack = [0]
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

