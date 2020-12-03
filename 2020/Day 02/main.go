package main; import ("fmt"; "strings"; "os"; "bufio")

func main() {
  var a, b, X, Y int
  var C byte; var P string
  file, _ := os.Open("input.txt")
    defer file.Close()
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    fmt.Sscanf(scanner.Text(), "%d-%d %c: %s", &X, &Y, &C, &P)
    if V := strings.Count(P, string(C)); X <= V && V <= Y { a++ }
    if (C == P[X-1]) != (C == P[Y-1]) { b++ }
  }; fmt.Printf("Silver: %d\nGold: %d\n", a, b)
}
