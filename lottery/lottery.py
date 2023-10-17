import random

class Lottery:
    def __init__(self):
        self.list_reward = [
            "GTA VI"
            "Koenigsegg Trevita"
            "Nissan Nismo 370z"
            "Nissan GT-R"
            "Trip to Netherlands"
        ]

    def get_reward(self):
        random.randint(0, self.list_reward.len())
        return self.list_reward