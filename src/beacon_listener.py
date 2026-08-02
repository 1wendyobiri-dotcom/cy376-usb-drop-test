import http.server
import socketserver
import datetime

PORT = 8000
LOGFILE = "beacon_log.txt"

class BeaconHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        timestamp = datetime.datetime.now().isoformat()
        client_ip = self.client_address[0]
        entry = f"{timestamp} | Trigger from {client_ip} | Path: {self.path}\n"
        with open(LOGFILE, "a") as f:
            f.write(entry)
        print(entry.strip())
        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()

with socketserver.TCPServer(("", PORT), BeaconHandler) as httpd:
    print(f"Listening on port {PORT}, logging to {LOGFILE}")
    httpd.serve_forever()
