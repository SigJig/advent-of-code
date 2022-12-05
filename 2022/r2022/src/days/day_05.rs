
use std::vec;

use lazy_static::lazy_static;
use regex::Regex;

lazy_static!{
    static ref MOVE_PATTERN: Regex = Regex::new(r"move\s(\d+)\sfrom\s(\d)\sto\s(\d)").unwrap();
    static ref STACK_PATTERN: Regex = Regex::new(r"^\s?(?:(\s{3})|\[([A-Z])\])").unwrap();
    static ref DESC_PATTERN: Regex = Regex::new(r"\s(?:\d+\s{3})*(\d+)").unwrap();
}

fn parse_stacks(inp: &str) -> Vec<Vec<char>> {
    let mut v: Vec<Vec<char>> = vec![Vec::new(); DESC_PATTERN.captures(inp).unwrap()[1].parse::<usize>().unwrap()];
    
    for line in inp.split("\n") {
        let mut current = line;
        for i in 0.. {
            let caps = STACK_PATTERN.captures(current);

            if caps.is_none() {
                break;
            }
            if i >= v.len() {
                panic!("i at illegal index");
            }

            let caps = caps.unwrap();

            // for example "[B]" is group 2, "   " is group 1
            let cap = if caps.get(1).is_some() {&caps[1]} else {&caps[2]};

            if !cap.trim().is_empty() {
                v[i].push(cap.chars().nth(0).unwrap());
            }

            current = &current[caps[0].len()..];
        }
    }

    for x in &mut v {
        x.reverse();
    }

    v
}

fn sol_1(inp: &str) {
    let mut stacks: Vec<Vec<char>> = parse_stacks(inp);

    for cap in MOVE_PATTERN.captures_iter(&inp) {
        let src: usize = cap[2].parse::<usize>().unwrap() - 1;
        let dest: usize = cap[3].parse::<usize>().unwrap() - 1;

        for _ in 0..cap[1].parse::<usize>().unwrap() {
            let c: char = stacks[src].pop().unwrap();
            stacks[dest].push(c);
        }
    }

    for v in stacks {
        print!("{}", v.last().unwrap());
    }
    println!("");
}

fn sol_2(inp: &str) {
    let mut stacks: Vec<Vec<char>> = parse_stacks(inp);

    for cap in MOVE_PATTERN.captures_iter(&inp) {
        let src: usize = cap[2].parse::<usize>().unwrap() - 1;
        let dest: usize = cap[3].parse::<usize>().unwrap() - 1;

        let index: usize = stacks[dest].len();

        for _ in 0..cap[1].parse::<usize>().unwrap() {
            let c: char = stacks[src].pop().unwrap();
            stacks[dest].insert(index, c);
        }
    }

    for v in stacks {
        print!("{}", v.last().unwrap());
    }
    println!("");
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}