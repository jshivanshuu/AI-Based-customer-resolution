import React from 'react';
import { AlertTriangle, ShieldAlert, ArrowUpRight } from 'lucide-react';

export default function EscalationAlert({ escalated, details }) {
  if (!escalated) return null;

  return (
    <div className="escalation-alert-banner">
      <div className="alert-content">
        <ShieldAlert className="alert-icon" />
        <div>
          <h3>Human Supervisor Handoff Triggered</h3>
          <p>{details || 'This ticket requires manual supervisor review due to risk parameters or policy boundaries.'}</p>
        </div>
      </div>
      <button className="escalation-action-btn">
        View Supervisor Queue <ArrowUpRight className="btn-icon" />
      </button>
    </div>
  );
}
