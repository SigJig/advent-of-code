
use crate::utils;

struct SectionRange(u32, u32);

impl From<&str> for SectionRange {
    fn from(s: &str) -> SectionRange {
        let mut iter = s.split("-").map(|x| x.parse::<u32>().unwrap());

        SectionRange(iter.next().unwrap(), iter.next().unwrap())
    }
}

impl SectionRange {
    fn overlaps_full(&self, other: &SectionRange) -> bool {
        self.0 <= other.0 && self.1 >= other.1
    }

    fn _in_range(&self, x: u32) -> bool {
        x >= self.0 && x <= self.1
    }

    fn overlaps(&self, other: &SectionRange) -> bool {
        self._in_range(other.0) || self._in_range(other.1)
    }
}

pub fn run() {
    let inp = utils::get_input(4);
    let mut sum_full = 0;
    let mut sum_partial = 0;

    for line in inp.split("\n") {
        let mut iter = line.split(",").map(|x| SectionRange::from(x));
        let (left, right) = (iter.next().unwrap(), iter.next().unwrap());

        if left.overlaps_full(&right) || right.overlaps_full(&left) {
            sum_full += 1;
        }
        if left.overlaps(&right) || right.overlaps(&left) {
            sum_partial += 1;
        }
    }

    println!("sum_full: {}, sum_partial: {}", sum_full, sum_partial);
}