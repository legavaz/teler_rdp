# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "192.168.21.145"
serverPort = 8888

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print('incoming call:',self.path)


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    print('CTRL+C - выход')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")