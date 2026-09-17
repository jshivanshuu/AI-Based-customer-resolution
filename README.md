# AI-Based Customer Resolution System

An intelligent, automated customer resolution framework powered by AI agents and deterministic policy enforcement. Designed to seamlessly manage customer support inquiries, evaluate booking eligibility, auto-issue resolutions (refunds, vouchers, rebookings), and escalate complex cases to human supervisors when necessary.

---

## 🏗 System Architecture

```
AI-Based-customer-resolution/
│
├── backend/                  # Python FastAPI application
│   ├── main.py               # REST API Server & WebSockets
│   ├── config.py             # System & environment configuration
│   ├── agent/                # Autonomous Agent logic & Prompts
│   │   ├── agent.py          # Orchestrator agent logic
│   │   ├── prompts.py        # Dynamic system instructions
│   │   └── schemas.py        # Pydantic data models
│   ├── tools/                # AI Agent Tools
│   │   ├── customer_tools.py # Customer lookup & loyalty data
│   │   ├── booking_tools.py  # Booking retrieval & modification
│   │   ├── policy_tools.py   # Business rules & policy checks
│   │   ├── action_tools.py   # Refund, rebook, voucher issuance
│   │   └── escalation_tools.py # Human handoff & alerts
│   ├── services/             # Deterministic engine services
│   │   └── policy_engine.py  # Refund & policy engine rules
│   └── data/                 # Data store mocks
│       ├── customers.json
│       └── bookings.json
│
├── frontend/                 # React UI Dashboard
│   ├── src/
│   │   ├── components/       # Modular UI components
│   │   │   ├── CustomerList.jsx
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── BookingPanel.jsx
│   │   │   ├── ResolutionPanel.jsx
│   │   │   └── EscalationAlert.jsx
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── App.css
│   └── package.json
│
├── .env                      # Local environment variables
├── .env.example              # Template environment config
├── docker-compose.yml        # Multi-container orchestrator
└── README.md                 # System Documentation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker & Docker Compose (optional)

### Running with Docker Compose
```bash
docker-compose up --build
```

### Running Locally

#### 1. Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate

pip install -r requirements.txt
python main.py
```
Backend server will run at: `http://localhost:8000`

#### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend app will run at: `http://localhost:5173`

---

## 🌟 Key Features
- **Smart Customer Lookup**: Instant access to customer profiles, tier statuses (VIP, Gold, Silver), and ticket histories.
- **Automated Policy Engine**: Deterministic rules evaluation for cancellation fees, full/partial refund eligibility, and compensation credit.
- **Interactive Agent Chat**: AI support assistant capable of tool calls, transparent step-by-step reasoning, and direct execution.
- **Action Execution**: Instant automated refunds, flight/hotel rebooking, and gesture voucher generation.
- **Human Escalation Guardrails**: Real-time safety triggers that highlight high-risk, multi-tier, or out-of-policy complaints for human agent review.
