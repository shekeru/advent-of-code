package main

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
  queue SearchQueue
  visited map[Position]int
  values map[Location]int
  target Location
  depth int
}

func mkWorld (depth int, x int, y int) World {
  return World {
    make(SearchQueue, 0),
    make(map[Position]int),
    make(map[Location]int),
    Location {x, y},
    depth}
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

func (wp World) erode(pl Location) int {
  if val, ok := wp.values[pl]; ok {
    return val
  }; wp.values[pl] =
    (wp.geoIx(pl) + wp.depth) % 20183
  return wp.values[pl]
}

func (wp World) level(pl Location) Terrain {
  return Terrain(wp.erode(pl) % 3)
}
