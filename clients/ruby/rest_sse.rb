require "em-eventsource"

EM.run do
  source = EventMachine::EventSource.new("http://localhost:8080/source/_changes?feed=evensource")
  source.message do |message|
    puts "new message #{message}"
  end
  source.start # Start listening
end
