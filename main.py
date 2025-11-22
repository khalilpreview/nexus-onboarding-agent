from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import time
import random
from datetime import datetime

app = FastAPI(title="Nexus Orchestration Engine")

# --- IN-MEMORY STATE ---
# We keep track of logs and stats here
state = {
    "total_calls": 142, # Start with a fake number so it looks used
    "tokens_saved": 4500,
    "active_agents": 1,
    "logs": [
        {"time": "09:00:01", "msg": "System initialized. Listening for Watsonx events..."},
        {"time": "09:15:22", "msg": "Connection established with Mock Identity Provider."},
    ]
}

# --- DATA MODELS ---
class BatchRequest(BaseModel):
    candidates: List[str]
    department: str

class LunchRequest(BaseModel):
    manager_email: str
    new_hire_name: str
    date: str = "Monday"

class ApprovalRequest(BaseModel):
    amount: str
    reason: str = "Standard Request"


class DeviceRequest(BaseModel):
    employee_email: str
    device_type: str = "MacBook Pro"


# --- THE FRONTEND (HTML/CSS/JS) ---
# We serve this as a single string to keep it simple for Replit
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Control Plane</title>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;600&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #161616;
            --card-bg: #262626;
            --text: #f4f4f4;
            --blue: #0F62FE;
            --teal: #009d9a;
            --red: #da1e28;
            --border: #393939;
        }
        body {
            margin: 0;
            padding: 0;
            font-family: 'IBM Plex Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            flex-direction: column;
            height: 100vh;
            overflow: hidden;
        }
        /* HEADER */
        header {
            background: #000;
            padding: 15px 30px;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .logo { font-weight: 600; font-size: 20px; letter-spacing: 1px; display: flex; align-items: center; gap: 10px; }
        .logo span { color: var(--blue); }
        .status { font-size: 12px; color: var(--teal); display: flex; align-items: center; gap: 5px; }
        .dot { width: 8px; height: 8px; background: var(--teal); border-radius: 50%; animation: blink 2s infinite; }

        /* LAYOUT */
        .container {
            display: flex;
            flex: 1;
            padding: 30px;
            gap: 30px;
        }
        .left-panel { flex: 2; display: flex; flex-direction: column; gap: 20px; }
        .right-panel { flex: 1; background: var(--card-bg); border: 1px solid var(--border); padding: 20px; display: flex; flex-direction: column; }

        /* STAT CARDS */
        .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .card {
            background: var(--card-bg);
            padding: 20px;
            border: 1px solid var(--border);
            border-left: 4px solid var(--blue);
        }
        .card-label { font-size: 12px; text-transform: uppercase; color: #a8a8a8; margin-bottom: 10px; }
        .card-value { font-size: 32px; font-weight: 300; }
        .card-value.green { color: #42be65; }

        /* TERMINAL */
        .terminal-window {
            flex: 1;
            background: #000;
            border: 1px solid var(--border);
            font-family: 'IBM Plex Mono', monospace;
            padding: 20px;
            overflow-y: auto;
            font-size: 13px;
            color: #00ff00;
        }
        .log-entry { margin-bottom: 5px; opacity: 0.8; }
        .log-time { color: #888; margin-right: 10px; }

        /* CHAT PREVIEW (RIGHT SIDE) */
        .chat-header { font-weight: 600; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px;}
        .chat-box { flex: 1; display: flex; flex-direction: column; gap: 15px; opacity: 0.7; }
        .msg { padding: 10px 15px; border-radius: 4px; font-size: 13px; max-width: 90%; }
        .msg.user { background: var(--blue); align-self: flex-end; color: white; }
        .msg.bot { background: #393939; align-self: flex-start; border-left: 3px solid var(--teal); }
        
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    </style>
</head>
<body>

    <header>
        <div class="logo">NEXUS <span>// ORCHESTRATOR</span></div>
        <div class="status"><div class="dot"></div> SYSTEM ONLINE</div>
    </header>

    <div class="container">
        <!-- LEFT: STATS & LOGS -->
        <div class="left-panel">
            <div class="stats-grid">
                <div class="card">
                    <div class="card-label">Total API Calls</div>
                    <div class="card-value" id="calls">0</div>
                </div>
                <div class="card">
                    <div class="card-label">Est. Tokens Saved</div>
                    <div class="card-value green" id="tokens">0</div>
                </div>
                <div class="card">
                    <div class="card-label">Active Workflows</div>
                    <div class="card-value" id="agents">1</div>
                </div>
            </div>

            <div class="terminal-window" id="terminal">
                <div class="log-entry">-- NEXUS BACKEND LOG STREAM --</div>
                <!-- Logs will appear here -->
            </div>
        </div>

        <!-- RIGHT: VISUAL CONTEXT -->
        <div class="right-panel">
            <div class="chat-header">Live Agent Preview</div>
            <div class="chat-box">
                <!-- This simulates what is happening in Watsonx -->
                <div class="msg user">Onboard John, Sarah, and Mike</div>
                <div class="msg bot">
                    <strong>Batch Process Initiated</strong><br>
                    <br>
                    Processing 3 candidates via vectorized API...<br>
                    ✅ Identities Created<br>
                    ✅ Slack Invites Sent
                </div>
                <div class="msg user">Book lunch for Monday</div>
                <div class="msg bot">
                    ⚠️ <strong>Conflict Detected</strong><br>
                    Manager is busy. Suggesting Tuesday at 12:30 PM.
                </div>
                <div style="margin-top: auto; font-size: 11px; color: #666; text-align: center;">
                    Waiting for next trigger from watsonx...
                </div>
            </div>
        </div>
    </div>

    <script>
        // --- REAL TIME UPDATE LOGIC ---
        
        function updateDashboard() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    // Update Numbers
                    document.getElementById('calls').innerText = data.total_calls;
                    document.getElementById('tokens').innerText = data.tokens_saved;
                    
                    // Update Logs
                    const term = document.getElementById('terminal');
                    term.innerHTML = '<div class="log-entry">-- NEXUS BACKEND LOG STREAM --</div>';
                    
                    // Reverse logs to show newest first, take top 20
                    data.logs.slice().reverse().forEach(log => {
                        const line = document.createElement('div');
                        line.className = 'log-entry';
                        line.innerHTML = `<span class="log-time">[${log.time}]</span> ${log.msg}`;
                        term.appendChild(line);
                    });
                });
        }

        // Poll every 1.5 seconds (Fast enough to look "Live")
        setInterval(updateDashboard, 1500);
        updateDashboard();
    </script>
</body>
</html>
"""

# --- ROUTES ---

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return html_code

@app.get("/api/stats")
def get_stats():
    return JSONResponse(state)

# --- HELPER TO ADD LOGS ---
def add_log(message: str):
    now = datetime.now().strftime("%H:%M:%S")
    state["logs"].append({"time": now, "msg": message})
    # Keep logs clean (last 50)
    if len(state["logs"]) > 50:
        state["logs"].pop(0)

# --- ACTION ENDPOINTS ---

@app.post("/batch-onboard")
def batch_onboard(request: BatchRequest):
    count = len(request.candidates)
    
    # Update Stats
    state['total_calls'] += 1
    # Formula: 3 people in 1 call = 2 calls saved * ~150 tokens per prompt context
    state['tokens_saved'] += (count * 150)
    
    add_log(f"⚡ BATCH TRIGGER: Onboarding {count} candidates for {request.department}")
    time.sleep(0.3) # Fake latency for realism
    add_log(f"✅ SUCCESS: Identity & Slack provisioning complete for {', '.join(request.candidates)}")
    
    processed = []
    for name in request.candidates:
        processed.append({"name": name, "status": "onboarded"})
        
    return {"status": "completed", "results": processed}

@app.post("/book-lunch")
def book_lunch(request: LunchRequest):
    state['total_calls'] += 1
    add_log(f"📅 CALENDAR: Requesting slot for {request.new_hire_name} on {request.date}")
    
    if "monday" in request.date.lower():
        add_log(f"⚠️ CONFLICT: Manager busy on Monday. Sending suggestion: Tuesday.")
        return {
            "status": "failed",
            "error": "Manager busy",
            "suggested_alternative": "Tuesday at 12:30 PM"
        }
    
    add_log(f"✅ BOOKED: Lunch confirmed for {request.date} at 12:00 PM")
    return {"status": "confirmed", "time": "12:00 PM"}

@app.post("/create-identity")
def create_id(request: dict):
    state['total_calls'] += 1
    add_log("🔑 IDENTITY: Single user credential generation requested.")
    return {"status": "ok"}

@app.post("/request-approval")
def request_approval(request: ApprovalRequest):
    state['total_calls'] += 1
    add_log(f"🛡️ GOVERNANCE: Budget exceeded ({request.amount}). Ticket #992 sent to CFO.")
    return {"status": "pending"}


@app.post("/order-device")
def order_device(request: DeviceRequest):
    # Update Dashboard Logs
    state['total_calls'] += 1
    add_log(f"📦 PROCUREMENT: Ordering {request.device_type} for {request.employee_email}")
    
    return {
        "status": "ordered", 
        "order_id": f"ORD-{random.randint(1000,9999)}",
        "eta": "2 business days"
    }
