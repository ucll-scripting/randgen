import pkg_resources




def _load_resource(id):
    stream = pkg_resources.resource_stream(__name__, f'data/{id}.txt')
    return stream


def _load_strings(id):
    return [ line.decode('utf-8').strip() for line in _load_resource(id).readlines() ]


def first_names():
    return _load_strings('fnames')


def last_names():
    return _load_strings('lnames')


def english_words():
    return _load_strings('english')


def lowercase_alphabet():
    return 'abcdefghijklmnopqrstuvwxyz'


def uppercase_alphabet():
    return lowercase_alphabet().upper()
