
#include <vector>
#include <fstream>
#include <string>
#include <iostream>
#include <chrono>
#include <utility>
#include <functional>

#define BITCOUNT 12

int calc(int* input, int sz, bool most)
{
    std::vector<int> inp(input, input + sz);
    int shift = BITCOUNT - 1;

    while (inp.size() > 1 && shift >= 0)
    {
        std::vector<int> zeros;
        std::vector<int> ones;

        for (auto i : inp)
        {
            if (i & (1 << shift)) ones.push_back(i);
            else zeros.push_back(i);
        }

        shift--;

        if (most)
        {
            inp = std::move((ones.size() >= zeros.size()) ? ones : zeros);
        }
        else
        {
            inp = std::move((ones.size() < zeros.size()) ? ones : zeros);
        }
    }

    return inp[0];
}

int puzzle_2(int* input, int sz)
{
    return (calc(input, sz, true) * calc(input, sz, false));
}


/*
Note: I dont know how the python counter object works, but im assuming
this is something similar
*/
std::pair<int, int> counter(const std::vector<std::string>& vec, int idx)
{
    int z = 0;
    int o = 0;

    for (auto s : vec)
    {
        if (s[idx] == '1') o += 1;
        else z += 1;
    }

    return std::make_pair(z, o);
}

std::vector<std::string> filter(const std::vector<std::string>& input, char delim, int idx)
{
    std::vector<std::string> n;

    for (auto i : input)
    {
        if (i[idx] == delim) n.push_back(i);
    }

    return n;
}

/*
Implementation of puzzle_4 (from the python file, see 2021/day_3.py)
*/
int puzzle_4(std::string* input, int sz)
{
    std::vector<std::string> inp(input, input + sz);

    std::string theta;
    std::string epsilon;

    std::vector<std::string> ll = inp;
    for (int i = 0; i < BITCOUNT; i++)
    {
        auto count = counter(ll, i);

        if (count.first > count.second) ll = filter(ll, '0', i);
        else ll = filter(ll, '1', i);

        theta = ll[0];
    }

    ll = inp;
    for (int i = 0; i < BITCOUNT; i++)
    {
        auto count = counter(ll, i);

        if (count.first > count.second) ll = filter(ll, '1', i);
        else ll = filter(ll, '0', i);

        if (ll.size()) epsilon = ll[0];
    }

    return (std::stoi(theta, nullptr, 2) * std::stoi(epsilon, nullptr, 2));
}

template<typename T>
std::pair<int, double> run(T input, std::function<int(T, int)> func, int sz, int times)
{
    int result;
    auto start = std::chrono::system_clock::now();

    for (int i = 0; i < times; i++)
        result = func(input, sz);
    
    auto end = std::chrono::system_clock::now();
    auto t = std::chrono::duration_cast<std::chrono::duration<double>>(end - start).count();

    return std::make_pair(result, t);
}

int main(int argc, char** argv)
{
    int input[1000];
    std::string lines[1000];

    std::ifstream ifs("input/day_3.txt");
    std::string line;

    for (int i = 0; std::getline(ifs, line); i++)
    {
        input[i] = std::stoi(line, nullptr, 2);
        lines[i] = line;
    }

    // int result;
    // auto start = std::chrono::system_clock::now();

    // for (int i = 0; i < 1000; i++)
    //     result = puzzle_2(input, 1000);
    
    // auto end = std::chrono::system_clock::now();
    // auto t = std::chrono::duration_cast<std::chrono::duration<double>>(end - start).count();

    const int times = 10000;

    auto p2 = run<int*>(input, puzzle_2, 1000, times);
    auto p4 = run<std::string*>(lines, puzzle_4, 1000, times);

    std::cout << "Result p2: " << p2.first << ", time elapsed: " << p2.second << "s" << std::endl;
    std::cout << "Result p4: " << p4.first << ", time elapsed: " << p4.second << "s" << std::endl;

    return 0;
}