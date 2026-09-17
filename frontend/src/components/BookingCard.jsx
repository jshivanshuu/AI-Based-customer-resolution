import { bookings } from "../data";


function BookingCard({ customer }) {

    const customerBookings =
        bookings[customer.pnr] || [];


    return (
        <div className="booking-section">

            <div className="section-heading">

                <div>
                    <span className="eyebrow">
                        BOOKING
                    </span>

                    <h3>
                        Flight information
                    </h3>
                </div>

            </div>


            {customerBookings.map((booking, index) => (

                <div
                    className="booking-card"
                    key={index}
                >

                    <div className="booking-header">

                        <strong>
                            {booking.flight}
                        </strong>

                        <span
                            className={
                                booking.status === "Cancelled"
                                    ? "status cancelled"
                                    : booking.status === "Delayed"
                                        ? "status delayed"
                                        : "status unaffected"
                            }
                        >
                            {booking.status}
                        </span>

                    </div>


                    <div className="route">
                        {booking.route}
                    </div>


                    <div className="booking-info">

                        <div>
                            <span>Date</span>
                            <strong>{booking.date}</strong>
                        </div>

                        <div>
                            <span>Departure</span>
                            <strong>
                                {booking.departure}
                            </strong>
                        </div>


                        {booking.newDeparture && (

                            <div>
                                <span>New departure</span>
                                <strong>
                                    {booking.newDeparture}
                                </strong>
                            </div>

                        )}

                        {booking.delay && (

                            <div>
                                <span>Delay</span>
                                <strong>
                                    {booking.delay}
                                </strong>
                            </div>

                        )}

                    </div>


                    {booking.reason && (

                        <div className="booking-note">
                            Reason: {booking.reason}
                        </div>

                    )}

                </div>

            ))}

        </div>
    );
}


export default BookingCard;