
use std::collections::VecDeque;

fn vec_duplicates(v: &VecDeque<char>) -> bool {
    for (i, c) in v.iter().enumerate() {
        for j in i+1..v.len() {
            if c == &v[j] {
                return true;
            }
        }
    }

    false
}

fn find_marker(inp: &str, length: usize) -> Option<usize> {
    let mut dq: VecDeque<char> = VecDeque::new();

    for (i, c) in inp.chars().enumerate() {
        dq.push_back(c);
        
        if dq.len() >= length {
            if !vec_duplicates(&dq) {
                return Some(i + 1);
            }
            
            dq.pop_front();
        }
    }

    None
}

fn sol_1(inp: &str) {
    println!("index {}", find_marker(inp, 4).unwrap());
}

fn sol_2(inp: &str) {
    println!("index {}", find_marker(inp, 14).unwrap());
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}