
use std::{rc::Rc, ptr};

struct File {
    path: String,
    size: usize
}

struct Directory {
    path: String,
    children: Vec<Directory>,
    files: Vec<File>,
    parent: Option<Rc<Directory>>,
    cwd: Option<Rc<Directory>>,
}

impl Directory {
    fn changedir(&mut self, path: &str) {
        if path.starts_with("/") {
            panic!("can't change dir to absolute from relative");
        }

        let mut last: Rc<Directory> = Rc::from(self);
        for dir in path.split("/") {
        }
    }

    fn cd(&mut self, args: &Vec<&str>) {
        self.changedir(args[1]);
    }

    fn ls(&mut self, _args: &Vec<&str>) {

    }

    fn add_file(&mut self, path: &str, size: usize) {
        self.files.push(File {path: String::from(path), size: size});
    }

    fn resolve_command(&mut self, args: &Vec<&str>) {
        match args[0] {
            "cd" => self.cd(args),
            "ls" => self.ls(args),
            _ => panic!("unrecognized command {}", args[0])
        };
    }
}

fn sol_1(inp: &str) {
    let root = Directory {
        path: String::from("/"),
        children: Vec::new(),
        files: Vec::new(),
        parent: None,
        cwd: None
    };

    for line in inp.split("\n") {
        if !line.starts_with("$") {
            panic!("expected $");
        }

        let args: Vec<&str> = line.split(" ").collect();

        root.resolve_command(&args);
    }
}

pub fn run(_inp: &str) {

}