
use std::collections::{HashSet};

fn char_prio(c: char) -> u32 {
    if (c as u32) >= ('a' as u32) {
        return (c as u32) - ('a' as u32) + 1;
    }

    (c as u32) - ('A' as u32) + 27
}

fn sol_1(inp: &str) {
    let mut sum: u32 = 0;

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }

        let chars: Vec<char> = line.chars().collect();
        let middle = chars.len() / 2;
        let mut hshset: HashSet<char> = HashSet::new();

        for ch in &chars[0..middle] {
            hshset.insert(*ch);
        }

        for ch in &chars[middle..] {
            if hshset.contains(ch) {
                sum += char_prio(*ch);
                break;
            }
        }
    }

    println!("sum: {}", sum);
}

fn sol_2(inp: &str) {
    let mut sum: u32 = 0;
    let mut sets: [HashSet<char>; 2] = [HashSet::new(), HashSet::new()];

    for (i, line) in inp.split("\n").enumerate() {
        if i % 3 == 0 {
            sets[0].clear();
            sets[1].clear();
            sets[0].extend(line.chars());
        } else if i % 3 == 2 {
            for ch in line.chars() {
                if sets[1].contains(&ch) {
                    sum += char_prio(ch);
                    break;
                }
            }
        } else {
            for ch in line.chars() {
                if sets[0].contains(&ch) {
                    sets[1].insert(ch);
                }
            }
        }
    }

    println!("sol 2 sum: {}", sum);
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}