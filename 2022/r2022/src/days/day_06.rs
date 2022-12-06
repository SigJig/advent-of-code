
use std::collections::{VecDeque, HashSet};
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

// up to 3x as slow as find_marker_fast
// bench with 100 iterations: 1399us(max), 1307us(avg), 1287us(min)
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

// bench with 100 iterations: 937us(max), 644us(avg), 514us(min)
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

// up to 20x as slow as find_marker_fast
// benched with 100 iterations: 12250us(max), 9763us(avg), 9617us(min)
fn find_marker_set(inp: &str, length: usize) -> Option<usize> {
    let bytes = inp.as_bytes();
    let mut set: HashSet<u8> = HashSet::new();
    for i in 0..inp.len() {
        for j in i..i+length {
            set.insert(bytes[j]);
        }

        if set.len() == length {
            return Some(i+length);
        }

        set.clear();
    }

    None
}

fn bench_sol(sol: fn(&str,usize)->Option<usize>, inp: &str, length: usize) {
    let mut times: Vec<u128> = Vec::new();
    
    for _ in 0..100 {
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
    println!("index {}", find_marker_set(inp, 14).unwrap());
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);

    bench_sol(find_marker_fast, inp, 14);
    bench_sol(find_marker, inp, 14);
    bench_sol(find_marker_set, inp, 14);
}