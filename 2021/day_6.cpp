
#include <queue>
#include <stdint.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <cmath>
#include "../include/infint.h"

#ifdef INFINT_H_
typedef InfInt fish_c_t;
#else
typedef uint64_t fish_c_t;
#endif

class Cache
{
protected:
    std::unordered_map<uint16_t, fish_c_t> m_cache;
    const uint16_t m_days;

public:
    Cache(const uint16_t& days) : m_days(days) {}

    int get_size() { return m_cache.size() * (sizeof(uint16_t) + sizeof(fish_c_t)); }

    fish_c_t calc(const uint16_t& num);
    fish_c_t get(const uint16_t& num)
    {
        auto it = m_cache.find(num);

        if (it != m_cache.end()) {
            return it->second;
        }

        fish_c_t tot = this->calc(num);
        m_cache.insert({num, tot});

        return tot;
    }

    fish_c_t get_shifted(const uint16_t& num)
    {
        return this->get(m_days + 6 - num);
    }
};

fish_c_t Cache::calc(const uint16_t& num)
{
    if (num < 7) return 0;

    uint16_t direct = num / 7;
    fish_c_t total = direct;

    for (uint16_t i = 0; i < direct; i++)
    {
        int16_t tmp = num - (7 * i + 9);

        if (tmp > 0) total += this->get(tmp);
    }

    return total;
}

int main(int argc, char** argv)
{
    std::vector<uint16_t> nums;
    std::ifstream ifs("input/day_6.txt");

    for (std::string line; std::getline(ifs, line, ',');)
    {
        nums.emplace_back(std::stoi(line));
    }

    int days = argc ? std::stoi(argv[1]) : 256;

    Cache cch(days);
    auto start = std::chrono::steady_clock::now();

    fish_c_t total = nums.size();

    for (auto n : nums)
    {
        total += cch.get_shifted(n);
    }

    auto tdiff = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now() - start);

    std::cout
    << total
    << std::endl
    << "Time elapsed "
    << tdiff.count()
    << "us, cache size at: "
    << cch.get_size() / pow(1024,1)
    << "KB"
    << std::endl;

    return 0;
}