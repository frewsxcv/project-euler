main :: IO ()
main = print $ sum [x :: Integer | x <- [1..999], mod x 3 == 0 || mod x 5 == 0]
