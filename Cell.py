class Cell:
    def __init__(self, i, j, w, c="#FFFFFF"):
        self.c = c
        self.i = i
        self.j = j
        self.w = w
    
    def show(self):
        fill(self.c)
        # noStroke()
        stroke('#383838')
        rect(self.i * self.w, self.j * self.w, self.w, self.w)
    
    def update_color(self, c):
        self.c = c
        
