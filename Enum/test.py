from enum import Enum, unique
import random



# 扑克牌花色
@unique
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
    # 小于
    def __lt__(self, other):
        return self.value < other.value
    
    @staticmethod
    def test():
        print(Suite.SPADE)
        print(Suite.SPADE.name)
        print(Suite.SPADE.value)        




if __name__ == '__main__':
    Suite.test()