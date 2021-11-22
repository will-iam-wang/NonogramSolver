#include <iostream>
#include <fstream>
#include <algorithm>

#include "OneLineSolver.hpp"
#include "NonogramReader.hpp"

using namespace std;

typedef vector<bool> Dead;
typedef vector<vector<int>> Mask;

bool update_state(OneLineSolver solver);

bool update_group_state(OneLineSolver solver, Dead d, Group g, Mask m) {
    for (int i = 0; i < g.size(); ++i) {
        if (!d[i]) {
            if (!solver.update_state(g[i], m[i]))
                return false;
            bool is_dead = true;
            for (int n: m[i]) {
                if (__builtin_popcount(n) != 1) {
                    is_dead = false;
                    break;
                }
            }
            d[i] = is_dead;
        }
    }
    return true;
}

int update_cell_value(Mask row, Mask col) {
    int ans = 0;
    for (int i = 0; i < row.size(); ++i) {
        for (int j = 0; j < col.size(); ++j) {
            row[i][j] &= col[i][j];
            col[j][i] &= row[i][j];
            ans += row[i][j];
        }
    }
    return ans;
}


int main(int argc, char *argv[]) {
    NonogramReader reader = NonogramReader(argv[2]);
    OneLineSolver solver;

    Group row_groups = reader.get_row_groups();
    Group col_groups = reader.get_col_groups();
    unordered_map<string, int> color_panel = reader.get_color_panel();

    int m = row_groups.size(), n = col_groups.size();
    int color_cnt = color_panel.size();
    solver = OneLineSolver(max(m, n));

    Dead dead_rows(m, false);
    Dead dead_cols(n, false);
    vector<Dead> painted(m, Dead(n, false));

    Mask row_masks(m, vector<int>(n, (1 << color_cnt) - 1));
    Mask col_masks(n, vector<int>(m, (1 << color_cnt) - 1));

    while (1) {

    }
    cout << "Done:)\n";
}
