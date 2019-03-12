import http.server
import socketserver
import termcolor

PORT = 8090

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
                in the HTTP protocol request"""

        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            with open("index.html", 'r') as f:
                contents = f.read()
        elif self.path == "/blue":
            with open("blue.html", 'r') as f:
                contents = f.read()
        elif self.path == "/pink":
            with open("pink.html", 'r') as f:
                contents = f.read()
        else:
            with open("error.html", 'r') as f:
                contents = f.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except:
        print()
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")