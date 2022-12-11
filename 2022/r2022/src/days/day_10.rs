

trait Opcode {
    fn tick(&mut self, registers: &mut [i32]) -> bool;
}

struct Addx {
    val: i32,
    ticks: u8
}

impl Addx {
    fn new(val: i32) -> Addx {
        Addx {val, ticks: 0}
    }
}

impl Opcode for Addx {
    fn tick(&mut self, registers: &mut[i32]) -> bool {
        self.ticks += 1;

        if self.ticks >= 2 {
            registers[0] += self.val;
            return true;
        }

        false
    }
}

struct Noop {

}

impl Opcode for Noop {
    fn tick(&mut self, _registers: &mut[i32]) -> bool {
        true
    }
}

struct Vm {
    registers: [i32; 1],
    instructions: Vec<Box<dyn Opcode>>,
    inst_p: usize
}

impl Vm {
    fn tick(&mut self) -> bool {
        let instruction = &mut self.instructions[self.inst_p];
        if instruction.tick(&mut self.registers) {
            self.inst_p += 1;
            
            if self.inst_p >= self.instructions.len() {
                return true;
            }
        }

        false
    }
}

fn parse_input(inp: &str) -> Vec<Box<dyn Opcode>> {
    let mut res: Vec<Box<dyn Opcode>> = Vec::new();

    for line in inp.split("\n") {
        if line.is_empty() {
            continue;
        }

        let split: Vec<&str> = line.split(" ").collect();

        match split[0] {
            "addx" => res.push(Box::new(Addx::new(split[1].parse::<i32>().unwrap()))),
            "noop" => res.push(Box::new(Noop {})),
            _ => panic!("unrecognized opcode \"{}\"", split[0])
        }
    }

    res
}

fn sol_1_print(regvals: &Vec<i32>) {
    let mut sum = 0;

    for idx in 0..regvals.len() {
        let ridx = 20 + (40 * idx);

        if ridx >= regvals.len() {
            break;
        }

        println!("{}: {}", ridx, regvals[ridx-1]);
        sum += ridx as i32 * regvals[ridx-1];
    }

    println!("sum: {}", sum);
}

fn sol_1(inp: &str) {
    let opcodes = parse_input(inp);
    let mut vm = Vm {registers: [1; 1], instructions: opcodes, inst_p: 0};
    let mut v: Vec<i32> = Vec::new();

    loop {
        v.push(vm.registers[0]);

        if vm.tick() {
            break;
        }
    }

    sol_1_print(&v);

}

fn sol_2(inp: &str) {
    let opcodes = parse_input(inp);
    let mut vm = Vm {registers: [1; 1], instructions: opcodes, inst_p: 0};
    
    for _ in 0..6 {
        for x in 0..40 {
            if vm.registers[0] - 1 <= x  && x <= vm.registers[0] + 1 {
                print!("#");
            } else {
                print!(".");
            }

            vm.tick();
        }
        println!("");
    }
}

pub fn run(inp: &str) {
    sol_1(inp);
    sol_2(inp);
}