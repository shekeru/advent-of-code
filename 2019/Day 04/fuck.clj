(defn asc [x] (= (sort x) (seq x)))
(def freqs
  (->> (range 136760 595730)
  (map str) (filter asc)
  (map #(map last (frequencies %)))
))

(def part1 (filter
  #(some (fn [x] (< 1 x)) %) freqs
))
(def part2 (filter
  #(some (fn [x] (= 2 x)) %) part1
))

(println "Silver:"
  (count part1))
(println "Gold:"
  (count part2))
