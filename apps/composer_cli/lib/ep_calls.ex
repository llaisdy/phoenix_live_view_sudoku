defmodule ElixirPython do
  @moduledoc """
  Documentation for ElixirPython.
  """
  alias ElixirPython.Helper

  def maybe_solution(grid) do
    rules_fn = get_rules_fn()
    call_python(:proc, :maybe_solution, [grid, rules_fn])
  end

  def maybe_valid_grid(grid) do
    rules_fn = get_rules_fn()
    call_python(:proc, :maybe_valid_grid, [grid, rules_fn])
  end

  defp default_instance() do
    #Load all modules in our priv/python directory
    path = [:code.priv_dir(:composer_cli), "python"] 
          |> Path.join()
    Helper.python_instance(to_charlist(path))
  end

  # wrapper function to call python functions using
  # default python instance
  defp call_python(module, function, args \\ []) do
    default_instance()
    |> Helper.call_python(module, function, args)
  end

  defp get_rules_fn() do
    [:code.priv_dir(:composer_cli), "asp/sudoku9.lp"]
    |> Path.join()
  end
end
