import http.server
import socketserver
import termcolor

PORT = 8003

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")

        # print the request line
        termcolor.cprint(" " + self.requestline, 'green')

        # print the command received (should be GET)
        print(" Command: " + self.command)

        # print the resource request (the path)
        print(" Path: " + self.path)

        # in this simple server version we  are not generating any response message
        return

# set the new handler
Handler = TestHandler

# open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")