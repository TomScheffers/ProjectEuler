import itertools

def get_primes(range):
    primes = [2, 3]
    blocks = [4, 9]
    num = 5
    while num < range:
        if num in blocks:
            idx = blocks.index(num)
            prime = primes[idx]
            new_block = num + 2 * prime
            while new_block in blocks:
                new_block += 2 * prime
            blocks[idx] = new_block
        else:
            primes.append(num)
            blocks.append(num ** 2)

        #print(num, primes, blocks) #dit moet je uit commenten als je grote getallen gaat zoeken

        if num % 100000 == 0:
            print("Found ", len(primes), " until number: ", num)

        num += 2
    return primes

def rotations(value): #deze functie returnt alle permutaties
    digits = [d for d in str(value)]
    N = len(digits)
    rotations = [value]
    for n in range(1,N):
        digits.append(digits[0])
        digits = digits[1:]
        rotations.append(int("".join(digits)))
    return rotations

primes = get_primes(1000000)
steps = 3
min_val = 0
max_val = 10

circular_primes = []

for s in range(steps):
    print("Looking in range: ", min_val, max_val) #alle circular primes hebben evenveel getallen
    prime_range = [x for x in primes if x < max_val and x > min_val] #filter de primes op deze values

    if s == 0:
        [circular_primes.append(x) for x in prime_range]
    else:
        while len(prime_range) > 0:
            rots = rotations(prime_range[0])
            rots_dist = list(set(rots)) #dit is een trucje... sets zijn namelijk uniek.
            circular = [i for i in rots_dist if i in prime_range] #check of ze in beide lijsten voorkomen

            if len(circular) != len(rots_dist):
                prime_range.remove(prime_range[0])
            else:
                [circular_primes.append(i) for i in circular]
                [prime_range.remove(i) for i in circular] #permutaties hoeven we niet dubbel te checken.

    min_val = max_val
    max_val = 10 * max_val

print(circular_primes)
