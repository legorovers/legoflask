"""
Really simple web server that just redirects requests on port 80
(from the captive portal) to https on port 5443 (webrover1)
"""
import BaseHTTPServer

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(301)
        s.send_header("Location", 'https://legorover.space:5443/')
        s.end_headers()
    def do_GET(s):
        s.do_HEAD()

if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 80), RedirectHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
