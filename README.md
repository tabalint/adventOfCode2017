# adventOfCode2017

`# Week 1: WILL BE MOVING THIS TO ITS OWN FILE WHEN I GET HOME`
`# Part 1`
`sum = 0`
`lastChar=myString[len(myString)-1]`
`for char in myString:`
`  if char == lastChar:`
`    sum += int(lastChar)`
`  lastChar = char`

`print sum`

`# Part 2`
`sum2 = 0`
`myStringFirstHalf = myString[:len(myString)/2]`
`myStringSecondHalf = myString[len(myString)/2:]`
`for a in range(len(myStringFirstHalf)):`
`  if myStringFirstHalf[a] == myStringSecondHalf[a]:`
`    sum2 += 2*int(myStringFirstHalf[a])`

`print sum2`
