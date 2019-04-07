import http.server
import socketserver
import termcolor
from P7.Seq import Seq


# Define the Server's port
PORT = 8010


class TestHandler(http.server.BaseHTTPRequestHandler):
    def validSequence(self, s):
        valid = 'ACTG'
        for letter in s:
            if letter not in valid:
                return False
        return True

    def treat(self, seq, comand):
        print("Making comand", comand)
        if comand == "len":
            return seq.length()
        elif comand == "complement":
            return seq.complement().get_strbase()
        elif comand == "reverse":
            return seq.reverse().get_strbase()
        elif comand == "countA":
            return seq.count('A')
        elif comand == "countT":
            return seq.count('T')
        elif comand == "countG":
            return seq.count("G")
        elif comand == "countC":
            return seq.count("C")
        elif comand == "percA":
            return seq.perc("A")
        elif comand == "percT":
            return seq.perc("T")
        elif comand == "percG":
            return seq.perc("G")
        elif comand == "percC":
            return seq.perc("C")
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
            """<!DOCTYPE html>
                        <html lang ="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>SERVER RESPONSE</title>
                        </head>
                        <body style="background-color: pink">"""

            request = self.path.split('=')[1]
            pieces = request.split("&")
            chain = pieces[0]
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
                comand = operation + base
                answer = self.treat(seq, comand)
                contents = contents + "<p>Answer: " + str(answer) + "</p>"
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