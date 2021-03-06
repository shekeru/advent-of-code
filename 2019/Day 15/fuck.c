Label_0() {
// 0: IN -> {.1033, v = 0}
  $33 := input()
// 2: EQ -> {.1033, v = 0}, i(.4, v = 1), {.1032, v = 0}
// 6: 1, JMP -> {.1032, v = 0}, i(.8, v = 31)
  IF ($33 = 1)
    #goto 31
// 9: EQ -> {.1033, v = 0}, i(.11, v = 2), {.1032, v = 0}
// 13: 1, JMP -> {.1032, v = 0}, i(.15, v = 58)
  IF ($33 = 2)
    #goto 58
// 16: EQ -> {.1033, v = 0}, i(.18, v = 3), {.1032, v = 0}
// 20: 1, JMP -> {.1032, v = 0}, i(.22, v = 81)
  IF ($33 = 3)
    #goto 81
// 23: EQ -> {.1033, v = 0}, i(.25, v = 4), {.1032, v = 0}
// 27: 1, JMP -> {.1032, v = 0}, i(.29, v = 104)
  IF ($33 = 4)
    #goto 104
// 30: HALT -
  #halt
}

Label_31(direction N) {
// 31: ADD -> {.1034, v = 21}, i(.33, v = 0), {.1039, v = 0}
  xNew := xStart
// 35: MUL -> {.1036, v = 1}, i(.37, v = 1), {.1041, v = 0}
  bnX := boX
// 39: ADD -> {.1035, v = 21}, i(.41, v = -1), {.1040, v = 0}
  yNew := yStart - 1
// 43: EQ -> {.1038, v = 1}, i(.45, v = 0), {.1043, v = 0}
// 47: MUL -> i(.48, v = -1), {.1043, v = 0}, {.1032, v = 0}
// 51: ADD -> {.1037, v = 10}, {.1032, v = 0}, {.1042, v = 0}
  bnY := !boY
  $32 := -bnY
  newHash := oldHash + $32
// 55: 0, JMP -> i(.56, v = 0), i(.57, v = 124)
  #goto 124
}

Label_58(direction S) {
// 58: ADD -> {.1034, v = 21}, i(.60, v = 0), {.1039, v = 0}
  xNew := xStart
// 62: MUL -> i(.63, v = 1), {.1036, v = 1}, {.1041, v = 0}
  bnX := boX
// 66: ADD -> {.1035, v = 21}, i(.68, v = 1), {.1040, v = 0}
  yNew := yStart + 1
// 70: EQ -> {.1038, v = 1}, i(.72, v = 0), {.1043, v = 0}
// 74: ADD -> {.1037, v = 10}, {.1038, v = 1}, {.1042, v = 0}
  bnY := !boY
  newHash := oldHash + boY
// 78: 1, JMP -> i(.79, v = 1), i(.80, v = 124)
  #goto 124
}

Label_81(direction W) {
// 81: ADD -> {.1034, v = 21}, i(.83, v = -1), {.1039, v = 0}
  xNew := xStart - 1
// 85: EQ -> {.1036, v = 1}, i(.87, v = 0), {.1041, v = 0}
  bnX := 36 is 0
// 89: MUL -> i(.90, v = 1), {.1035, v = 21}, {.1040, v = 0}
  yNew := yStart
// 93: MUL -> {.1038, v = 1}, i(.95, v = 1), {.1043, v = 0}
// 97: ADD -> i(.98, v = 0), {.1037, v = 10}, {.1042, v = 0}
  bnY := boY
  newHash := oldHash
// 101: 1, JMP -> i(.102, v = 1), i(.103, v = 124)
  #goto 124
}

Label_104(direction E) {
// 104: ADD -> {.1034, v = 21}, i(.106, v = 1), {.1039, v = 0}
  xNew := xStart + 1
// 108: EQ -> {.1036, v = 1}, i(.110, v = 0), {.1041, v = 0}
  bnX := boX is 0
// 112: MUL -> i(.113, v = 1), {.1035, v = 21}, {.1040, v = 0}
  yNew := yStart
// 116: ADD -> {.1038, v = 1}, i(.118, v = 0), {.1043, v = 0}
// 120: ADD -> i(.121, v = 0), {.1037, v = 10}, {.1042, v = 0}
  bnY := boY
  newHash := oldHash
  #goto 124
}

