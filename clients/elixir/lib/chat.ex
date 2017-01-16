defmodule Barrex.Chat do

  @database_url "http://192.168.1.89:8080/source"
  @docid "chat"

  defp read_doc do
    db = Barrex.Database.open(@database_url)
    Barrex.Database.get(@docid, db)
  end

  def sender(url \\ @database_url) do
     db = Barrex.Database.open(url)
     read_send(db)
  end

  defp read_send(db) do
    message = IO.gets "Your message:"
    read_doc()
      |> Map.put("message", message)
      |> Barrex.Database.put(db)
    read_send(db)
  end

  def receiver(url \\ @database_url) do
    db = Barrex.Database.open(url)
    Barrex.Database.changes(db)
      |> Stream.map(fn doc -> IO.puts doc["message"] end)
      |> Stream.run
  end

end