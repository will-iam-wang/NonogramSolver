#ifndef _NONOGRAMREADER_H
#define _NONOGRAMREADER_H

#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

typedef vector<vector<pair<int, int>>> Group;

class NonogramReader {
    public: 
        NonogramReader(string id);
        unordered_map<string, int> get_color_panel();
        Group get_row_groups();
        Group get_col_groups();

    private:
		unordered_map<string, int> color_panel;
		Group row_groups, col_groups;
};

#endif

