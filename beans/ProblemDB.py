import random

from Problem import Problem


class ProblemDB:
    """
    为了简单，这里没有用数据库，题目信息临时创建，保存在内存中。
    因为对不同层次的考生一道题目在不同试卷中的分数可能不一样，
    因此题目分数一般是老师出卷时定的，不保存在题库中。
    且单选，多选，判断题每题分数应该相同，填空题一般根据空数来定分数，而问答题一般根据题目难度来定的，
    因此这里的单选、多选、判断分数相同，填空空数取1-4间的随机数，填空题分数即为空数，
    问答题即为该题难度系数*10取整。这里各种题型均为1000题，具体应用时改为数据库即可。
    """
    problemDB = list()

    def __init__(self):
        for i in range(10):
            model = Problem(0, 0, 0, 0.0, list())
            model.id = i
            model.difficulty = random.randint(30, 100) * 0.01
            # 单选题 -> 1分
            if i < 1001:
                model.type = 1
                model.score = 1

            # 单选题 -> 2分
            if i > 1000 and i < 2001:
                model.type = 2
                model.score = 2

            # 判断题 -> 2分
            if i > 2000 and i < 3001:
                model.type = 3
                model.score = 3

            # 填空题 -> 1-4分
            if i > 3000 and i < 4001:
                model.type = 4
                model.score = random.randint(1, 5)

            # 问答题分数为难度系数*10
            if i > 4000 and i < 5001:
                model.type = 5
                model.score = 3 if model.difficulty < 0.3 else int(float(model.difficulty)) * 10
            # 每题1到4个知识点
            count = random.randint(1, 5)
            for i in range(count):
                model.points.append(random.randint(1, 100))
                ProblemDB.problemDB.append(model)


def printDB():
    """
    打印题库
    """
    ProblemDB()
    for item in ProblemDB.problemDB:
        print(item.__toStr__())

printDB()