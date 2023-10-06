def seq_count(s1, s2):
    l_s1 = len(s1)
    l_s2 = len(s2)
    count = 0
    for i in range(l_s1-l_s2+1):
        seq1 = []
        seq2 = []
        for j in range(l_s2):
            seq1.append(s1[i+j])
            seq2.append(s2[j])
        if seq1 == seq2:
            count += 1
    return count

print(seq_count('ACTACTAG','ACTA'))