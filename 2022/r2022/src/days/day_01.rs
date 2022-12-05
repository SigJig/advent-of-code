
pub fn run(inp: &str) {
    let mut v: Vec<u32> = vec![0];

    for i in inp.split("\n") {
        if i.is_empty() {
            v.push(0);
        } else {
            let n = v.len() - 1;
            v[n] += i.parse::<u32>().unwrap()
        }
    }
    
    v.sort();
    
    println!("max: {}", &v[v.len() - 1]);
    println!("total: {}", &v[v.len() - 3..].iter().sum::<u32>());
}