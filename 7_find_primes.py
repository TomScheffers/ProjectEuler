import time
start = time.time()

primes = [2,3]
blocks = [4,9]
search_range = 100

num = 5
while len(primes) < 10001:
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

print(time.time() - start)
print(primes[9999])
