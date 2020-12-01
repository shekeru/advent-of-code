defmodule Day01 do
  def nCr([], _), do: []
  def nCr(_, 0), do: [[]]
  def nCr([h|t], m) do
    (for l <- nCr(t, m-1), do: [h|l])
      ++ nCr(t, m)
  end
  def solve(what, nums, xt) do
    v = Enum.find(nCr(nums, xt),
        fn xs -> 2020 == Enum.sum(xs) end)
      |> Enum.reduce(1, fn x, a -> x * a end)
    "#{what}: #{v}"
  end
  def main do
    nums = File.read!("input.txt")
      |> String.split(~r/\R/, trim: true)
      |> Enum.map(&String.to_integer/1)
    solve("Silver", nums, 2) |> IO.puts
    solve("Gold", nums, 3) |> IO.puts
  end
end; Day01.main
