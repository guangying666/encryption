

class DesEncode:
    def __int__(self):
        self.ip = [2, 6, 3, 1, 4, 8, 5, 7]  # 初始置换盒
        self.ip1 = [4, 1, 3, 5, 7, 2, 8, 5, 7]  # 最终置换盒

        self.EpBox = [4, 1, 2, 3, 2, 3, 4, 1]  # E扩展置换
        self.Sbox1 = [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 0, 2]
        ]  # 第一个S盒替代
        self.Sbox2 = [
            [0, 1, 2, 3],
            [2, 3, 1, 0],
            [3, 0, 1, 2],
            [2, 1, 0, 3]
        ]  # 第二个S盒替代
        self.SPbox = [2, 4, 3, 1]  # P盒置换

        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        self.LeftShiFt1 = [2, 3, 4, 5, 1]
        self.LeftShiFt2 = [3, 4, 5, 1, 2]
