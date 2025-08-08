#include <bits/stdc++.h>

using namespace std;

// Possible colors
const vector<string> COLORS = {"Red", "Green", "Blue"};

// Adjacency map (region -> list of neighboring regions)
unordered_map<string, vector<string>> adjacency = {
    {"WA", {"NT", "SA"}},
    {"NT", {"WA", "SA", "Q"}},
    {"SA", {"WA", "NT", "Q", "NSW", "V"}},
    {"Q", {"NT", "SA", "NSW"}},
    {"NSW", {"Q", "SA", "V"}},
    {"V", {"SA", "NSW"}},
    {"T", {}}  // Tasmania has no neighbors
};

// Assignment map: region -> color
unordered_map<string, string> assignment;

// Check if current color assignment is valid for region
bool isValid(const string& region, const string& color) {
    for (const string& neighbor : adjacency[region]) {
        if (assignment.count(neighbor) && assignment[neighbor] == color) {
            return false;  // Neighbor has same color
        }
    }
    return true;
}

// Backtracking search to assign colors
bool backtrack(const vector<string>& regions, int index) {
    if (index == regions.size()) {
        return true;  // All regions assigned
    }

    string region = regions[index];

    for (const string& color : COLORS) {
        if (isValid(region, color)) {
            assignment[region] = color;

            if (backtrack(regions, index + 1)) {
                return true;
            }

            assignment.erase(region);  // Undo assignment (backtrack)
        }
    }

    return false;  // No valid color found for this region
}

int main() {
    vector<string> regions = {"WA", "NT", "SA", "Q", "NSW", "V", "T"};

    if (backtrack(regions, 0)) {
        cout << "Color assignment:" << endl;
        for (const auto& pair : assignment) {
            cout << pair.first << " -> " << pair.second << endl;
        }
    } else {
        cout << "No valid coloring found." << endl;
    }

    return 0;
}

