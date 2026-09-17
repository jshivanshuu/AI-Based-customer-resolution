import React, { useState } from 'react';
import { Send, Bot, User, Cpu, AlertTriangle } from 'lucide-react';

export default function ChatWindow({ messages, onSendMessage, thoughts, isProcessing }) {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim() || isProcessing) return;
    onSendMessage(input);
    setInput('');
  };

  return (
    <div className="chat-window-panel">
      <div className="panel-header">
        <Bot className="icon" />
        <div>
          <h2>AI Resolution Assistant</h2>
          <span className="subtitle">Real-time Policy Agent Orchestration</span>
        </div>
      </div>

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="empty-chat">
            <Bot className="empty-icon" />
            <p>Select a customer and issue a inquiry message to start resolution.</p>
          </div>
        ) : (
          messages.map((msg, index) => (
            <div key={index} className={`message-bubble ${msg.sender}`}>
              <div className="bubble-header">
                {msg.sender === 'user' ? <User className="avatar" /> : <Bot className="avatar" />}
                <span className="sender-name">{msg.sender === 'user' ? 'Customer' : 'AI Resolution Agent'}</span>
              </div>
              <p className="bubble-text">{msg.text}</p>
            </div>
          ))
        )}

        {thoughts && thoughts.length > 0 && (
          <div className="thoughts-container">
            <div className="thoughts-title">
              <Cpu className="mini-icon" /> Agent Reasoning Steps:
            </div>
            <ul>
              {thoughts.map((step, idx) => (
                <li key={idx}>{step}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <form className="chat-input-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type customer inquiry or issue description..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={isProcessing}
        />
        <button type="submit" disabled={isProcessing || !input.trim()}>
          <Send className="btn-icon" /> Send
        </button>
      </form>
    </div>
  );
}
