"""isPrime_large"""
def main():
    """Code"""
    num = int(input())
    is_prime = True

    if num < 2:
        is_prime = False
    else:
        i = 2
        while i * i <= num:
            if not num % i:
                is_prime = False
                break
            i += 1

    if is_prime:
        print("YES")
    else:
        print("NO")

main()
