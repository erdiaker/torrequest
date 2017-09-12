TorRequest
==========

A simple Python interface for HTTP(s) requests over
[Tor](https://www.torproject.org). 
```python
from torrequest import TorRequest

with TorRequest() as tr:
  response = tr.get('http://ipecho.net/plain')
  print(response.text)  # not your IP address
```

It's basically a wrapper around [Stem](https://stem.torproject.org) and
[Requests](http://docs.python-requests.org/en/master/) libraries.

## Dependencies
You need Tor. It's available via Homebrew.
```sh
brew install tor
```

After installation, you may want to configure Tor by creating a `.torrc` file in your `$HOME` directory. More information is available on [Tor
documentation](https://www.torproject.org/docs/tor-manual.html.en).

## Installation
After installing dependencies, you can install `torrequest` via PyPI:
```sh
pip install torrequest
```

## Examples
```python
from torrequest import TorRequest

# Choose a proxy port, a control port, and a password. 
# Defaults are 9050, 9051, and None respectively. 
# If there is already a Tor process listening the specified 
# ports, TorRequest will use that one. 
# Otherwise, it will create a new Tor process, 
# and terminate it at the end.
with TorRequest(proxy_port=9050, ctrl_port=9051, password=None) as tr:

  # Specify HTTP verb and url.
  resp = tr.get('http://google.com')
  print(resp.text)

  # Send data. Use basic authentication.
  resp = tr.post('https://api.example.com', 
    data={'foo': 'bar'}, auth=('user', 'pass'))'
  print(resp.json)

  # Change your Tor circuit,
  # and likely your observed IP address.
  tr.reset_identity()

  # TorRequest object also exposes the underlying Stem controller 
  # and Requests session objects for more flexibility.

  print(type(tr.ctrl))            # a stem.control.Controller object
  tr.ctrl.signal('CLEARDNSCACHE') # see Stem docs for the full API

  print(type(tr.session))         # a requests.Session object
  c = cookielib.CookieJar()
  tr.session.cookies.update(c)    # see Requests docs for the full API
```

## License
MIT

