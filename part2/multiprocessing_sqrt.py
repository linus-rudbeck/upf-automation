from multiprocessing import Pool
import math

def compute_sqrt(n):
    return math.sqrt(n)

numbers = [16, 25, 36, 49, 64]


def main():
    with Pool(4) as p:
        results = p.map(compute_sqrt, numbers)
    
    print(results)

if __name__ == "__main__":
    main()