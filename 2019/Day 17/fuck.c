Label_0() {
// 0: ADD -> {.330, v = 0}, {.331, v = 1}, {.332, v = 1}
// 4: RBX -> i(.5, v = 4014)
  $332 = $330 + $331
  InitDynamic(4014)
// 6: ADD -> i(.7, v = 1182), i(.8, v = 0), {.15, v = 0}
// 10: MUL -> i(.11, v = 1), i(.12, v = 1429), {.24, v = 0}
  $15 := 1182
  $24 := 1429
}

Label_18 () {
// 14: ADD -> {.0, v = 1}, i(.16, v = 0), {.570, v = 0}
  $570 := $1182
// 18: 0, JMP -> {.570, v = 0}, i(.20, v = 36)
  IF ($570 = 0)
    #goto 36
// 21: MUL -> {.571, v = 0}, i(.23, v = 1), {.0, v = 1}
  $1429 := $571
// 25: ADD -> {.570, v = 0}, i(.27, v = -1), {.570, v = 0}
  $570 := $570 - 1
// 29: ADD -> {.24, v = 0}, i(.31, v = 1), {.24, v = 0}
  $24 := $24 + 1
// 33: 0, JMP -> i(.34, v = 0), i(.35, v = 18)
  IF (0 = 0)
    #goto 18
}

