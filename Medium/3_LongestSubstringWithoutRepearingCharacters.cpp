#include <unordered_map>
#include <string>
#include <iostream>

class Solution {
public:
    std::unordered_map<char, int> map;
    int lengthOfLongestSubstring(std::string s) {
        map.clear();
        int left = 0,
            right = 0;
        int res = 0;
        size_t len = s.length();
        for (int i = 0; i < len; ++i) {
            if (map.contains(s[i])) {
                left = map[s[i]] + 1;
                map[s[i]] = i;

                // remove all values not in current range
                for (auto it = map.begin(); it != map.end();) {
                    if (it->second < left) {
                        it = map.erase(it);
                    }
                    else {
                        ++it;
                    }
                }
            }
            else {
                map.emplace(s[i], i);
            }
            right++;
            res = std::max(res, right - left);
        }
        return res;
    }
};

//int main() {
//    Solution* sol = new Solution();
//    std::cout << sol->lengthOfLongestSubstring("abcabcbb") << std::endl;
//    std::cout << sol->lengthOfLongestSubstring("bbbbb") << std::endl;
//    std::cout << sol->lengthOfLongestSubstring("pwwkew") << std::endl;
//    std::cout << sol->lengthOfLongestSubstring("dvdf") << std::endl;
//    std::cout << sol->lengthOfLongestSubstring("tmmzuxt") << std::endl;
//    std::cout << sol->lengthOfLongestSubstring("bbtablud") << std::endl;
//}