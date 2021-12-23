class PuzzleReader:
    def __init__(self, puzzle_id):
        linux_path = './puzzle/'
        # win_path = '.\\puzzle\\'
        with open(linux_path + puzzle_id + '.txt') as f:
            self.lines = f.read().split('-')
            
    def get_color_panel(self):
        color_panel = {}
        color_token = self.lines[0].strip().split('\n')
        for i, c in enumerate(color_token, start=1):
            color_panel[i] = c
        return color_panel
    
    def get_row_groups(self):
        row_groups = []
        row_groups_token = self.lines[1].strip().split('\n')
        for row in row_groups_token:
            cur = []
            for r in row.strip(',').split(','):
                temp = list(map(int, r.strip().split(':')))
                cur.append(temp)
            row_groups.append(cur)
        return row_groups
    
    def get_col_groups(self):
        col_groups = []
        col_groups_token = self.lines[2].strip().split('\n')
        for row in col_groups_token:
            cur = []
            for r in row.strip(',').split(','):
                temp = list(map(int, r.strip().split(':')))
                cur.append(temp)
            col_groups.append(cur)
        return col_groups
    
    
