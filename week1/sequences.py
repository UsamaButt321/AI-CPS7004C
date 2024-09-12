def find_distance(sequence, marker):

    indices = [i for i, char in enumerate(sequence) if char == marker]


    distances = []
    for i in range(len(indices) - 1):
        distances.append(indices[i + 1] - indices[i] - 1)


    return tuple(distances)


sequence = "----x----x----"
marker = "x"
distances = find_distance(sequence, marker)
print(distances)