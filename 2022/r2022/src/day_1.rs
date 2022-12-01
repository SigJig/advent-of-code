
use std::fs;

const FILE: &str = "./input/day_1.txt";

fn get_input() -> String {
    fs::read_to_string(FILE).expect("ioerror")
}

pub fn day_1() {
    let inp = get_input();
    let mut v: Vec<u32> = vec![0];

    for i in inp.split("\n") {
        if i.is_empty() {
            v.push(0);
        } else {
            let n = v.len() - 1;
            v[n] += i.parse::<u32>().unwrap()
        }
    }
    
    v.sort();
    
    println!("max: {}", &v[v.len() - 1]);
    println!("total: {}", &v[v.len() - 3..].iter().sum::<u32>());
}