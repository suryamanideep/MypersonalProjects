def calculate_cost_and_hamming_distance(binary_string, A, B):
    count_0 = binary_string.count('0')
    count_1 = binary_string.count('1')
    
    # Calculate the cost of the original string
    cost_original = 0
    for i in range(len(binary_string) - 1):
        if binary_string[i:i+2] == '01':
            cost_original += A
        elif binary_string[i:i+2] == '10':
            cost_original += B
    
    # Possible rearrangements
    # 1. All zeros followed by all ones
    rearrangement_1 = '0' * count_0 + '1' * count_1  # "000...111"
    # Hamming distance from original to rearrangement 1
    hamming_distance_01 = sum(1 for i in range(len(binary_string)) if binary_string[i] != rearrangement_1[i])
    cost_01 = 0  # There will be no "01" or "10" pairs

    # 2. All ones followed by all zeros
    rearrangement_2 = '1' * count_1 + '0' * count_0  # "111...000"
    # Hamming distance from original to rearrangement 2
    hamming_distance_10 = sum(1 for i in range(len(binary_string)) if binary_string[i] != rearrangement_2[i])
    cost_10 = 0  # There will be no "01" or "10" pairs

    # Choose the arrangement with minimum cost, then minimum hamming distance
    if cost_01 < cost_10:
        return hamming_distance_01
    elif cost_10 < cost_01:
        return hamming_distance_10
    else:  # costs are equal, choose minimum hamming distance
        return min(hamming_distance_01, hamming_distance_10)

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        binary_string = input().strip()
        costs = input().strip().split()
        
        # Validate binary string
        if not all(c in '01' for c in binary_string):
            results.append("INVALID")
            continue
        
        try:
            A = int(costs[0])
            B = int(costs[1])
        except ValueError:
            results.append("INVALID")
            continue
        
        hamming_distance = calculate_cost_and_hamming_distance(binary_string, A, B)
        results.append(str(hamming_distance))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
