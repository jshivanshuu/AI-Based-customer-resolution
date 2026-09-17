import React from 'react';
import { Zap, CheckCircle, Gift, RefreshCw, DollarSign } from 'lucide-react';

export default function ResolutionPanel({ actionProposal, onExecuteAction, isExecuting }) {
  if (!actionProposal) {
    return (
      <div className="resolution-panel empty">
        <Zap className="panel-icon" />
        <h3>Action Execution Panel</h3>
        <p>No automated resolution action pending.</p>
      </div>
    );
  }

  return (
    <div className="resolution-panel active">
      <div className="panel-header">
        <Zap className="icon pulse" />
        <h2>Proposed Resolution Action</h2>
      </div>

      <div className="action-details-card">
        <div className="action-header">
          <span className="action-type-tag">
            <DollarSign className="mini-icon" /> {actionProposal.action_type.toUpperCase()}
          </span>
          <span className="action-amount">${actionProposal.amount?.toFixed(2)}</span>
        </div>

        <p className="action-description">{actionProposal.details}</p>

        <div className="action-button-group">
          <button
            className="execute-btn"
            disabled={isExecuting}
            onClick={() => onExecuteAction(actionProposal)}
          >
            {isExecuting ? (
              <>
                <RefreshCw className="btn-icon spin" /> Executing Action...
              </>
            ) : (
              <>
                <CheckCircle className="btn-icon" /> Confirm & Execute Resolution
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
