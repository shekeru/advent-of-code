let Input =
`.##..
  ##.#.
  ##.##
  .#..#
  #.###`;
let Location = {};
let Arrays = Input.split('\n').map((x) => Array.from(x.trim()));
for (let Idx in Arrays) {
    let String = Arrays[Idx];
    for (let Jdx in String) {
        Location[[Idx, Jdx]] =
          String[Jdx] == '#'
    }
}
function Adjacent(X, Y) {
  return [
    [X - 1, Y], [X + 1, Y],
    [X, Y - 1], [X, Y + 1]
  ].map((v) => Location[v]).reduce
    ((a, v) => a + (v || 0), 0)
}

function Step() {
  for(Key in Location) {
    let A = JSON.parse(`[${Key}]`)
    let Val = Adjacent(A[0], A[1])
    if(Location[Key]) {
      Location[Key] = (Val == 1)
    } else {
      Location[Key] = Val && (Val <= 2)
    }
  }
}

let Hashes = new Set()
function Layout(){
  let V = Object.values(Location).toString()
  if(Hashes.has(V))
    return true;
  else {
    Hashes.add(V)
  }
}

while(true) {
  Step()
  if(Layout())
    break;
}

Step()
console.log(Location)
