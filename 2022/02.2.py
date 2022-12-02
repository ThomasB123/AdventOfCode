infile = open('02input.txt','r')
score = 0
scores = {'AX':3,'AY':4,'AZ':8,'BX':1,'BY':5,'BZ':9,'CX':2,'CY':6,'CZ':7}
for line in infile:
    score += scores[line[0]+line[2]]
print(score)
