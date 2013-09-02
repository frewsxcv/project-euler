use std::*;

fn is_multiple(x: int) -> bool { x % 3 == 0 || x % 5 == 0 }

fn work(x: int) -> int {
   return match x {
      0 => 0,
      y if is_multiple(y) => y + work(x-1),
      _ => work(x-1)
   }
}

fn main() {
   println(int::to_str(work(999)));
}
