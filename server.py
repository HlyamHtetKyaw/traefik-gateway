# server.py
import http.server
import socketserver
import sys

# Get port from command line argument
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # The HTML "UI" showing the instance details
        html = f"""
        <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 50px;">
            <div style="border: 2px solid #333; display: inline-block; padding: 20px; border-radius: 10px; background-color: #f0f0f0;">
                <h1>📖 Visitor GuestBook</h1>
                <hr>
                <p>✅ <strong>Status:</strong> Online</p>
                <p>⚙️ <strong>Served by Instance:</strong> <span style="color: blue; font-size: 1.5em;">Port {PORT}</span></p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
