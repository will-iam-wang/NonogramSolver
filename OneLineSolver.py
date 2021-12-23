class OneLineSolver:
    def __init__(self, n):
        self.cache = [[0] * (n + 1) for _ in range(n + 1)]
        self.calc_fill = [[0] * (n + 1) for _ in range(n + 1)]
        self.cache_cnt = 0

        self.result_cell = [0] * n

    def update_state(self, groups, cells):
        self.cache_cnt += 1
        self.result_cell = [0] * len(cells)
        if not self.can_fill(groups, cells):
            return False
        for i in range(len(cells)):
            cells[i] = self.result_cell[i]
        return True

    @staticmethod
    def can_place_color(cells, clr, l, r):
        if r >= len(cells):
            return False
        mask = 1 << clr
        for i in range(l, r + 1):
            if (cells[i] & mask) == 0:
                return False
        return True

    def set_place_color(self, clr, l, r):
        for i in range(l, r + 1):
            self.result_cell[i] |= (1 << clr)

    def can_fill(self, groups, cells, cur_group=0, cur_cell=0):
        if cur_cell == len(cells):
            return cur_group == len(groups)
        cached = self.cache[cur_group][cur_cell]
        answer = self.calc_fill[cur_group][cur_cell]
        if cached == self.cache_cnt:
            return answer
        answer = 0
        if self.can_place_color(cells, 0, cur_cell, cur_cell) and self.can_fill(groups, cells, cur_group, cur_cell + 1):
            self.set_place_color(0, cur_cell, cur_cell)  # fill white
            answer = 1
        if cur_group < len(groups):
            cur_color = groups[cur_group][1]
            l = cur_cell
            r = cur_cell + groups[cur_group][0] - 1

            can_place = self.can_place_color(cells, cur_color, l, r)
            place_white = False

            next_cell = r + 1
            if can_place:
                if cur_group + 1 < len(groups) and groups[cur_group + 1][1] == cur_color:
                    place_white = True
                    can_place = self.can_place_color(cells, 0, next_cell, next_cell)
                    next_cell += 1
            if can_place:
                if self.can_fill(groups, cells, cur_group + 1, next_cell):
                    answer = 1
                    self.set_place_color(cur_color, l, r)
                    if place_white:
                        self.set_place_color(0, r + 1, r + 1)
        self.calc_fill[cur_group][cur_cell] = answer
        self.cache[cur_group][cur_cell] = self.cache_cnt
        return answer
