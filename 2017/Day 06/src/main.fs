module Solution
// Namespaces
open Microsoft.FSharp.Collections
open System.Collections.Generic
open System.IO
// Main has to be last, that nigger
let show table = 
    for n in table do
        printf "%d " n
    printfn ""

let encode table = 
    let mutable y = 1
    for x in table do
        y <- 17 * y + x
    y
// Utter Fucking Aids to Setup
[<EntryPoint>]
let main argv = 
    let seen, table = 
        new List<int>(), File.ReadAllLines "src/input.txt" |> 
            Array.head |> fun x -> x.Split '\t' |> Array.map int
    while seen.Contains(encode table) |> not do
        let mutable i,v = Array.indexed table |> Array.maxBy snd
        seen.Add(encode table)
        let len = table.Length
        table.[i] <- 0
        while v > 0 do
            i <- (i + 1) % len
            table.[i] <- table.[i] + 1
            v <- v - 1
    printfn "Silver: %d" seen.Count
    printfn "Gold: %d" <| seen.Count -
        seen.IndexOf(encode table)
    0
