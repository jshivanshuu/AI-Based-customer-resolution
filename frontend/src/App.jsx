import React, { useState, useEffect } from 'react';
import CustomerList from './components/CustomerList';
import ChatWindow from './components/ChatWindow';
import BookingPanel from './components/BookingPanel';
import ResolutionPanel from './components/ResolutionPanel';
import EscalationAlert from './components/EscalationAlert';
import { fetchCustomers, fetchBookings, sendChatMessage, executeRefundAction } from './api';
import { Bot, RefreshCw, Layers } from 'lucide-react';
import './App.css';

export default function App() {
  const [customers, setCustomers] = useState([]);
  const [selectedCustomer, setSelectedCustomer] = useState(null);
  const [bookings, setBookings] = useState([]);
  const [selectedBooking, setSelectedBooking] = useState(null);

  const [messages, setMessages] = useState([]);
  const [thoughts, setThoughts] = useState([]);
  const [actionProposal, setActionProposal] = useState(null);
  const [escalated, setEscalation] = useState(false);

  const [loading, setLoading] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [isExecuting, setIsExecuting] = useState(false);

  useEffect(() => {
    loadCustomers();
  }, []);

  useEffect(() => {
    if (selectedCustomer) {
      loadBookingsForCustomer(selectedCustomer.id);
      setMessages([]);
      setThoughts([]);
      setActionProposal(null);
      setEscalation(false);
    }
  }, [selectedCustomer]);

  const loadCustomers = async () => {
    try {
      setLoading(true);
      const data = await fetchCustomers();
      setCustomers(data);
      if (data.length > 0) {
        setSelectedCustomer(data[0]);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const loadBookingsForCustomer = async (custID) => {
    try {
      const data = await fetchBookings(custID);
      setBookings(data);
      if (data.length > 0) {
        setSelectedBooking(data[0]);
      } else {
        setSelectedBooking(null);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleSendMessage = async (text) => {
    if (!selectedCustomer) return;

    const userMsg = { sender: 'user', text };
    setMessages((prev) => [...prev, userMsg]);
    setIsProcessing(true);

    try {
      const response = await sendChatMessage(
        selectedCustomer.id,
        selectedBooking?.id,
        text,
        messages
      );

      const agentMsg = { sender: 'agent', text: response.response_text };
      setMessages((prev) => [...prev, agentMsg]);
      setThoughts(response.thought_process || []);
      setActionProposal(response.action_proposal || null);
      setEscalation(response.escalated || false);
    } catch (err) {
      console.error(err);
      setMessages((prev) => [
        ...prev,
        { sender: 'agent', text: 'Error connecting to resolution backend agent.' }
      ]);
    } finally {
      setIsProcessing(false);
    }
  };

  const handleExecuteAction = async (proposal) => {
    if (!selectedBooking) return;
    setIsExecuting(true);
    try {
      const res = await executeRefundAction(selectedBooking.id, proposal.amount, proposal.details);
      setMessages((prev) => [
        ...prev,
        { sender: 'system', text: `Action Executed: ${res.message}` }
      ]);
      setActionProposal(null);
    } catch (err) {
      console.error(err);
    } finally {
      setIsExecuting(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="logo-group">
          <Bot className="logo-icon" />
          <h1>AI-Based Customer Resolution Dashboard</h1>
        </div>
        <div className="header-meta">
          <span className="status-indicator online">System Active</span>
          <button className="refresh-btn" onClick={loadCustomers}>
            <RefreshCw className="btn-icon" /> Refresh Data
          </button>
        </div>
      </header>

      <EscalationAlert escalated={escalated} />

      <main className="dashboard-grid">
        <section className="column-left">
          <CustomerList
            customers={customers}
            selectedCustomer={selectedCustomer}
            onSelectCustomer={setSelectedCustomer}
          />
        </section>

        <section className="column-center">
          <ChatWindow
            messages={messages}
            onSendMessage={handleSendMessage}
            thoughts={thoughts}
            isProcessing={isProcessing}
          />
        </section>

        <section className="column-right">
          <BookingPanel
            bookings={bookings}
            selectedBooking={selectedBooking}
            onSelectBooking={setSelectedBooking}
          />
          <ResolutionPanel
            actionProposal={actionProposal}
            onExecuteAction={handleExecuteAction}
            isExecuting={isExecuting}
          />
        </section>
      </main>
    </div>
  );
}
