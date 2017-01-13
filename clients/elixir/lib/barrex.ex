defmodule Barrex do

  def hello do
    method = :get
    url = "https://friendpaste.com"
    headers = []
    payload = <<>>
    options = []

    :io.format "~p", [:hackney.request(method, url, headers, payload, options)]
  end
end
