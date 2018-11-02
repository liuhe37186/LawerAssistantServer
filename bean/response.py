class ResponseBean(object):
    def __init__(self, code=0, msg='success', data=''):
        self._code = code
        self._msg = msg
        self._data = data
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, new_code):
        self._code = new_code

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, new_msg):
        self._msg = new_msg

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data