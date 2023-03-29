import math
def PI_Calculator(user_input):
    desired_answer=round(math.pi,user_input)
    calculation=0
    iterator=1
    while round(math.sqrt(calculation),user_input)!= round(math.pi,user_input):
        function=6/(iterator**2)
        calculation+=function
        iterator+=1
    Answer=round(math.sqrt(calculation),user_input)
    print(Answer)