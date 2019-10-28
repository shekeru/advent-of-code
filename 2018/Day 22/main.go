package main
import ("fmt"
  "container/heap")

func main() {
  world := mkWorld(3879, 8, 713)
	fmt.Printf("Silver: %d\n",
     world.Silver())
  fmt.Printf("Gold: %d\n",
    world.Gold())
}

func (wp World) Gold() int {
  wp.queue.push(0, 0, Torch, 0)
  var composite = Position{wp.target, Torch}
  // Search for Route, While Queued
  for len(wp.queue) > 0 {
    item := heap.Pop(&wp.queue).(*Movement)
    // Check for Visit
    pos := item.entry; if val, ok :=
      wp.visited[pos]; ok && val <=
        item.minutes {continue}
    // Record Visit
    wp.visited[pos] = item.minutes
    // Check for Target
    if item.entry == composite {
      return item.minutes
    } // Search BFS, nb4
    for _, off := range [4][2]int {
      {-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
        var next = item.entry.coords
        next.y += off[1]; next.x += off[0]
        // Select Out Invalids
        if (next.x < 0 || next.y < 0) {
          continue
        } else if (wp.level(next) !=
            Terrain(pos.tool)) {
          wp.queue.push(next.x, next.y,
            pos.tool, item.minutes + 1)
        } else { for i := 0; i <= 2; i++ {
          switch (Terrain(i)) {
            case wp.level(pos.coords):
              continue
            case wp.level(next):
              continue
          }; wp.queue.push(next.x, next.y,
            Equipment(i), item.minutes + 8)
          }
        }
      }
  }; return -1
}

func (wp World) Silver() int {
    var result = 0
  for x := 0; x <= wp.target.x; x++ {
    for y := 0; y <= wp.target.y; y++ {
      result += int(wp.level(Location{x, y}))
  }}; return result
}
