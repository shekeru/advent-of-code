package main
import "fmt"

type Equipment int
const (
  Torch = iota
  Nothing
  Gear
)

type Terrain int
const (
  Rocky = iota
  Wet
  Narrow
)

type Location struct {
  x, y int
}

type World struct {
  values map[Location]int
  target Location
  depth int
}

func mkWorld (depth int, x int, y int) World {
  return World {
    make(map[Location]int),
    Location {x, y},
    depth}
}

func (wp World) level(pl Location) Terrain {
  return Terrain(wp.erode(pl) % 3)
}

func (wp World) erode(pl Location) int {
  if val, ok := wp.values[pl]; ok {
    return val
  }; wp.values[pl] =
    (wp.geoIx(pl) + wp.depth) % 20183
  return wp.values[pl]
}

func (wp World) geoIx(pl Location) int {
    if (pl == Location{0, 0} || pl == wp.target) {
      return 0
    }; if (pl.x == 0) {
      return pl.y * 48271
    }; if (pl.y == 0) {
      return pl.x * 16807
    }; return wp.erode(Location{pl.x - 1, pl.y}) *
      wp.erode(Location{pl.x, pl.y - 1})
}

func main() {
  world := mkWorld(3879, 8, 713)
	fmt.Printf("Silver: %d\n",
     world.silver())
}

func (wp World) silver() int {
    var result = 0
  for x := 0; x <= wp.target.x; x++ {
    for y := 0; y <= wp.target.y; y++ {
      result += int(wp.level(Location{x, y}))
  }}; return result
}
