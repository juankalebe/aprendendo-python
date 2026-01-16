conj1 = {"Carlos", "Josiel","Jandira","Aline"}
conj2 = {"Aline","Carlos","Jaqueline","Altair"}

print(f"Pessoas presentes nos dois grupos: {conj1.intersection(conj2)}")
print(f"Pessoas presentes em apenas um grupo: {conj1.symmetric_difference(conj2)}")
print(f"Todas as pessoas: {conj1.union(conj2)}")