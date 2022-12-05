
use std::vec;

use crate::utils;
use lazy_static::lazy_static;
use regex::Regex;

lazy_static!{
    static ref MOVE_PATTERN: Regex = Regex::new(r"move\s(\d+)\sfrom\s(\d)\sto\s(\d)").unwrap();
}

fn sol_1(stacks: &mut [Vec<char>]) {
    let inp = utils::get_input(5);

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

fn sol_2(stacks: &mut [Vec<char>]) {
    let inp = utils::get_input(5);

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

pub fn run() {
    let mut stacks: [Vec<char>; 9] = [
        vec!['Z', 'P', 'M', 'H', 'R'],
        vec!['P', 'C', 'J', 'B'],
        vec!['S', 'N', 'H', 'G', 'L', 'C', 'D'],
        vec!['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
        vec!['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
        vec!['T', 'F', 'S', 'Z', 'B', 'G'],
        vec!['N', 'R', 'V'],
        vec!['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
        vec!['W', 'Q', 'N', 'J', 'F', 'M', 'L'],
    ];
    let mut test_stacks: [Vec<char>; 3] = [
        vec!['Z', 'N'],
        vec!['M', 'C', 'D'],
        vec!['P'],
    ];

    // sol_1(&mut stacks);
    sol_2(&mut stacks);
}