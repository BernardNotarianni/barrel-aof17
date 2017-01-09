var EventSource = require('eventsource');

var url = 'http://localhost:8080/source/_changes?feed=eventsource';
var es = new EventSource(url);

es.addEventListener('message', function (e) {
  console.log(e.data);
});
