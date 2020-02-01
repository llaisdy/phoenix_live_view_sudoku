defmodule SudokuWeb.DemoLive do
  use Phoenix.LiveView

  def render(assigns) do
    ~L"""
    <form phx-change="maybe_valid_grid" phx-submit="maybe_solve">
      <div class="sudoku">
      <%= for i <- 1..9 do %>
        <div>
          <%= for j <- 1..9 do %>
            <input
	     pattern="[1-9]" maxlength="1" size="1" name="input[<%= i %>][<%= j %>]"
	     value="<%= sudoku_value(@sudoku, {i, j}) %>"
	     class="<%= sudoku_style(@sudoku, {i, j}) %>"
	     />
          <% end %>
        </div>
      <% end %>
      </div>

      <button>Solve</button>
      <p class="<%= @message_class %>"><%= @message %></p>
    </form>
    """
  end

  def sudoku_value(smap, key) do
      case Map.get(smap, key) do
        nil        -> ''
	{value, _} -> value
	value      -> value
      end
  end

  def sudoku_style(smap, key) do
      case Map.get(smap, key) do
	{_, style} -> style
	nil        -> 'empty'
	_          -> 'question'
      end
  end

  def mount(_session, socket) do
    sudoku = %{}

    {:ok,
     assign(socket,
       sudoku: sudoku,
       message: '',
       message_class: :ok
     )}
  end

  def handle_event("maybe_valid_grid", %{"input" => input}, socket) do
    smap = map_sudoku(input)

    {class, message} = ElixirPython.maybe_valid_grid(smap)
    {:noreply, assign(socket,
                      message: message,
	              message_class: class,
		      sudoku: smap)}
  end

  def handle_event("maybe_solve", %{"input" => input}, socket) do
    smap = map_sudoku(input)

    case ElixirPython.maybe_solution(smap) do
      {'ok', new_sudoku} ->
	{:noreply, assign(socket,
	    message: 'Solved!',
	    message_class: :ok,
	    sudoku: new_sudoku)}
      {'error', _} ->
	{:noreply, assign(socket,
	    message: 'No solutions!',
	    message_class: :error)}
    end
  end

  defp map_sudoku(input) do
      for {row_str, num_strs_by_col_str} <- input,
          {col_str, num_str} <- num_strs_by_col_str,
          num_str != "",
          row = String.to_integer(row_str),
          col = String.to_integer(col_str),
          num = String.to_integer(num_str),
          into: %{} do
        {{row, col}, num}
      end
  end

end
