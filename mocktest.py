q1 = """Which planet is known as blue planet?
a.earth
b.mumbai
c.chennai
d.bombay"""

q2 = """which one of our is our galaxy?
a.milky way
b.earth
c.mercury
d.venus"""

q3 = """which is the hottest planet in our solar system?
a.earth
b.venus
c.mercury
d.none"""

q4 = """which is the brightest planet?
a.earth
b.venus
c.mercury
d.none"""



questions={q1:"a",q2:"a",q3:"b",q4:"b"}
score=0
name=input("enter your name:")
print("hello",name,"welcome to our mock test")

for i in questions:
    print()
    print(i)
    
    ans=input("enter the answer (a/b/c/d):")
    if ans==questions[i]:
        print("correct answer ,you have scored 1 point")
        score=score+1
        print("current score is :",score)
    else:
        print("wrong answer ,you have lost 1 point")
        score=score-1
        print("current score is :",score)
print("final score is :",score)
