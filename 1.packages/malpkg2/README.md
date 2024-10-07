# Malicious Package Example

This package is used to demonstrate common tricks by threat actor to masquerade malicious code.

## Malpkg 2: Malicious Setup

Malicious code is inserted at the end of `setup.py` file.

The code will be executed as part of installation process by package manager (ie: pip). Specifically, it create an install hook that will be executed during installation.

The payload will find `.env` file and send the content to attacker-controlled server.

## Usage

To test locally, first setup a HTTP server that accept POST request.

```python
# file: server.py
from http.server import BaseHTTPRequestHandler, HTTPServer 

class S(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(f"POST: '{data}'")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

httpd = HTTPServer(("127.0.0.1",80), S)
httpd.serve_forever()
```

then run the script to start the server.

```sh
python3 server.py
```

create a `.env` in any of the following path: 
- ~/.env
- /.env

use following command for building and installing

```sh
python3 setup.py sdist
pip install dist/malpkg2-0.1.0.tar.gz
```

during `pip install`, you should see one or more POST request to the server.