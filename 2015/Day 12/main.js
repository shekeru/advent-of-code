const json = JSON.parse(require('fs')
  .readFileSync('text.json'));

class Counter {
  constructor(js, omit) {
    this.omit = omit
    this.value = 0
    this.iter(js)
  }
  iter(xvs) {
    switch (typeof xvs) {
      case 'number':
        this.value += xvs
        break
      case 'object':
        if(Array.isArray(xvs) || !Object.values(xvs)
          .includes(this.omit)) for(let t in xvs)
            this.iter(xvs[t])
        break
      default:
        break
    }
  }
}

var part1 = new Counter(json),
  part2 = new Counter(json, "red")

console.log("Silver:", part1.value)
console.log("Gold:", part2.value)
