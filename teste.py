class sprite(object):
    def __init__(self, y, x):
        self.sprite = x + y

x = sprite(10, 10)

print(x.sprite)