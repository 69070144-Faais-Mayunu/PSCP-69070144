"""Ink"""
import math
def main():
    """code"""
    S, N = map(int,input().split())
    for i in range(N):
        X, Y = map(int,input().split())
        R = X ** 2 + Y ** 2
        print(math.ceil((3.1416 * R)/S))
        i += 1
main()
