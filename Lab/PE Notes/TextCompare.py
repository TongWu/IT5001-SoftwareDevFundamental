

def compareDNA_I(dna1,dna2):
    dna_compare = ''
    for i in range(len(dna1)):
        if dna1[i] == dna2[i]:
            dna_compare += '*'
        else:
            dna_compare += '.'
    return dna_compare

def compareDNA_R(dna1,dna2):
    dna_compare = ''
    if not dna1:
        return ''
    if dna1[0] == dna2[0]:
        dna_compare = '*'
    else:
        dna_compare = '.'
    return dna_compare + compareDNA_R(dna1[1:], dna2[1:])


#You should not submit any test cases to Coursemology
#print(compareDNA_I('AGTCATATAC','ACTCATGTAA'))

print(compareDNA_R('AGTCATATAC','ACTCATGTAA'))