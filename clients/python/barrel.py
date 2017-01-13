import re
import requests
import json
import sseclient


class Database:

    def __init__(self, url):
        """Open the database at the given url."""
        self.url = url
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('Barrel-db database not available at ' + url)

    def get(self, docid):
        r = requests.get(self.url + '/' + docid)
        if r.status_code != 200:
            return None
        return r.json()

    def post(self, doc):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.url, headers=headers, data=json.dumps(doc))
        return r.json()

    def put(self, doc):
        headers = {'Content-Type': 'application/json'}
        docid = doc['id']
        url = self.url + '/' + docid
        r = requests.put(url, headers=headers, data=json.dumps(doc))
        return r.json()

    def delete(self, docid, rev):
        url = self.url + '/%s?rev=%s' % (docid, rev)
        r = requests.delete(url)
        return r.json()

    def list(self):
        url = self.url + '/_all_docs'
        r = requests.get(url)
        if r.status_code != 200:
            return None
        j = r.json()
        result = []
        for ref in j['rows']:
            docid = ref['id']
            result.append(docid)
        return result

    def changes(self, regex=None):
        """A stream of document modified on the database.

        The regex parameter can be used to provide a filter on documents id.
        Examples:
        - changes('^chat') streams docs with id starting with 'chat'
        """
        url = self.url + '/_changes?feed=eventsource'

        response = requests.get(url, stream=True)
        client = sseclient.SSEClient(response)

        for event in client.events():
            j = json.loads(event.data)

            for d in j['results']:
                id = d['id']
                if regex is not None:
                    if not re.match(regex, id):
                        continue
                doc = self.get(d['id'])
                yield doc
