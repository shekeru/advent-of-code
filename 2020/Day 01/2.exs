defmodule Day01 do
  def nCr([], _), do: []; def nCr(_, 0), do: [[]]
  def nCr([h|t], m), do: (for l <- nCr(t, m-1), do: [h|l]) ++ nCr(t, m)
  def solve(nums, {what, xt}) do
    v = Enum.find(nCr(nums, xt),
        fn xs -> 2020 == Enum.sum(xs) end)
      |> Enum.reduce(1, fn x, a -> x * a end)
    IO.puts "#{what}: #{v}" end
  def main do
    nums = File.read!("input.txt")
      |> String.split(~r/\R/, trim: true)
      |> Enum.map(&String.to_integer/1)
    [{"Silver", 2}, {"Gold", 3}] |>
      Enum.map(&solve(nums, &1)) end
end; Day01.main
