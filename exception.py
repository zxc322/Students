class GroupIsFull(Exception):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'This group already have 10 users!' + '\n' + "You can't add more students."
