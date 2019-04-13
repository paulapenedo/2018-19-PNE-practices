import http.server
import socketserver
import termcolor
from P6.Seq import Seq


# Define the Server's port
PORT = 8010


class TestHandler(http.server.BaseHTTPRequestHandler):
    def validSequence(self, s):
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def process_command(self, seq, command, base):
        print("Making comand", command)
        if command == "c":
            return str(seq.count(base))
        elif command == "p":
            return str(seq.perc(base)) + "%"
        else:
            return "ERROR"

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/":
            f = open("main_page.html", 'r')
            contents = f.read()
            f.close()
        elif '/seq' in self.path:
            contents = """<!DOCTYPE html>
                        <html lang ="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>SERVER RESPONSE</title>
                        </head>
                        <body style="background-color: pink">"""

            request = self.path.split('=')[1]
            pieces = request.split("&")
            chain = pieces[0].upper()
            contents = contents + "<p>Sequence: " + chain + "</p>"

            if self.validSequence(chain):
                seq = Seq(chain)
                if 'lenCheck=on' in self.path:
                    length = seq.len()
                    contents = contents + "<p>Length: " + str(length) + "</p>"
                operation = self.path.split('operation=')[1].split("&")[0]
                contents = contents + "<p>Operation: " + operation + "</p>"
                base = self.path.split('base=')[1].split("&")[0]
                contents = contents + "<p>Base: " + base + "</p>"
                answer = self.process_command(seq, operation, base)
                contents = contents + "<p>Result: " + str(answer) + "</p>"
            else:
                contents = contents + "<p>No Valid</p>"

            contents = contents+"""<br> <a href="/"> [Main page] </a>
            </body></html>"""

        else:
            print("error detected")
            f = open("error.html", 'r')
            contents = f.read()

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
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")