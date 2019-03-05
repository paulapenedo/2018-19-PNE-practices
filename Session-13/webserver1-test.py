import http.server
import socketserver

PORT = 8001


#we are going to create our own handler

class TestHandler(http.server.BaseHTTPRequestHandler):

    #just print a message
    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        content = "I am the happy server!"

        #for generating the status line
        self.send_response(200)
        self.send_header('Content-Type','text/plain')
        self.send_header('Content-Lenght', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    httpd.serve_forever()

#to check on internet localhost:PORT

