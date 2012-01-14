package main

import (
   "fmt"
   "big"
)

func main() {
   fmt.Println(digitSum(factorial(100)))
}

func factorial(num int) (ret *big.Int) {
   ret = big.NewInt(1)
   for i := num; i > 0; i-- {
      ret = ret.Mul(ret, big.NewInt(int64(i)))
   }
   return
}

func digitSum(num *big.Int) (sum int) {
   sum = 0
   str := num.String()
   for _, v := range str {
      sum += v - 48
   }
   return
}
