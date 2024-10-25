# Use this to receive log from malpkd2
#   python3 receiver.py

from http.server import BaseHTTPRequestHandler, HTTPServer 
import logging

# Web server that implement GET and POST
class PyConServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
    
    # decoy, give blank page
    def do_GET(self):
        self._set_response()
        self.wfile.write(b"")

    # log the POST request
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length)
        logging.info(
            "[POST] path: %s\nHeaders:\n%s\n\nBody:\n%s\n", 
            str(self.path), 
            str(self.headers), 
            data.decode("utf-8")
        )

        self._set_response()
        self.wfile.write(f"{len(data)} received".encode())


def run(server_class=HTTPServer, handler_class=PyConServer, port=8080):
    logging.basicConfig(level=logging.INFO)

    address = ("", port)
    httpd = server_class(address, handler_class)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass 

    httpd.server_close()


if __name__ == "__main__":
    from sys import argv 

    print("Running receiver")

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()