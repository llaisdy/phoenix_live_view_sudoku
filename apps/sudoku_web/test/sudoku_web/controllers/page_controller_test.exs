defmodule SudokuWeb.PageControllerTest do
  use SudokuWeb.ConnCase

  test "GET /", %{conn: conn} do
    conn = get(conn, "/")
    assert html_response(conn, 200) =~ "Xdoku Composer"
  end
end
