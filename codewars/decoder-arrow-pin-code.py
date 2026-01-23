# Source: https://www.codewars.com/kata/69178eb3a22411a3aab31347/train/python

# Title: decoder arrow pin code


def dec_arrow_pin_code(arrow_str):
    matrix, result = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [0]], []
    iX, iY = 0, 0

    for i, s in enumerate(arrow_str):
        if i == 0:
            result.append(int(s))
            for mx, m in enumerate(matrix):
                for ny, n in enumerate(m):
                    if matrix[mx][ny] == int(s):
                        iX = mx
                        iY = ny
            continue
        if s == '*':
            result.extend([result[len(result) - 1]] * (int(arrow_str[i + 1])))
        elif s in ['←', '→', '↓', '↑']:
            if s == '←':
                iY -= 1
            elif s == '→':
                iY += 1
            elif s == '↓':
                iX += 1
            elif s == '↑':
                iX -= 1

            if s != '↑' and result[len(result) - 1] == 0: return []
            if iY < 0 or iY > 2 or iX > 3 or iX < 0: return []
            if iX == 3 and iY > 0: return []

            result.append(matrix[iX][iY])

    return result