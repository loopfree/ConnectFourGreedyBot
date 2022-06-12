class Player:
    """
    Class representation for Player

    [ATTRIBUTES]
        quota: dict -> piece shape quota owned by player
        shape: str -> shape representation for this player
        color: str -> color representation for this player
    """
    def __init__(self, color: str):
        self.color = color

    def __eq__(self, other):
        return other.color == self.color
