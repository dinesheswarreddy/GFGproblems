#Flood fill Algorithm
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != originalColor:
                return
            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image


def printImage(img):
    for row in img:
        print(' '.join(map(str, row)))


def userInputMode():
    n = int(input("Enter number of rows: "))
    m = int(input("Enter number of columns: "))
    print("Enter the image row by row (space-separated):")
    image = [list(map(int, input().split())) for _ in range(n)]

    sr = int(input("Enter starting row (sr): "))
    sc = int(input("Enter starting column (sc): "))
    newColor = int(input("Enter new color: "))

    sol = Solution()
    result = sol.floodFill(image, sr, sc, newColor)

    print("\nFlood-filled image:")
    printImage(result)


def builtInExample():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc = 1, 1
    newColor = 2

    print("Original image:")
    printImage(image)

    sol = Solution()
    result = sol.floodFill(image, sr, sc, newColor)

    print("\nFlood-filled image:")
    printImage(result)


if __name__ == "__main__":
    print("Choose mode:")
    print("1. User Input")
    print("2. Built-in Example")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        userInputMode()
    else:
        builtInExample()
