fn is_multiple(x: int) -> bool {x % 3 == 0 || x % 5 == 0}

fn sum_multiples(x: int) -> int {
   return match x {
      0 => 0,
      y if is_multiple(y) => y + sum_multiples(x-1),
      _ => sum_multiples(x-1)
   }
}

fn main() {
   println(sum_multiples(999).to_str());
}
