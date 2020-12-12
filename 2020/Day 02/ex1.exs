defmodule Day02 do
  def silver [a, b, [ch | _], pwd] do
    x = Enum.count(pwd, & ch == &1)
    a <= x && x <= b
  end
  def gold [a, b, [ch | _], pwd] do
    Enum.map([a, b], &Enum.at(pwd, &1 - 1)
      == ch) |> Enum.count(& &1) == 1
  end
  def input do
    parse = fn [a, b, ch, pwd] ->
      Enum.map([a, b], &String.to_integer/1)
      ++ Enum.map([ch, pwd], &to_charlist/1)
    end; File.stream!("input.txt")
      |> Stream.map(&Regex.scan(~r/\w+/, &1)
      |> List.flatten |> parse.()) |> Enum.to_list
  end
  def main do
    xvs = Day02.input
    IO.puts "Silver: #{Enum.count(xvs, &silver/1)}"
    IO.puts "Gold: #{Enum.count(xvs, &gold/1)}"
  end
end; Day02.main
