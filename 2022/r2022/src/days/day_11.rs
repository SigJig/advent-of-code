
use std::{collections::{VecDeque}, rc::Rc, cell::RefCell};

use regex::Regex;
use lazy_static::lazy_static;

lazy_static! {
    static ref MONKEY_PAT: Regex = Regex::new(r#"Monkey (\d+):\n\s{2}Starting items: (\d+(?:,\s\d+)*),?\n\s{2}Operation: new = ([a-zA-Z0-9]+\s(?:\+|-|\*|/)\s[a-zA-Z0-9]+)\n\s{2}Test: divisible by (\d+)\n\s{4}If true: throw to monkey (\d+)\n\s{4}If false: throw to monkey (\d+)"#).unwrap();
}

struct Monkey {
    items: Rc<RefCell<VecDeque<u128>>>,
    inspect_args: Vec<String>,
    test_div: u32,
    test_throw: [usize; 2],
}

impl Monkey {
    fn _parse_inspect_arg(&self, idx: usize) -> u128 {
        match &self.inspect_args[idx][..] {
            "old" => self.items.borrow()[0],
            _ => self.inspect_args[idx].parse::<u128>().unwrap()
        }
    }
    
    fn has_items(&self) -> bool {
        self.items.borrow().len() > 0
    }

    fn inspect(&self) {
        let mut tmp = self._parse_inspect_arg(0);
        let operand = self._parse_inspect_arg(2);

        match &self.inspect_args[1][..] {
            "+" => tmp += operand,
            "-" => tmp -= operand,
            "*" => tmp *= operand,
            "/" => tmp /= operand,
            _ => panic!("unrecognized operator {}", self.inspect_args[1])
        };

        self.items.borrow_mut()[0] = tmp;
    }

    fn relief(&self) {
        self.items.borrow_mut()[0] /= 3;
    }

    fn test(&self) -> usize {
        if (self.items.borrow()[0] % self.test_div as u128) == 0 {
            self.test_throw[0]
        } else {
            self.test_throw[1]
        }
    }

    fn reduce_worry(&self, modulo: u32) {
        self.items.borrow_mut()[0] %= modulo as u128;
    }

    fn throw_to(&self, other: &Monkey) {
        other.items.borrow_mut().push_back(self.items.borrow_mut().pop_front().unwrap());
    }
}

fn parse_input(inp: &str) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = Vec::new();

    for cap in MONKEY_PAT.captures_iter(inp) {
        monkeys.push(Monkey {
            items: Rc::new(RefCell::new(cap[2].split(",").map(|x| x.trim().parse::<u128>().unwrap()).collect())),
            inspect_args: cap[3].trim().split(" ").map(|x| String::from(x)).collect(),
            test_div: cap[4].parse::<u32>().unwrap(),
            test_throw: [cap[5].parse::<usize>().unwrap(), cap[6].parse::<usize>().unwrap()],
        })
    }

    monkeys
}

fn sol_1(inp: &str) {
    let monkeys = parse_input(inp);
    let mut inspect_c: Vec<u128> = vec![0; monkeys.len()];

    for _ in 0..20 {
        for (idx, m) in monkeys.iter().enumerate() {
            while m.has_items() {
                m.inspect();
                m.relief();
                let throw = m.test();

                m.throw_to(&monkeys[throw]);
    
                inspect_c[idx] += 1;
            }
        }
    }

    inspect_c.sort();

    let last = inspect_c.len() - 1;
    println!("monkey business: {}", inspect_c[last] * inspect_c[last-1])
}

fn sol_2(inp: &str) {
    let monkeys = parse_input(inp);
    let mut inspect_c: Vec<u128> = vec![0; monkeys.len()];
    let modulo = monkeys.iter().map(|x| x.test_div).product();

    for _ in 0..10000 {
        for (idx, m) in monkeys.iter().enumerate() {
            while m.has_items() {
                m.inspect();
                m.reduce_worry(modulo);
                let throw = m.test();
    
                m.throw_to(&monkeys[throw]);
    
                inspect_c[idx] += 1;
            }
        }
    }

    inspect_c.sort();

    let last = inspect_c.len() - 1;
    println!("monkey business: {}", inspect_c[last] * inspect_c[last-1])

}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}