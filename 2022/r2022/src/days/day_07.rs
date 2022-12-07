
use std::{rc::Rc, cell::RefCell, borrow::BorrowMut};

const INDENT_SIZE: u8 = 4;

struct File {
    path: String,
    size: usize
}

struct Directory {
    path: String,
    children: Vec<Rc<RefCell<Directory>>>,
    files: Vec<File>,
    parent: Option<Rc<RefCell<Directory>>>,
}

struct Fs {
    cwd: Rc<RefCell<Directory>>,
    root: Rc<RefCell<Directory>>,
    readls: bool,
}

fn make_indent(lvl: u8) -> String {
    let mut s = String::with_capacity((lvl * INDENT_SIZE) as usize);

    for _ in 0..(lvl * INDENT_SIZE) {
        s.push(' '); 
    }

    s
}

impl Directory {
    fn new(path: &str, parent: Option<Rc<RefCell<Directory>>>) -> Directory {
        Directory {
            path: String::from(path),
            children: Vec::new(),
            files: Vec::new(),
            parent
        }
    }

    fn print(&self, indent: u8) {
        let indentstr = make_indent(indent);

        for dir in &self.children {
            println!("{}dir {}", indentstr, dir.borrow().path);
            dir.borrow().print(indent + 1);
        }

        for fi in &self.files {
            println!("{}{} {}", indentstr, fi.size, fi.path);
        }
    }

    fn size(&self) -> usize {
        self.files.iter().map(|x| x.size).sum::<usize>()
        + self.children.iter().map(|x| (*x).borrow().size()).sum::<usize>()
    }
}

impl Fs {
    fn _changedir(&mut self, path_raw: &str) {
        if path_raw.starts_with("..") {
            self.cwd = {
                let cwd = self.cwd.borrow();
                if cwd.parent.is_none() {
                    panic!("attempted .. when parent is none");
                }
                cwd.parent.as_ref().unwrap().clone()
            };

            return self._changedir(&path_raw[2..]);
        }

        let mut lastdir = self.cwd.clone();

        if path_raw.starts_with("/") {
            lastdir = self.root.clone();
        }

        for dirname in path_raw.split("/") {
            if dirname.trim().is_empty() {
                continue;
            }

            lastdir = {
                let mut parent = (*lastdir).borrow_mut();
                parent.children.push(
                    Rc::new(RefCell::new(Directory::new(
                        dirname, Some(lastdir.clone())
                    )))
                );
                parent.children.last().unwrap().clone()
            }
                
        }

        self.cwd = lastdir.clone();
    }

    fn cd(&mut self, args: &Vec<&str>) {
        if args.len() < 2 {
            panic!("missing arguments to cd");
        }

        self._changedir(args[1]);
    }

    fn _list(&mut self, line: &str) {
        let tokens: Vec<&str> = line.split(" ").collect();

        if tokens[0] != "dir" {
            (*self.cwd).borrow_mut().files.push(File {
                path: String::from(tokens[1]),
                size: tokens[0].parse::<usize>().unwrap()
            });
        }
    }

    fn ls(&mut self, _args: &Vec<&str>) {
        self.readls = true;
    }

    fn resolve_command(&mut self, args: &Vec<&str>) {
        self.readls = false;
        match args[0] {
            "cd" => self.cd(args),
            "ls" => self.ls(args),
            _ => panic!("unrecognized command {}", args[0])
        };
    }

    fn resolve_read(&mut self, line: &str) {
        if !self.readls {
            panic!("attempted read with disabled readls");
        }

        self._list(line);
    }
}

pub fn run(inp: &str) {
    let root = Rc::new(
        RefCell::new(Directory::new("/", None)));

    let mut fs = Fs {
        cwd: root.clone(),
        root: root,
        readls: false
    };

    for line in inp.split("\n") {
        if line.starts_with("$") {
            fs.resolve_command(&line[2..].split(" ").collect());
        } else {
            fs.resolve_read(line);
        }
    }

    fs.root.borrow().print(0);

    let root_size = fs.root.borrow().size();
    let required = 30_000_000 - (70_000_000 - root_size);
    let mut work: Vec<Rc<RefCell<Directory>>> = vec![fs.root];
    let mut smallest = root_size;
    let mut sum: usize = 0;

    while work.len() > 0 {
        let dir = work.pop().unwrap();
        let size = dir.borrow().size();

        if size <= 100_000 {
            sum += size;
        }
        if size >= required && size < smallest {
            smallest = size;
        }

        work.extend(dir.borrow().children.clone());
    }

    println!("sum: {}, smallest: {}", sum, smallest);

}
