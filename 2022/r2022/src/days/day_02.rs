
#[derive(PartialEq, Clone, Copy)]
enum Hand {
    Rock = 1,
    Paper = 2,
    Scissor = 3,
}

enum Expected {
    Loss = 1,
    Draw = 2,
    Win = 3,
}

impl Hand {
    fn defeats(&self, other: Hand) -> bool {
        (other as u32) != (((*self as u32) % 3) + 1)
    }

    fn corresponding(&self, expect: Expected) -> Hand {
        match expect {
            Expected::Draw => *self,
            Expected::Win => Hand::from(((*self as u32) % 3) + 1),
            Expected::Loss => Hand::from((((*self as u32) + 1) % 3) + 1)
        }
    }
}

impl From<u32> for Hand {
    fn from(code: u32) -> Hand {
        match code {
            1 => Hand::Rock,
            2 => Hand::Paper,
            3 => Hand::Scissor,
            _ => panic!("invalid hand code {}", code)
        }
    }
}

impl From<u32> for Expected {
    fn from(code: u32) -> Expected {
        match code {
            1 => Expected::Loss,
            2 => Expected::Draw,
            3 => Expected::Win,
            _ => panic!("invalid expect code {}", code)
        }
    }
}

struct Pair(Hand, Hand);

fn index_str(str_: &str, index: usize) -> char {
    str_.chars().nth(index).unwrap()
}

fn convert_left(line: &str) -> Hand {
    Hand::from((index_str(line, 0) as u32) - ('A' as u32) + 1)
}

fn convert_right_u32(line: &str) -> u32 {
    (index_str(line, 2) as u32) - ('X' as u32) + 1
}

fn convert_right(line: &str) -> Hand {
    Hand::from(convert_right_u32(line))
}

fn sum_pairs(pairs: &Vec<Pair>) -> u32 {
    let mut result: u32 = 0;

    for x in pairs {
        result += x.1 as u32;

        if x.1 == x.0 {
            result += 3;
        } else if x.1.defeats(x.0) {
            result += 6;
        }
    }

    result
}

fn sol_1(inp: &str) {
    let mut pairs: Vec<Pair> = vec![];

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }

        if line.len() != 3 {
            println!("parse error");
        }

        pairs.push(Pair(convert_left(line), convert_right(line)));
    }

    println!("my points: {}", sum_pairs(&pairs));
}

fn sol_2(inp: &str) {
    let mut pairs: Vec<Pair> = vec![];

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }

        let left = convert_left(line);

        pairs.push(Pair(left, left.corresponding(Expected::from(convert_right_u32(line)))));
    }

    println!("my points: {}", sum_pairs(&pairs));
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}