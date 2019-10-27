package main
import ("fmt"
  "container/heap")

func main() {
  world := mkWorld(3879, 10, 10)
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
    item := heap.Pop(&wp.queue).(*Movement); pos :=
      item.entry; val, ok := wp.visited[pos]
    // Update Visited
    if ok && val <= item.minutes {
      continue
    }; wp.visited[item.entry] = item.minutes
      fmt.Printf("Item: %d\n", *item)
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
        } else if (wp.target == next) {
          var adj = item.minutes + 1
          if (pos.tool != Torch) {
            adj += 7
          }; wp.queue.push(next.x, next.y,
            Torch, adj)
        } else if (wp.level(next) !=
            Terrain(pos.tool)) {
          wp.queue.push(next.x, next.y,
            pos.tool, item.minutes + 1)
        } else {
          wp.queue.push(next.x, next.y,
            wp.swapTool(next, pos.coords),
          item.minutes + 8)
        }
      };
  }; return -1
}

func (wp World) Silver() int {
    var result = 0
  for x := 0; x <= wp.target.x; x++ {
    for y := 0; y <= wp.target.y; y++ {
      result += int(wp.level(Location{x, y}))
  }}; return result
}

func (wp World) swapTool(a, b Location) Equipment {
  for i := 0; i <= 2; i++ {
    if (int(wp.level(a)) != i &&
      int(wp.level(b)) != i) {
        return Equipment(i)
    }
  }; return Torch
}
