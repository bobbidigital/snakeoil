import requests
import json

class Torrent(object):

    def __init__(self, location):
        self.file_location = location
        self.torrent_id = None
        self._name = ''

    @property
    def location(self):
        return self.file_location

    @location.setter
    def location(self, value):
        self.file_location = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class TransmissionDaemon(object):

    def __init__(self, host='localhost', port='9091'):


        self._session_id = None
        self.TORRENT_ADD = 'torrent-add'
        self.TORRENT_GET = 'torrent-get'
        self.TORRENT_PERCENT = 'percentDone'
        self.SESSION_HEADER = 'x-transmission-session-id'
        self.TORRENT_NAME = 'name'
        self._host = host
        self._port = port
        self.FILENAME = 'filename'
        self.URI_SCHEME = 'http'
        self.BASE_URL = '%s://%s:%s/transmission/rpc' % (self.URI_SCHEME,
                host, port)
        self._initial_header_set()

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    def _initial_header_set(self):
        response = self.status()
        response = self.status()

    def add_torrent(self, torrent):
        rpc_request =  {'method': self.TORRENT_ADD }
        arguments = { self.FILENAME: torrent.location }
        rpc_request['arguments'] = arguments
        rpc_response = self.__submit(rpc_request)
        return rpc_response

    def status(self):
        rpc_request = { 'method': self.TORRENT_GET }
        arguments = { 'fields': [ self.TORRENT_NAME, self.TORRENT_PERCENT] }
        rpc_request['arguments'] = arguments
        response = self.__submit(rpc_request)
        return response

    def __rpc_call(self,request_dict):
        headers = { 'content-type': 'application/json',
            self.SESSION_HEADER: self.session_id}
        response = requests.post(self.BASE_URL,
            data=json.dumps(request_dict), headers=headers)
        return response


    def __submit(self, request_dict):
        try:
            response = self.__rpc_call(request_dict)
            if response.status_code == requests.codes.ok:
                result = json.loads(response.text)
            elif response.status_code == requests.codes.conflict:
                self.session_id = response.headers[self.SESSION_HEADER]
                result = self.__submit(request_dict)
            else:
                msg = 'Returned status code %s' % response.status_code
                result = {'result': 'failed', 'arguments': {'error': msg}}
            return result

        except BaseException as ex:
            result = {'result': 'failed', 'arguments': {'error': str(ex)}}
            return result

