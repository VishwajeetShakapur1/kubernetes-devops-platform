import json, os, time
from http.server import BaseHTTPRequestHandler, HTTPServer

REQUESTS = 0
ERRORS = 0

def log(message, level="INFO"):
    print(json.dumps({
        "service":"order-service","level":level,
        "message":message,"timestamp":time.time()
    }), flush=True)

class Handler(BaseHTTPRequestHandler):
    def reply(self, code, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        global REQUESTS, ERRORS
        REQUESTS += 1

        if self.path == "/health":
            return self.reply(200, {"status":"ok"})
        if self.path == "/ready":
            return self.reply(200, {"status":"ready"})
        if self.path == "/metrics":
            metrics = f"""# HELP app_requests_total Total application requests
# TYPE app_requests_total counter
app_requests_total {REQUESTS}
# HELP app_errors_total Total application errors
# TYPE app_errors_total counter
app_errors_total {ERRORS}
"""
            return self.reply(200, metrics.encode(),
                              "text/plain; version=0.0.4")
        if self.path == "/fail":
            ERRORS += 1
            log("simulated application failure", "ERROR")
            return self.reply(500, {"error":"simulated failure"})

        started=time.time()
        time.sleep(0.01)
        log(f"request completed path={self.path} duration_ms={round((time.time()-started)*1000,2)}")
        self.reply(200, {"service":"order-service","status":"accepted"})

    def log_message(self, fmt, *args):
        return

if __name__ == "__main__":
    port=int(os.getenv("PORT","8080"))
    log(f"starting order-service on port {port}")
    HTTPServer(("0.0.0.0",port),Handler).serve_forever()
