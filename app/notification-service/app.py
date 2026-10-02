import json, os, time
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/health","/ready"):
            body={"status":"ok"}
        else:
            time.sleep(0.02)
            body={"service":"notification-service","status":"processed"}
        data=json.dumps(body).encode()
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    def log_message(self,fmt,*args):
        print(json.dumps({"service":"notification-service","message":fmt % args}),flush=True)
if __name__=="__main__":
    HTTPServer(("0.0.0.0",8082),Handler).serve_forever()
