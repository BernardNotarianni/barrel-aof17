var request = require('request');

store = 'http://localhost:8080/source';

console.log("post a document");
doc = {name: 'tom'};

request.post(
  store,
  { json: doc },
  function (error, response, body) {
    if (!error && response.statusCode == 201) {
      console.log('got the reply: ');
      console.log(body);
      docid = body.id;
      request.get(store + '/' + docid);
    }
  }
);
