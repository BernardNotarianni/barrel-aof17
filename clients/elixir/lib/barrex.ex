defmodule Barrex.Database do
 
  def open(url) do
    url
  end

  def get(docid, database_url) do
    url = database_url <> "/" <> docid
    headers = ["Content-type": "application/json"]
    %HTTPoison.Response{status_code: 200, body: body} = HTTPoison.get!(url, headers)
    {:ok, reply} = Poison.decode(body)
    reply
  end

  def post(doc, database_url) do
    url = database_url
    headers = ["Content-type": "application/json"]
    {:ok, json} = Poison.encode(doc)
    %HTTPoison.Response{status_code: 201, body: body} = HTTPoison.post!(url, json, headers)
    {:ok, reply} = Poison.decode(body)
    reply
  end

  def put(doc, database_url) do
    docid = doc["id"]
    url = database_url <> "/" <> docid
    headers = ["Content-type": "application/json"]
    {:ok, json} = Poison.encode(doc)
    %HTTPoison.Response{status_code: response_code, body: body} = HTTPoison.put!(url, json, headers)
    true = Enum.member?([200,201], response_code)
    {:ok, reply} = Poison.decode(body)
    reply
  end

  def delete(doc, database_url) do
    docid = doc["id"]
    rev = doc["_rev"]
    url = database_url <> "/" <> docid <> "?rev=" <> rev
    headers = ["Content-type": "application/json"]
    %HTTPoison.Response{status_code: 200, body: body} = HTTPoison.delete!(url, headers)
    {:ok, reply} = Poison.decode(body)
    reply
  end

  def changes(database_url) do
    Stream.resource(fn -> connect_changes(database_url) end,
                    fn(acc) -> recv_changes(acc) end,
                    fn(acc) -> end_changes(acc) end)
  end

  defp connect_changes(database_url) do
    headers = ["Content-type": "application/json"]
    options = [stream_to: self(), recv_timeout: 60000]
    url = database_url <> "/_changes?feed=eventsource"
    HTTPoison.get! url, headers, options
    database_url
  end

  defp recv_changes(acc) do
    receive do
      %HTTPoison.AsyncStatus{code: 200, id: _ref} ->
        recv_changes(acc)
      %HTTPoison.AsyncHeaders{headers: _headers, id: _ref} ->
        recv_changes(acc)
      %HTTPoison.AsyncChunk{chunk: chunk, id: _ref} ->
        database_url = acc
        [_id, data | _] = String.split chunk, "\n"
        json = String.slice(data, 6..-1)

        docs = Poison.decode!(json)
          |> Map.get("results")
          |> Enum.map(fn(change) ->
              docid = change["id"]
              get(docid, database_url)
          end) 
          
        {docs, acc}
      %HTTPoison.AsyncEnd{id: _} ->
        {:halt, acc}
      _ ->
        {:halt, acc}
    end
  end

  

  defp end_changes(_acc) do
    :ok
  end

end
