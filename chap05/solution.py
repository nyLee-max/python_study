def solution(array, commands):
    answer = []
    for a, b, c in commands:
        answer += [sorted(array[a-1:b])[c-1]]
    return answer

def solution2(array, commands):
    return [sorted(array[a-1:b])[c-1] for a, b, c in commands]

if __name__ == "__main__":
    res = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [2, 7, 3]])
    print(type(res), res)
    print()# list [5, 6, 3]