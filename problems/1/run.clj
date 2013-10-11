(defn is-multiple [x]
  (or
    (zero? (mod x 3))
    (zero? (mod x 5))))

(println
  (reduce +
    (filter is-multiple
      (range 1000))))
