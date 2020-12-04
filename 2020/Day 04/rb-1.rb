B, I = [
  /byr:(19[2-9]\d|200[0-2])/,
  /iyr:(201\d|2020)\b/,
  /eyr:(202\d|2030)\b/,
  /hgt:((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)\b/,
  /hcl:#[0-9a-f]{6}\b/,
  /ecl:(amb|blu|brn|gry|grn|hzl|oth)\b/,
  /pid:\d{9}\b/,
], File.read("input.txt").split("\n\n")
A = [/byr/, /iyr/, /eyr/, /hgt/, /hcl/, /ecl/, /pid/]

puts "Silver: #{I.count{|ln| A.all?{ln.match _1}}}",
  "Gold: #{I.count{|ln| B.all?{ln.match _1}}}"