Label_124() {
// 124: 0, JMP -> {.1039, v = 0}, i(.126, v = 217)
  IF (xNew = 0)
    #goto 217
// 127: 0, JMP -> {.1040, v = 0}, i(.129, v = 217)
  IF (yNew = 0)
    #goto 217
// 130: EQ -> {.1039, v = 0}, i(.132, v = 40), {.1032, v = 0}
// 134: 1, JMP -> {.1032, v = 0}, i(.136, v = 217)
  IF(xNew = 40)
    #goto 217
// 137: EQ -> {.1040, v = 0}, i(.139, v = 40), {.1032, v = 0}
// 141: 1, JMP -> {.1032, v = 0}, i(.143, v = 217)
  IF(yNew = 40)
    #goto 217
// 144: EQ -> {.1039, v = 0}, i(.146, v = 33), {.1032, v = 0}
// 148: 0, JMP -> {.1032, v = 0}, i(.150, v = 165)
  IF(xNew != 33)
    #goto 165
// 151: EQ -> {.1040, v = 0}, i(.153, v = 33), {.1032, v = 0}
// 155: 0, JMP -> {.1032, v = 0}, i(.157, v = 165)
  IF(yNew != 33)
    #goto 165
// 158: ADD -> i(.159, v = 0), i(.160, v = 2), {.1044, v = 0}
  $nextBlock := 2
// 162: 0, JMP -> i(.163, v = 0), i(.164, v = 224)
  #goto 224
}

Label_165() {
// 165: MUL -> {.1041, v = 0}, {.1043, v = 0}, {.1032, v = 0}
// 169: 0, JMP -> {.1032, v = 0}, i(.171, v = 179)
  IF(bnX = 0 || bnY = 0)
    #goto 179
// 172: MUL -> i(.173, v = 1), i(.174, v = 1), {.1044, v = 0}
  $nextBlock := 1
// 176: 1, JMP -> i(.177, v = 1), i(.178, v = 224)
  #goto 224
}

Label_179() {
// 179: ADD -> {.1041, v = 0}, {.1043, v = 0}, {.1032, v = 0}
// 183: 0, JMP -> {.1032, v = 0}, i(.185, v = 217)
  IF(!bnX && !bnY)
    #goto 217
// 186: ADD -> {.1042, v = 0}, {.1043, v = 0}, {.1032, v = 0}
// 190: ADD -> {.1032, v = 0}, i(.192, v = -1), {.1032, v = 0}
// 194: MUL -> {.1032, v = 0}, i(.196, v = 39), {.1032, v = 0}
// 198: ADD -> {.1032, v = 0}, {.1039, v = 0}, {.1032, v = 0}
// 202: ADD -> i(.203, v = -1), {.1032, v = 0}, {.1032, v = 0}
  $32 := newHash + bnY
  $32 -= 1
  $32 *= 39
  $32 += xNew
  $32 -= 1
// 206: ADD -> i(.207, v = 252), {.1032, v = 0}, {.211, v = 0}
// 210: LT -> {.0, v = 3}, i(.212, v = 42), {.1044, v = 0}
  [211] := 252 + $32
  $nextBlock := [211] < 42
// 214: 0, JMP -> i(.215, v = 0), i(.216, v = 224)
  #goto 224
}

Label_217() {
// 217: MUL -> i(.218, v = 0), i(.219, v = 1), {.1044, v = 0}
// 221: 0, JMP -> i(.222, v = 0), i(.223, v = 224)
  $nextBlock := 0
  #goto 224
}

Label_224() {
// 224: 0, JMP -> {.1044, v = 0}, i(.226, v = 247)
  IF($nextBlock = 0)
    #goto 247
// 227: ADD -> {.1039, v = 0}, i(.229, v = 0), {.1034, v = 21}
  xStart := xNew
// 231: ADD -> {.1040, v = 0}, i(.233, v = 0), {.1035, v = 21}
  yStart := yNew
// 235: ADD -> {.1041, v = 0}, i(.237, v = 0), {.1036, v = 1}
  boX := bnX
// 239: ADD -> {.1043, v = 0}, i(.241, v = 0), {.1038, v = 1}
  boY := bnY
// 243: MUL -> i(.244, v = 1), {.1042, v = 0}, {.1037, v = 10}
  oldHash := newHash
// 247: OUT -> {.1044, v = 0}
  print($nextBlock)
// 249: 0, JMP -> i(.250, v = 0), i(.251, v = 0)
  #goto 0
}