Label_36(){
// 36: EQ -> {.571, v = 0}, i(.38, v = 0), {.571, v = 0}
  $571 := $571 is 0
// 40: ADD -> {.15, v = 0}, i(.42, v = 1), {.15, v = 0}
  $15++
// 44: EQ -> {.15, v = 0}, i(.46, v = 1429), {.570, v = 0}
// 48: 0, JMP -> {.570, v = 0}, i(.50, v = 14)
  $570 := $15 is 1429
  IF($15 != 1429)
    #goto 14
}
// 51: ADD -> i(.52, v = 58), i(.53, v = 0), [rbx + 2]
// 55: 0, JMP -> i(.56, v = 0), i(.57, v = 786)
// 58: 0, JMP -> {.332, v = 1}, i(.60, v = 62)
// 61: HALT -
#halt
// 62: ADD -> i(.63, v = 333), i(.64, v = 0), [rbx + 2]
// 66: ADD -> i(.67, v = 0), i(.68, v = 73), [rbx + 2]
// 70: 0, JMP -> i(.71, v = 0), i(.72, v = 579)
// 73: ADD -> i(.74, v = 0), i(.75, v = 0), {.572, v = 0}
// 77: MUL -> i(.78, v = 1), i(.79, v = 0), {.573, v = 0}
// 81: IN -> {.574, v = 0}
// 83: ADD -> i(.84, v = 1), {.573, v = 0}, {.573, v = 0}
// 87: LT -> {.574, v = 0}, i(.89, v = 65), {.570, v = 0}
// 91: 1, JMP -> {.570, v = 0}, i(.93, v = 151)
// 94: LT -> i(.95, v = 67), {.574, v = 0}, {.570, v = 0}
// 98: 1, JMP -> {.570, v = 0}, i(.100, v = 151)
// 101: ADD -> {.574, v = 0}, i(.103, v = -64), {.574, v = 0}
// 105: MUL -> {.574, v = 0}, i(.107, v = -1), {.574, v = 0}
// 109: ADD -> {.572, v = 0}, i(.111, v = 1), {.572, v = 0}
// 113: LT -> {.572, v = 0}, i(.115, v = 11), {.570, v = 0}
// 117: 0, JMP -> {.570, v = 0}, i(.119, v = 165)
// 120: ADD -> i(.121, v = 1182), {.572, v = 0}, {.127, v = 0}
// 124: ADD -> {.574, v = 0}, i(.126, v = 0), {.0, v = 1}
// 128: IN -> {.574, v = 0}
// 130: ADD -> i(.131, v = 1), {.573, v = 0}, {.573, v = 0}
// 134: EQ -> {.574, v = 0}, i(.136, v = 10), {.570, v = 0}
// 138: 1, JMP -> {.570, v = 0}, i(.140, v = 189)
// 141: EQ -> {.574, v = 0}, i(.143, v = 44), {.570, v = 0}
// 145: 0, JMP -> {.570, v = 0}, i(.147, v = 158)
// 148: 1, JMP -> i(.149, v = 1), i(.150, v = 81)
// 151: ADD -> i(.152, v = 0), i(.153, v = 340), [rbx + 2]
// 155: 1, JMP -> i(.156, v = 1), i(.157, v = 177)
// 158: ADD -> i(.159, v = 0), i(.160, v = 477), [rbx + 2]
// 162: 1, JMP -> i(.163, v = 1), i(.164, v = 177)
// 165: ADD -> i(.166, v = 514), i(.167, v = 0), [rbx + 2]
// 169: MUL -> i(.170, v = 176), i(.171, v = 1), [rbx + 2]
// 173: 0, JMP -> i(.174, v = 0), i(.175, v = 579)
// 176: HALT -
#halt
// 177: MUL -> i(.178, v = 1), i(.179, v = 184), [rbx + 2]
// 181: 1, JMP -> i(.182, v = 1), i(.183, v = 579)
// 184: OUT -> {.574, v = 0}
// 186: OUT -> i(.187, v = 10)
// 188: HALT -
#halt
// 189: LT -> {.573, v = 0}, i(.191, v = 22), {.570, v = 0}
// 193: 0, JMP -> {.570, v = 0}, i(.195, v = 165)
// 196: MUL -> i(.197, v = 1), {.572, v = 0}, {.1182, v = 14}
// 200: ADD -> i(.201, v = 375), i(.202, v = 0), [rbx + 2]
// 204: ADD -> i(.205, v = 211), i(.206, v = 0), [rbx + 2]
// 208: 0, JMP -> i(.209, v = 0), i(.210, v = 579)
// 211: ADD -> i(.212, v = 1182), i(.213, v = 11), [rbx + 2]
// 215: MUL -> i(.216, v = 222), i(.217, v = 1), [rbx + 2]
// 219: 1, JMP -> i(.220, v = 1), i(.221, v = 979)
// 222: ADD -> i(.223, v = 0), i(.224, v = 388), [rbx + 2]
// 226: MUL -> i(.227, v = 1), i(.228, v = 233), [rbx + 2]
// 230: 1, JMP -> i(.231, v = 1), i(.232, v = 579)
// 233: ADD -> i(.234, v = 1182), i(.235, v = 22), [rbx + 2]
// 237: MUL -> i(.238, v = 1), i(.239, v = 244), [rbx + 2]
// 241: 0, JMP -> i(.242, v = 0), i(.243, v = 979)
// 244: ADD -> i(.245, v = 401), i(.246, v = 0), [rbx + 2]
// 248: ADD -> i(.249, v = 255), i(.250, v = 0), [rbx + 2]
// 252: 0, JMP -> i(.253, v = 0), i(.254, v = 579)
// 255: ADD -> i(.256, v = 1182), i(.257, v = 33), [rbx + 2]
// 259: MUL -> i(.260, v = 1), i(.261, v = 266), [rbx + 2]
// 263: 0, JMP -> i(.264, v = 0), i(.265, v = 979)
// 266: MUL -> i(.267, v = 1), i(.268, v = 414), [rbx + 2]
// 270: MUL -> i(.271, v = 277), i(.272, v = 1), [rbx + 2]
// 274: 0, JMP -> i(.275, v = 0), i(.276, v = 579)
// 277: IN -> {.575, v = 1}
// 279: EQ -> {.575, v = 1}, i(.281, v = 89), {.570, v = 0}
// 283: EQ -> {.575, v = 1}, i(.285, v = 121), {.575, v = 1}
// 287: ADD -> {.575, v = 1}, {.570, v = 0}, {.575, v = 1}
// 291: IN -> {.574, v = 0}
// 293: EQ -> {.574, v = 0}, i(.295, v = 10), {.570, v = 0}
// 297: 0, JMP -> {.570, v = 0}, i(.299, v = 291)
// 300: OUT -> i(.301, v = 10)
// 302: ADD -> i(.303, v = 0), i(.304, v = 1182), [rbx + 2]
// 306: MUL -> i(.307, v = 1), i(.308, v = 313), [rbx + 2]
// 310: 1, JMP -> i(.311, v = 1), i(.312, v = 622)
// 313: 1, JMP -> {.575, v = 1}, i(.315, v = 327)
// 316: MUL -> i(.317, v = 1), i(.318, v = 1), {.575, v = 1}
// 320: MUL -> i(.321, v = 1), i(.322, v = 327), [rbx + 2]
// 324: 0, JMP -> i(.325, v = 0), i(.326, v = 786)
// 327: OUT -> {.438, v = 0}
// 329: HALT -
#halt
