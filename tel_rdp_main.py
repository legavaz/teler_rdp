# https://github.com/legavaz/teler_rdp.git

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import tel_rdp_utils

setting     =   tel_rdp_utils.setting()
hostName    = setting.hostName
serverPort  = setting.serverPort

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