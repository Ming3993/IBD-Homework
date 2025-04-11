import sys 
from itertools import combinations
from collections import defaultdict

# Đếm tần suất xuất hiện của từng 2-itemset
pair_counts = defaultdict(int)

# Đọc từng dòng từ STDIN
for line in sys.stdin:
    parts = line.strip().split("\t", 1) 
    if len(parts) < 2:
        continue  # Bỏ qua dòng không hợp lệ
    
    _, transaction = parts  
    words = transaction.split()

    for pair in combinations(words, 2):
        pair_counts[tuple(sorted(pair))] += 1  # Dùng frozenset để tránh trùng lặp theo thứ tự


for key, value in pair_counts.items():
    print(f"{' '.join(key)}\t{value}")