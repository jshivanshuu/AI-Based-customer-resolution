const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export async function fetchCustomers() {
  const res = await fetch(`${API_BASE_URL}/api/customers`);
  if (!res.ok) throw new Error('Failed to fetch customers');
  return res.json();
}

export async function fetchBookings(customerId) {
  const url = customerId 
    ? `${API_BASE_URL}/api/bookings?customer_id=${encodeURIComponent(customerId)}`
    : `${API_BASE_URL}/api/bookings`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to fetch bookings');
  return res.json();
}

export async function sendChatMessage(customerId, bookingId, message, history = []) {
  const res = await fetch(`${API_BASE_URL}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      customer_id: customerId,
      booking_id: bookingId,
      message,
      history
    })
  });
  if (!res.ok) throw new Error('Failed to process message');
  return res.json();
}

export async function executeRefundAction(bookingId, amount, reason) {
  const res = await fetch(`${API_BASE_URL}/api/actions/refund?booking_id=${encodeURIComponent(bookingId)}&amount=${amount}&reason=${encodeURIComponent(reason)}`, {
    method: 'POST'
  });
  if (!res.ok) throw new Error('Failed to execute refund');
  return res.json();
}

export async function fetchEscalations() {
  const res = await fetch(`${API_BASE_URL}/api/escalations`);
  if (!res.ok) throw new Error('Failed to fetch escalations');
  return res.json();
}
