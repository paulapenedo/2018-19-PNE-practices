import http.server
import socketserver
import termcolor

PORT = 8006


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            with open("echo.html", "r") as f:
                contents = f.read()
        elif "echo?msg=" in self.path:
            parameters = self.path.split('?')[1].split('&')
            words = parameters[0].split('=')[1].split('+')
            msg = " ".join(words)

            if len(parameters) > 1:
                msg = msg.upper()

            contents = '''
                    <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="UTF-8">
                                <title>FORM 1</title>
                            </head>
                            <body>
                                <h1>Echo from the message received</h1>
                    <p>''' + msg + '''</p>
                                <a href= "/">Main Page</a>
                            
                            </body>
                            </html>
            '''
        else:
            with open("error.html", "r") as f:
                contents = f.read()

        # Open the form1.html file
        # f = open("form_ex1.html", 'r')
        # contents = f.read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
