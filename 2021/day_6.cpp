
#include <queue>
#include <stdint.h>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <chrono>
#include <unordered_map>
#include <cmath>

class Cache
{
protected:
    std::unordered_map<uint16_t, uint64_t> m_cache;
    const uint16_t m_days;

public:
    Cache(const uint16_t& days) : m_days(days) {}

    int get_size() { return m_cache.size() * (sizeof(uint16_t) + sizeof(uint64_t)); }

    uint64_t calc(const uint16_t& num);
    uint64_t get(const uint16_t& num)
    {
        auto it = m_cache.find(num);

        if (it != m_cache.end()) {
            return it->second;
        }

        uint64_t tot = this->calc(num);
        m_cache.insert({num, tot});

        return tot;
    }

    uint64_t get_shifted(const uint16_t& num)
    {
        return this->get(m_days + 6 - num);
    }
};

uint64_t Cache::calc(const uint16_t& num)
{
    if (num < 7) return 0;

    uint16_t direct = num / 7;
    uint64_t total = static_cast<uint64_t>(direct);

    for (uint16_t i = 0; i < direct; i++)
    {
        int16_t tmp = static_cast<int16_t>(num - (7 * i + 9));

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

    const int days = 256;

    Cache cch(days);
    auto start = std::chrono::system_clock::now();

    uint64_t total = nums.size();

    for (auto n : nums)
    {
        total += cch.get_shifted(n);
    }

    auto tdiff = std::chrono::system_clock::now() - start;

    std::cout
    << total
    << std::endl
    << "Time elapsed "
    << std::chrono::duration_cast<std::chrono::duration<double>>(tdiff).count()
    << "s, cache size at: "
    << cch.get_size() / pow(1024,1)
    << "KB"
    << std::endl;

    return 0;
}