import { bookings } from "../data";


function ResolutionPanel({ customer }) {

    const customerBookings =
        bookings[customer.pnr] || [];

    const primaryBooking =
        customerBookings[0];


    const isCancelled =
        primaryBooking?.status === "Cancelled";

    const isDelayed =
        primaryBooking?.status === "Delayed";


    return (

        <div className="resolution-panel">

            <div className="panel-heading">

                <div>

                    <span className="eyebrow">
                        RESOLUTION
                    </span>

                    <h3>
                        Case overview
                    </h3>

                </div>

                <span className="live-badge">
                    LIVE
                </span>

            </div>


            <div className="resolution-status">

                <div className="resolution-icon">
                    {isCancelled ? "!" : "✓"}
                </div>

                <div>

                    <span>
                        Flight status
                    </span>

                    <strong>
                        {primaryBooking?.status}
                    </strong>

                </div>

            </div>


            {isCancelled && (

                <div className="resolution-block">

                    <div className="block-title">
                        Cancellation options
                    </div>

                    <div className="option">

                        <div>
                            <strong>
                                Full refund
                            </strong>

                            <span>
                                Processed within 7 business days
                            </span>
                        </div>

                        <span className="eligible">
                            Eligible
                        </span>

                    </div>


                    <div className="option">

                        <div>
                            <strong>
                                Free rebooking
                            </strong>

                            <span>
                                Next available flight within 24h
                            </span>
                        </div>

                        <span className="eligible">
                            Eligible
                        </span>

                    </div>

                </div>

            )}


            {isDelayed && (

                <div className="resolution-block">

                    <div className="block-title">
                        Delay entitlements
                    </div>

                    <div className="entitlement">
                        <span>Meal voucher</span>
                        <strong>₹500</strong>
                    </div>

                    {primaryBooking.delay === "4h" && (

                        <>
                            <div className="entitlement">
                                <span>Lounge access</span>
                                <strong>Included</strong>
                            </div>

                            <div className="not-eligible">
                                Hotel accommodation is not covered
                                for this delay duration.
                            </div>
                        </>

                    )}


                    {primaryBooking.delay === "6h" && (

                        <div className="entitlement">

                            <span>
                                Hotel accommodation
                            </span>

                            <strong>
                                Delayed hours only
                            </strong>

                        </div>

                    )}

                </div>

            )}


            <div className="policy-note">

                <span>ⓘ</span>

                <p>
                    Loyalty status provides priority rebooking
                    for Gold and Platinum customers, but does
                    not add compensation beyond standard policy.
                </p>

            </div>

        </div>
    );
}


export default ResolutionPanel;