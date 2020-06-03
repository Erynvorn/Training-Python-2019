from itertools import count, islice

sum(islice((x for x in count() if is_prime(x)),100))
