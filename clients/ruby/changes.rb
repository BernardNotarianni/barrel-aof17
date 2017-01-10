require "em-eventsource"

url = "http://localhost:8080/source/_changes?feed=eventsource"

EM.run do
  source = EventMachine::EventSource.new(url)
  source.message do |message|
    puts "new message #{message}"
  end
  source.start # Start listening
end
