
use std::fs;

fn make_path(test: bool, day: u32) -> String {
    if test {
        String::from(format!("./testinput/day_{}.txt", day))
    } else {
        String::from(format!("./input/day_{}.txt", day))
    }
}

pub fn get_input(test: bool, day: u32) -> String {
    fs::read_to_string(make_path(test, day)).expect("ioerror")
}