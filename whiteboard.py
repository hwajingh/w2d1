# given a random number, return fizz if even and buzz if odd

def rando(num):
    if num % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"

print(rando(6))

print(rando(5))
print(rando("bd"))