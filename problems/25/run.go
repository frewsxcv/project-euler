package main

import (
   "fmt"
   "big"
)

func main() {
   x, y := big.NewInt(0), big.NewInt(1)
   var i int

   for i = 1; len(y.String()) < 1000; i++ {
      x, y = y, x
      y.Add(x, y)
   }

   fmt.Println(i)
}
