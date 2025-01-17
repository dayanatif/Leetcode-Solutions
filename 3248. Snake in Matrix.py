class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0,0

        for com in commands:
            if com == "UP":
                x -= 1
            elif com == "DOWN":
                x += 1
            elif com == "RIGHT":
                y += 1
            elif com == "LEFT":
                y -= 1
        return (x * n) + y
