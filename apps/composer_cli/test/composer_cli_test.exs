defmodule ComposerCliTest do
  use ExUnit.Case
  doctest ComposerCli

  test "Detects invalid grid." do
    assert ElixirPython.maybe_solution(gridbad1()) == {'error', %{}}
  end

  test "Good grid has 81 elements." do
    {'ok', grid} = ElixirPython.maybe_solution(gridok1())
    assert map_size(grid) == 81
  end

  test "Invalid grid has no solutions." do
    assert ElixirPython.maybe_valid_grid(gridbad1()) ==
    {'error', 'No solutions found.'}
  end

  test "Valid grid has 100+ solutions." do
    assert ElixirPython.maybe_valid_grid(gridok1()) ==
    {'ok', '100+ solutions found.'}
  end

  defp gridok1 do
    %{{1,1} => 1, {1,2} => 3}
  end

  defp gridbad1 do
    %{{1,1} => 1, {1,2} => 1}
  end
end
