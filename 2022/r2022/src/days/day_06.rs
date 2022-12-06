
use std::collections::VecDeque;
use std::time::{SystemTime};

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

fn find_marker_fast(inp: &str, length: usize) -> Option<usize> {
    let bytes = inp.as_bytes();

    'head: for i in 0..bytes.len() {
        if i + length >= bytes.len() {
            return None;
        }

        for j in i..i+length {
            for k in j+1..i+length {
                if bytes[j] == bytes[k] {
                    continue 'head;
                }
            }
        }

        return Some(i+length);
    }


    None
}

fn bench_sol(sol: fn(&str,usize)->Option<usize>, inp: &str, length: usize) {
    let mut times: Vec<u128> = Vec::new();
    
    for _ in 0..10000 {
        let start = SystemTime::now();
        sol(inp, length);
        times.push(start.elapsed().unwrap().as_micros());
    }

    println!("time elapsed: {}us(max), {}us(avg), {}us(min)",
        times.iter().max().unwrap(),
        times.iter().sum::<u128>() / times.len() as u128,
        times.iter().min().unwrap());

}

fn sol_1(inp: &str) {
    println!("index {}", find_marker(inp, 4).unwrap());
}

fn sol_2(inp: &str) {
    println!("index {}", find_marker_fast(inp, 14).unwrap());
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);

    bench_sol(find_marker_fast, inp, 14);
    bench_sol(find_marker, inp, 14);
}