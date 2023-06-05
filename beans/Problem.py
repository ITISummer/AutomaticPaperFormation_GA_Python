# [Python 面向对象](https://www.runoob.com/python/python-object.html)
class Problem:
    """
    id 题目编号
    type 题型 （1、2、3、4、5对应单选，多选，判断，填空，问答）
    score 分数
    difficulty 难度系数
    points 知识点

    问题实体包含编号、类型（类型即题型，分为五种：单选，多选，判断，填空，问答， 分别用1、2、3、4、5表示）
    、分数、难度系数、知识点。
    一道题至少有一个知识点，为简单易懂，知识点用List<int> 表示（知识点编号集合）
    """

    def __init__(self, id, type, score, difficulty, points):
        self.id = id
        self.type = type
        self.score = score
        self.difficulty = difficulty
        self.points = points

    def __toStr__(self):
        return f"Problem(id={self.id}, type={self.type}, score={self.score}), difficulty={self.difficulty}, points={self.points}"
