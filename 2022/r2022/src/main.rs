
mod utils;
mod days;

use std::env;

use colored::Colorize;
use days::{day_01, day_02, day_03, day_04, day_05, day_06, day_07, day_08,
    day_09, day_10, day_11, day_12, day_13, day_14, day_15, day_16,
    day_17, day_18, day_19, day_20, day_21, day_22, day_23, day_24, day_25, };

type DayFunction = fn(&str) -> ();

const DAYFUNCTIONS: [DayFunction; 25] = [
    day_01::run, day_02::run, day_03::run, day_04::run, day_05::run, day_06::run,
    day_07::run, day_08::run, day_09::run, day_10::run, day_11::run, day_12::run,
    day_13::run, day_14::run, day_15::run, day_16::run, day_17::run,
    day_18::run, day_19::run, day_20::run, day_21::run, day_22::run,
    day_23::run, day_24::run, day_25::run,
];


fn main() {
    let args: Vec<String> = env::args().collect();
    let day = if args.len() > 1 {args[1].parse::<usize>().unwrap()} else {10};
    let test = args.len() > 2 || args.len() == 1;

    println!("{}", format!("Day {}", day).blue());
    DAYFUNCTIONS[day - 1](&utils::get_input(test, day as u32));
}
