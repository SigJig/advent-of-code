
mod utils;
mod days;

use colored::Colorize;
use days::{day_1, day_2};

type DayFunction = fn() -> ();

const DAYFUNCTIONS: [DayFunction; 2] = [
    day_1::run,
    day_2::run
];


fn main() {
    println!("{}", format!("Day {}", DAYFUNCTIONS.len()).blue());
    DAYFUNCTIONS.last().expect("last returned none")();
}
