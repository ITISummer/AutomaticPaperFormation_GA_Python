class Paper:
    """
    试卷一般包含试卷编号，试卷名称，考试时间，难度系数，知识点分布，总题数， 总分数，各种题型所占比率等属性，
    这里为简单去掉了试卷名称跟考试时间。其中的知识点分布即老师出卷时选定本试卷要考查的知识点，
    这里用List<int>（知识点编号集合）表示。
    """
    problemDB = list()

    def __init__(self, id, totalScore, difficulty, points, eachTypeCount):
        # 编号
        self.id = id
        # 总分
        self.totalScore = totalScore,
        # 难度系数
        self.difficulty = difficulty,
        # 知识点
        self.points = points,
        # 各种题型题数
        self.eachTypeCount = eachTypeCount
