import React from 'react';
import { User, ShieldCheck, CreditCard, HeartPulse } from 'lucide-react';

export default function CustomerList({ customers, selectedCustomer, onSelectCustomer }) {
  return (
    <div className="customer-list-panel">
      <div className="panel-header">
        <User className="icon" />
        <h2>Customer Queue</h2>
      </div>
      <div className="customer-cards">
        {customers.map((cust, idx) => {
          const custKey = cust.pnr || cust.id || `cust-${idx}`;
          const isSelected = (selectedCustomer?.pnr && selectedCustomer.pnr === cust.pnr) || (selectedCustomer?.id && selectedCustomer.id === cust.id) || selectedCustomer?.name === cust.name;
          const tier = cust.loyalty_tier || cust.tier || 'Standard';
          return (
            <div
              key={custKey}
              className={`customer-card ${isSelected ? 'selected' : ''}`}
              onClick={() => onSelectCustomer(cust)}
            >
              <div className="card-top">
                <span className="customer-name">{cust.name}</span>
                <span className={`tier-badge tier-${tier.toLowerCase()}`}>
                  {tier}
                </span>
              </div>
              <div className="card-details">
                <span className="cust-id">PNR: {cust.pnr || cust.id}</span>
                <span className="cust-email">{cust.email}</span>
                {cust.phone && <span className="cust-phone">Phone: {cust.phone}</span>}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
