# Source: https://datalemur.com/questions/python-same-stripes

# Title: Same Stripes


def is_same_stripes(matrix):
  reversed_m = matrix[::-1]

  n = len(matrix)
  m = len(matrix[0])

  for i in range(n * m // 2):
    first_value = None
    for j in range(0, n):
      key = i - j

      if 0 <= key < m:
        val = reversed_m[j][key]

        if first_value is None:
          first_value = val
        elif val != first_value:
          return False

  return True

