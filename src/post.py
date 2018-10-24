from http.server import  HTTPServer,  BaseHTTPRequestHandler
import urllib

messagehtml = """ <!DOCTYPE html>
            <title>Message Board</title>
            <form method="POST" action="http://localhost:8000/">
            <textarea name="message"></textarea>
            <br>
            <button type="submit">Post it!</button>
            </form>"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(messagehtml.encode())

    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode()
        query = urllib.parse.parse_qs(data)['message'][0]
        message = "<li>{}</li>".format
        self.send_response(303)
        self.send_header('Location','/')
        self.end_headers()





if __name__ == '__main__':
    server_address = ('',8000)
    httpd = HTTPServer(server_address,handler)
    httpd.serve_forever()