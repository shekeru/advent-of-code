package main
import "container/heap"

type Position struct {
  coords Location
  tool Equipment
}

type Movement struct {
  entry Position
  minutes int
}

type SearchQueue[] *Movement

func (pq *SearchQueue) push(x int, y int,
    eq Equipment, z int) {
  heap.Push(pq, &Movement{Position{
    Location{x, y}, eq}, z})
}

func (pq SearchQueue) Len() int {
  return len(pq)
}

func (pq SearchQueue) Less (i, j int) bool {
  return pq[i].minutes <= pq[j].minutes
}

func (pq SearchQueue) Swap(i, j int) {
  pq[i], pq[j] = pq[j], pq[i]
}

func (pq *SearchQueue) Push(x interface{})  {
  item := x.(*Movement)
  *pq = append(*pq, item)
}

func (pq *SearchQueue) Pop() interface{} {
  var old, n = *pq, len(*pq)
  var item = old[n - 1]
    old[n - 1] = nil
  *pq = old[0 : n - 1]
  return item
}
