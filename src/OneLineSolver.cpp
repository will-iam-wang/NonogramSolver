#include <iostream>
#include "OneLineSolver.hpp"

using namespace std;


OneLineSolver::OneLineSolver(int len_) {
    len = len_;
    cache_cnt = 0;
    cache.resize(len, vector<int>(len, 0));
    calc_fill.resize(len, vector<int>(len, 0));
    result_cell.resize(len, 0);
}

int OneLineSolver::can_place_color(vector<int> cells, int color, int l, int r) {
    if (r >= cells.size()) 
        return false;
    int mask = 1 << color;
    for (int i = l; i <= r; ++i) 
        if (!(cells[i] & mask))
            return false;
    return true;
}

void OneLineSolver::set_place_color(int color, int l, int r) {
    for (int i = l; i <= r; ++i) {
        result_cell[i] |= (1 << color);
    }
}

int OneLineSolver::can_fill(vector<pair<int, int>> groups, vector<int> cells, int cur_group, int cur_cell) {
    if (cur_cell == cells.size()) 
        return cur_group == groups.size();
    int cached = cache[cur_group][cur_cell];
    int answer = calc_fill[cur_group][cur_cell];
    if (cached == cache_cnt)
        return answer;
    answer = 0;
    if (can_place_color(cells, 0, cur_cell, cur_cell) && can_fill(groups, cells, cur_group, cur_cell + 1)) {
        set_place_color(0, cur_cell, cur_cell);
        answer = 1;
    }
    if (cur_group < groups.size()) {
        int cur_color = groups[cur_group].second;
        int l = cur_cell, r = cur_cell + groups[cur_group].first - 1;
        bool ok_place = can_place_color(cells, cur_color, l, r);
        bool ok_white = false;

        int next_cell = r + 1;
        if (ok_place) {
            if (cur_group + 1 < groups.size() && groups[cur_group].second == cur_color) {
                ok_white = true;
                ok_place = can_place_color(cells, 0, next_cell, next_cell);
                next_cell++;
            }
        }
        if (ok_place) {
            if (can_fill(groups, cells, cur_group + 1, next_cell)) {
                answer = 1;
                set_place_color(cur_color, l, r);
                if (ok_white) 
                    set_place_color(0, r + 1, r + 1);
            }
        }
    }
    calc_fill[cur_group][cur_cell] = answer;
    cache[cur_group][cur_cell] = cache_cnt;
    return answer;
}
