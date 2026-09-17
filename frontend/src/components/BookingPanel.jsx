import React from 'react';
import { Calendar, Plane, Building, Car, AlertCircle, CheckCircle2 } from 'lucide-react';

export default function BookingPanel({ bookings, selectedBooking, onSelectBooking }) {
  const getIcon = (type) => {
    switch (type.toLowerCase()) {
      case 'flight': return <Plane className="booking-icon" />;
      case 'hotel': return <Building className="booking-icon" />;
      case 'car rental': return <Car className="booking-icon" />;
      default: return <Calendar className="booking-icon" />;
    }
  };

  return (
    <div className="booking-panel">
      <div className="panel-header">
        <Calendar className="icon" />
        <h2>Customer Bookings</h2>
      </div>

      <div className="booking-list">
        {bookings.length === 0 ? (
          <p className="no-bookings">No active bookings found for this customer.</p>
        ) : (
          bookings.map((booking, idx) => {
            const key = booking.flight + '-' + idx;
            const isSelected = (selectedBooking?.flight === booking.flight && selectedBooking?.route === booking.route) || selectedBooking?.id === booking.id;
            const title = booking.title || `${booking.flight} (${booking.route})`;
            const status = booking.status || 'Scheduled';
            return (
              <div
                key={key}
                className={`booking-card ${isSelected ? 'selected' : ''}`}
                onClick={() => onSelectBooking(booking)}
              >
                <div className="booking-top">
                  <div className="title-group">
                    <Plane className="booking-icon" />
                    <span className="booking-title">{title}</span>
                  </div>
                  <span className={`status-tag status-${status.toLowerCase()}`}>
                    {status}
                  </span>
                </div>

                <div className="booking-body">
                  <div className="info-row">
                    <span>Flight: {booking.flight}</span>
                    <span>Date: {booking.date || booking.booking_date}</span>
                  </div>
                  <div className="info-row highlight">
                    <span>Departure: {booking.departure} {booking.new_departure ? `→ New: ${booking.new_departure}` : ''}</span>
                    <span>
                      {booking.delay_hours ? (
                        <span className="delay-flag">
                          <AlertCircle className="mini-icon" /> {booking.delay_hours}h Delay
                        </span>
                      ) : booking.status === 'cancelled' ? (
                        <span className="delay-flag">
                          <AlertCircle className="mini-icon" /> Cancelled ({booking.cause})
                        </span>
                      ) : (
                        <span className="on-time-flag">
                          <CheckCircle2 className="mini-icon" /> Unaffected
                        </span>
                      )}
                    </span>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
