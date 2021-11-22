#include <iostream>
#include <fstream>

#include "NonogramReader.hpp"

vector<int> splitByDelimiter(string str, char c) {
    vector<int> ans;
    string cur;

    cur = "";
    for (char x: str) {
        if (x == ' ') {
            ans.push_back(atoi(cur.c_str()));
            cur = "";
        } else {
            cur += x;
        }
    }
    return ans;
}

NonogramReader::NonogramReader(string id) {
    ifstream file;
    string line;
    int color_cnt, m, n;
    file.open("../puzzle/" + id + ".txt");
    if (!file) {
        cout << "Error: File not found\n";
        return;
    }
    getline(file, line);
    color_cnt = atoi(line.c_str());
    for (int i = 0; i < color_cnt + 1; ++i) {
        getline(file, line);
        if (line.size())
            color_panel[line] = i;
    }

    getline(file, line);
    int idx = line.find(" ");
    m = atoi(line.substr(0, idx).c_str());
    n = atoi(line.substr(idx + 1).c_str());

    getline(file, line);  // skip a empty line
    
    for (int i = 0; i < m; ++i) {
        getline(file, line);
        vector<int> temp = splitByDelimiter(line, ' ');
        vector<pair<int, int>> cur;
        for (int i = 0; i < temp.size(); i+=2) 
            cur.push_back({temp[i], temp[i + 1]});
        row_groups.push_back(cur);
    }

    getline(file, line); // skip a empty line

    for (int i = 0; i < n; ++i) {
        getline(file, line);
        vector<int> temp = splitByDelimiter(line, ' ');
        vector<pair<int, int>> cur;
        for (int i = 0; i < temp.size(); i+=2)
            cur.push_back({temp[i], temp[i + 1]});
        col_groups.push_back(cur);
    }

} 

Group NonogramReader::get_row_groups() {
    return row_groups;
}

Group NonogramReader::get_col_groups() {
    return col_groups;
}

unordered_map<string, int> NonogramReader::get_color_panel() {
    return color_panel;
}
