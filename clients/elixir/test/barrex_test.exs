defmodule BarrexTest do
  use ExUnit.Case

  test "the truth" do
    assert 1 + 1 == 2
  end
  
  test "get" do
    db = Barrex.Database.open("http://192.168.1.89:8080/source")
    IO.inspect Barrex.Database.get("chat", db)
  end

  test "post" do
    db = Barrex.Database.open("http://192.168.1.89:8080/source")
    doc = %{"name" => "john"}
    r = Barrex.Database.post(doc, db)
    id = r["id"]
    IO.inspect Barrex.Database.get(id, db)
  end

  test "put" do
    db = Barrex.Database.open("http://192.168.1.89:8080/source")
    doc = %{"id" => "lfklfk", "name" => "john"}
    Barrex.Database.put(doc, db)    
    doc2  = Barrex.Database.get("lfklfk", db)
    IO.inspect doc2
    IO.inspect Barrex.Database.delete(doc2, db)
  end
  
  test "aync" do
    db = Barrex.Database.open("http://192.168.1.89:8080/source")
    stream = Barrex.Database.changes(db)

    stream |> Stream.map(fn x -> IO.inspect x end) |> Stream.run
  end

end
