
use std::fs;

fn make_path(day: u32) -> String {
    String::from(format!("./input/day_{}.txt", day))
}

pub fn get_input(day: u32) -> String {
    fs::read_to_string(make_path(day)).expect("ioerror")
}