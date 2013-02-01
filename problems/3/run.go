package main

import (
   "math"
   "fmt"
)

const Input = 600851475143

func main() {
   s := sqrt(Input)
   for s > 0 && !(Input % s == 0 && isPrime(s)) {
      s -= 1
   }
   fmt.Println(s)
}

func sqrt(num int64) int64 {
   return int64(math.Floor(math.Sqrt(float64(num))))
}

func isPrime(num int64) bool {
   for s := sqrt(num); s > 1; s-- {
      if num % s == 0 {
         return false
      }
   }
   return true
}
