function CustomerProfile({ customer }) {

    return (
        <div className="profile-card">

            <div className="profile-top">

                <div className="large-avatar">
                    {customer.name
                        .split(" ")
                        .map(word => word[0])
                        .join("")
                    }
                </div>

                <div>
                    <h2>{customer.name}</h2>

                    <div className="profile-meta">

                        <span className="tier-badge">
                            {customer.tier}
                        </span>

                        <span>
                            PNR {customer.pnr}
                        </span>

                    </div>
                </div>

            </div>


            <div className="profile-details">

                <div className="detail-row">
                    <span>Email</span>
                    <strong>{customer.email}</strong>
                </div>

                <div className="detail-row">
                    <span>Phone</span>
                    <strong>{customer.phone}</strong>
                </div>

                <div className="detail-row">
                    <span>Flights · 12 months</span>
                    <strong>{customer.flights}</strong>
                </div>

                <div className="detail-row">
                    <span>Prior complaints</span>
                    <strong>{customer.complaints}</strong>
                </div>

            </div>

        </div>
    );
}


export default CustomerProfile;