infile = open('02input.txt','r')
score = 0
scores = {'AX':4,'AY':8,'AZ':3,'BX':1,'BY':5,'BZ':9,'CX':7,'CY':2,'CZ':6}
for line in infile:
    score += scores[line[0]+line[2]]
print(score)
