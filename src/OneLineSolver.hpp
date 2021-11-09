#ifndef _ONELINESOLVER_H
#define _ONELINESOLVER_H

#include <vector>

using namespace std;

typedef vector<vector<pair<int, int>>> Groups;

class OneLineSolver {
    public:
        OneLineSolver(int len);

        bool update_state();

    private:
        int len;
        int cache_cnt;
        vector<vector<int>> cache, calc_fill;
        vector<int> result_cell;

        int can_place_color(vector<int> cells, int color, int l, int r);
        void set_place_color(int color, int l, int r);
        int can_fill(vector<pair<int, int>> groups, vector<int> cells, int cur_group=0, int cur_cell=0);
};

#endif

