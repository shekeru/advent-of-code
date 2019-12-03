function intersection(A,B,part) {
 if ((A.staticValue == 0) && (B.staticValue == 0)) return Infinity;
 if ((A.dynamicIsRow != B.dynamicIsRow) && (A.staticValue <= B.dynamicMax) && (A.staticValue >= B.dynamicMin) && (B.staticValue <= A.dynamicMax) && (B.staticValue >= A.dynamicMin)) return [Math.abs(A.staticValue) + Math.abs(B.staticValue),A.steps + B.steps + Math.abs(A.staticValue - B.dynamicStart) + Math.abs(B.staticValue - A.dynamicStart)][part-1];
 return Infinity;
}
function main(input) {
 var wires = input.split("\n").map(e => {var position = [0,0]; var stepsOfPath = 0; return e.split(",").map(function (el) {
  var segment;
   switch (el.slice(0,1)) {
   case "U": segment = {steps: stepsOfPath, dynamicStart: position[1], dynamicIsRow: true, staticValue: position[0], dynamicMax: position[1], dynamicMin: (position[1] -= parseInt(el.slice(1)))}; break;
   case "R": segment = {steps: stepsOfPath, dynamicStart: position[0], dynamicIsRow: false, staticValue: position[1], dynamicMin: position[0], dynamicMax: (position[0] += parseInt(el.slice(1)))}; break;
   case "D": segment = {steps: stepsOfPath, dynamicStart: position[1], dynamicIsRow: true, staticValue: position[0], dynamicMin: position[1], dynamicMax: (position[1] += parseInt(el.slice(1)))}; break;
   case "L": segment = {steps: stepsOfPath, dynamicStart: position[0], dynamicIsRow: false, staticValue: position[1], dynamicMax: position[0], dynamicMin: (position[0] -= parseInt(el.slice(1)))}; break;
  };
  stepsOfPath += segment.dynamicMax - segment.dynamicMin;
  return segment;
 })});
 var bestvalue = Infinity;
 for (var j = 0; j < wires[0].length; j++) {
  for (var k = 0; k < wires[1].length; k++) {
   bestvalue = Math.min(bestvalue,intersection(wires[0][j],wires[1][k],1)); // last parameter is 2 for part 2
  };
 };
 return bestvalue;
}
