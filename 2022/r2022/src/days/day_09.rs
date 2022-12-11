
use std::collections::HashSet;

enum Direction {
    Up(i32),
    Right(i32),
    Down(i32),
    Left(i32)
}

impl Direction {
    fn new(n: u8, val: i32) -> Direction {
        match n {
            0 => Direction::Up(val),
            1 => Direction::Right(val),
            2 => Direction::Down(val),
            3 => Direction::Left(val),
            _ => panic!("unexpected dir {}", n)
        }
    }
}

#[derive(Clone, Eq, PartialEq, Copy, Hash)]
struct Point {
    x: i32,
    y: i32
}

#[derive(Clone, Copy)]
struct End {
    coords: Point
}

impl End {
    fn diff(&self, other: &End) -> i32 {
        ((
            (self.coords.x - other.coords.x).pow(2)
            +(self.coords.y - other.coords.y).pow(2)
        ) as f64).sqrt() as i32
        //(self.distance_start() - other.distance_start()).abs() as u8
    }

    fn catch_up(&mut self, other: &End) -> &Point {
        if self.coords.x != other.coords.x {
            self.move_by(
                if self.coords.x > other.coords.x {
                    Direction::Left(1)
                } else {
                    Direction::Right(1)
                }
            );
        }

        if self.coords.y != other.coords.y {
            self.move_by(
                if self.coords.y > other.coords.y {
                    Direction::Down(1)
                } else {
                    Direction::Up(1)
                }
            );
        }

        &self.coords
    }

    fn move_by(&mut self, by: Direction) -> &Point {
        match by {
            Direction::Up(count) => self.coords.y += count,
            Direction::Right(count) => self.coords.x += count,
            Direction::Down(count) => self.coords.y -= count,
            Direction::Left(count) => self.coords.x -= count,
        };
        &self.coords
    }
}

fn parse_input(inp: &str) -> Vec<(u8, i32)> {
    let mut res: Vec<(u8, i32)> = Vec::new();

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }
        let args: Vec<&str> = line.split(" ").collect();

        res.push(match args[0] {
            "U" => (0, args[1].parse::<i32>().unwrap()),
            "R" => (1, args[1].parse::<i32>().unwrap()),
            "D" => (2, args[1].parse::<i32>().unwrap()),
            "L" => (3, args[1].parse::<i32>().unwrap()),
            _ => panic!("unexpected {} when parsing", args[0])
        });
    }

    res
}

fn sol_1(inp: &str) {
    let dirs = parse_input(inp);
    let mut head = End {coords: Point{x: 0, y: 0}};
    let mut tail = End {coords: Point{x: 0, y: 0}};
    let mut touched: HashSet<Point> = HashSet::new();

    for (dir, count) in dirs {
        for _ in 0..count {
            head.move_by(Direction::new(dir, 1));
    
            if tail.diff(&head) >= 2 {
                touched.insert(*tail.catch_up(&head));
            }
        }
    }

    println!("num touched: {}", touched.len() + !touched.contains(&Point{x: 0, y: 0}) as usize);
    for _i in touched.iter() {
        // println!("{}, {}", i.x, i.y);
    }
}

fn sol_2(inp: &str) {
    let dirs = parse_input(inp);
    let mut knots: [End; 10] = [End {coords: Point{x: 0, y: 0}}; 10];
    let knot_len = knots.len();
    let mut touched: HashSet<Point> = HashSet::new();

    for (dir, count) in dirs {
        for _ in 0..count {
            knots[0].move_by(Direction::new(dir, 1));
            let mut p: Option<Point> = None;

            for idx in 1..knot_len {
                // iteration starts at 1st element, so index 0
                // on knots is the one before x
                let other = knots[idx-1];
                let x = &mut knots[idx];
                
                if x.diff(&other) >= 2 {
                    let tmp = x.catch_up(&other);

                    if idx == knot_len - 1 {
                        p = Some(*tmp);
                    }
                }
            }

            if p.is_some() {
                touched.insert(p.unwrap());
            }
        }
    }

    println!("num touched (9): {}", touched.len() + !touched.contains(&Point{x: 0, y: 0}) as usize);
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}