// A poor attempt at a naive solution in Rust

use std::io;
use std::collections::HashMap;

fn main() {
    let lines = io::stdin().lines();
    let mut tree = HashMap::<String, Vec<String>>::new();

    let mut steps: Option<String> = None;
    let mut line_index = 0;
    for line in lines {
        let line = line.unwrap();

        if line_index == 0 {
            steps = Some(line);
        } else if line_index > 1 {
            let parts = line.split(" = ").collect::<Vec<&str>>();
            let parent = parts[0];
            let children_str = parts[1];
            let children = children_str[1..(children_str.len() - 1)].split(", ");
            tree.insert(String::from(parent), children.map(|str| String::from(str)).collect());
        }

        line_index += 1;
    }

    let mut current: Vec<&String> = tree.keys().filter(|key| key.ends_with("A")).collect();
    eprintln!("Current: {:?}", current);
    let mut i = 0;
    let mut step_iter = steps.iter();
    loop {
        let mut step = step_iter.next();
        if step.is_none() {
            step_iter = steps.iter();
            step = step_iter.next();
        }
        
        let step = step.unwrap();
        
        if step == "L" {
            let new = current.iter().map(|key| &(tree.get(*key).unwrap()[0])).collect();
            current = new;
        } else {
            let new = current.iter().map(|key| &(tree.get(*key).unwrap()[1])).collect();
            current = new;
        }

        if current.iter().all(|key| key.ends_with("Z")) {
            break;
        }

        if i % 1000000 == 0 {
            eprintln!("{}: {:?}", i, current);
        }

        i += 1;
    }

    eprintln!("Result: {}", i);
}