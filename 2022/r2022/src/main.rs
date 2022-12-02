
mod utils;
mod days;

use std::env;

use colored::Colorize;
use days::{day_1, day_2, day_3, day_4, day_5, day_6, day_7, day_8,
    day_9, day_10, day_11, day_12, day_13, day_14, day_15, day_16,
    day_17, day_18, day_19, day_20, day_21, day_22, day_23, day_24, day_25, };

type DayFunction = fn() -> ();

const DAYFUNCTIONS: [DayFunction; 25] = [
    day_1::run, day_2::run, day_3::run, day_4::run, day_5::run, day_6::run,
    day_7::run, day_8::run, day_9::run, day_10::run, day_11::run, day_12::run,
    day_13::run, day_14::run, day_15::run, day_16::run, day_17::run,
    day_18::run, day_19::run, day_20::run, day_21::run, day_22::run,
    day_23::run, day_24::run, day_25::run,
];


fn main() {
    let args: Vec<String> = env::args().collect();
    let day = args[1].parse::<usize>().unwrap();

    println!("{}", format!("Day {}", day).blue());
    DAYFUNCTIONS[day - 1]();
}
