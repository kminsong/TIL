while True:
    try:
        N, M = map(int, input().split())
        answer = M // (N+1)
        print(answer)
    except EOFError:
        break