import sys
import os

# Add backend directory to sys.path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from tools.customer_tools import get_customer
from tools.booking_tools import get_booking
from tools.policy_tools import check_policy
from tools.action_tools import execute_action
from tools.escalation_tools import escalate_to_human
from services.policy_engine import resolve_policy, get_delay_policy, check_fare_difference
from fastapi.testclient import TestClient
from main import app

def run_tests():
    print("==========================================")
    print("RUNNING ALL COMPONENT & INTEGRATION TESTS")
    print("==========================================")
    
    passed = 0
    total = 0

    # 1. Customer Tools Test
    total += 1
    print("\n[Test 1] Testing Customer Tool (get_customer)...")
    c_res = get_customer.invoke({"pnr": "SK4821X"})
    if isinstance(c_res, dict) and c_res.get("pnr") == "SK4821X":
        print(f"  [PASS] Found Customer for PNR SK4821X: {c_res.get('name')}")
        passed += 1
    else:
        print(f"  [FAIL] {c_res}")

    # 2. Booking Tools Test
    total += 1
    print("\n[Test 2] Testing Booking Tool (get_booking)...")
    b_res = get_booking.invoke({"pnr": "SK4821X"})
    if isinstance(b_res, list) and len(b_res) > 0 and b_res[0].get("pnr") == "SK4821X":
        print(f"  [PASS] Found {len(b_res)} Booking(s) for SK4821X, status: {b_res[0].get('status')}")
        passed += 1
    else:
        print(f"  [FAIL] {b_res}")

    # 3. Policy Engine Test
    total += 1
    print("\n[Test 3] Testing Policy Engine (resolve_policy)...")
    customer_data = {"id": "CUST101", "name": "Arvind Kumar", "tier": "Gold"}
    bookings_data = [{"pnr": "SK4821X", "status": "Cancelled"}]
    p_res = resolve_policy("cancellation_refund", customer_data, bookings_data)
    if p_res.get("allowed") is True and p_res.get("action") == "refund":
        print("  [PASS] Cancellation refund policy allowed")
        passed += 1
    else:
        print(f"  [FAIL] {p_res}")

    # 4. Check Policy Tool Test
    total += 1
    print("\n[Test 4] Testing Policy Tool (check_policy)...")
    cp_res = check_policy.invoke({"intent": "cancellation_refund", "pnr": "SK4821X"})
    if isinstance(cp_res, dict) and cp_res.get("allowed") is True:
        print("  [PASS] check_policy tool returned allowed=True for cancellation_refund")
        passed += 1
    else:
        print(f"  [FAIL] {cp_res}")

    # 5. Delay Policy Test
    total += 1
    print("\n[Test 5] Testing Delay Policy (get_delay_policy)...")
    d_res = get_delay_policy(4)
    if d_res.get("meal_voucher") is True and d_res.get("lounge_access") is True:
        print("  [PASS] Delay policy for 4 hours correctly calculated (meal_voucher & lounge_access)")
        passed += 1
    else:
        print(f"  [FAIL] {d_res}")

    # 6. Action Tools Test
    total += 1
    print("\n[Test 6] Testing Action Tool (execute_action)...")
    a_res = execute_action.invoke({"action": "refund", "pnr": "SK4821X"})
    if isinstance(a_res, dict) and a_res.get("success") is True:
        print(f"  [PASS] Action tool executed refund successfully: {a_res.get('message')}")
        passed += 1
    else:
        print(f"  [FAIL] {a_res}")

    # 7. Escalation Tools Test
    total += 1
    print("\n[Test 7] Testing Escalation Tool (escalate_to_human)...")
    e_res = escalate_to_human.invoke({"pnr": "SK4821X", "reason": "Customer requested business class upgrade"})
    if isinstance(e_res, dict) and e_res.get("escalated") is True:
        print("  [PASS] Escalation tool recorded issue for human review")
        passed += 1
    else:
        print(f"  [FAIL] {e_res}")

    # 8. FastAPI Endpoint Integration Test - Root Health Check
    total += 1
    print("\n[Test 8] Testing FastAPI Health Check GET /...")
    client = TestClient(app)
    response = client.get("/")
    if response.status_code == 200 and "running" in response.json().get("message", ""):
        print("  [PASS] FastAPI Health Check GET / returned 200 OK")
        passed += 1
    else:
        print(f"  [FAIL] {response.status_code} - {response.text}")

    # 9. FastAPI Chat Endpoint Integration Test
    total += 1
    print("\n[Test 9] Testing FastAPI Chat Endpoint POST /chat...")
    payload = {
        "message": "My flight SK-204 was cancelled. Can I get a full refund?",
        "pnr": "SK4821X"
    }
    chat_resp = client.post("/chat", json=payload)
    if chat_resp.status_code == 200 and "response" in chat_resp.json():
        agent_out = chat_resp.json()['response']
        # Remove any non-ASCII characters for clean printing
        clean_out = agent_out.encode('ascii', 'ignore').decode('ascii')
        print(f"  [PASS] POST /chat returned 200 OK.")
        print(f"    Agent Response snippet: {clean_out[:120]}...")
        passed += 1
    else:
        print(f"  [FAIL] {chat_resp.status_code} - {chat_resp.text}")

    print("\n==========================================")
    print(f"RESULTS: {passed}/{total} TESTS PASSED")
    print("==========================================")

    if passed == total:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
