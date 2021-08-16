class QuizBrain:
    def __init__(self,ques_l):
        self.quesNum = 0
        self.questionList = ques_l
        self.score = 0

    def stillHasQuestion(self):
        return self.quesNum < len(self.questionList)

    def nextQuestion(self):
        self.currQues = self.questionList[self.quesNum]
        self.quesNum += 1
        self.userInput = input(f"Q.{self.quesNum} {self.currQues.text}(Ture/False)?")
#
    def isAnswerCorrect(self):
        if self.userInput == self.currQues.answer:
            print('Your answer is correct!')
            self.score += 1
        else:
            print('You are wrong.')
        print(f'{self.currQues.answer} is the correct answer.')
        print(f'your current score is : {self.score}/{self.quesNum}') 
