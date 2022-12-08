
fn parse_input(inp: &str) -> Vec<Vec<u8>> {
    let mut result: Vec<Vec<u8>> = Vec::new();

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }

        result.push(Vec::new());

        for c in line.chars() {
            result.last_mut().unwrap().push(c.to_digit(10).unwrap() as u8);
        }
    }

    result
}

fn highest_y(grid: &[Vec<u8>], idx: usize) -> u8 {
    let mut highest = 0;
    for g in grid {
        if g[idx] > highest {
            highest = g[idx];
        }
    }

    highest
}

fn sol_1(inp: &str) {
    let grid = parse_input(inp);
    let grid_len = grid.len();

    let mut visible = 0;

    for (xidx, xaxis) in grid[1..grid_len - 1].iter().enumerate() {
        for (yidx, elem) in xaxis[1..grid_len - 1].iter().enumerate() {
            if *elem > highest_y(&grid[..xidx+1], yidx+1)
                    || *elem > highest_y(&grid[xidx+2..], yidx+1)
                    || elem > xaxis[..yidx+1].iter().max().unwrap()
                    || elem > xaxis[yidx+2..].iter().max().unwrap() {
                visible += 1;
            }
        }
    }
    visible += grid_len * 2 + (grid_len - 2) * 2;

    println!("visible: {}", visible);
}

fn sol_2(inp: &str) {
    let grid = parse_input(inp);
    let grid_len = grid.len();

    let mut highest = 0;

    for (xidx, xaxis) in grid[1..grid_len - 1].iter().enumerate() {
        for (yidx, elem) in xaxis[1..grid_len - 1].iter().enumerate() {
            let tmp = {
                let mut s = 1;
                for z in 1..xidx+1 {
                    if *elem > grid[xidx+1-z][yidx+1] {
                        s += 1;
                    } else {
                        break;
                    }
                }
                s
            } * {
                let mut s = 1;
                for z in 1..yidx+1 {
                    if *elem > xaxis[yidx+1-z] {
                        s += 1;
                    } else {
                        break;
                    }
                }
                s
            } * {
                let mut s = 1;
                for z in xidx+2..grid_len-1 {
                    if *elem > grid[z][yidx+1] {
                        s += 1;
                    } else {
                        break;
                    }
                }
                s
            } * {
                let mut s = 1;
                for z in yidx+2..grid_len-1 {
                    if *elem > xaxis[z] {
                        s += 1;
                    } else {
                        break;
                    }
                }
                s
            };

            if tmp > highest {
                highest = tmp;
            }
        }
    }

    println!("scenic score: {}", highest);
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}