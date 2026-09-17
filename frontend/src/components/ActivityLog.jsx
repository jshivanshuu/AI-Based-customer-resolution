function ActivityLog({ resolution }) {

    return (

        <div className="activity-card">

            <div className="panel-heading">

                <div>
                    <span className="eyebrow">
                        AGENT ACTIVITY
                    </span>

                    <h3>
                        Resolution process
                    </h3>
                </div>

            </div>


            <div className="activity-list">

                <div className="activity-item">
                    <span className="activity-icon">
                        ✓
                    </span>

                    <div>
                        <strong>
                            Customer verified
                        </strong>

                        <span>
                            Identity matched with PNR
                        </span>
                    </div>
                </div>


                <div className="activity-item">
                    <span className="activity-icon">
                        ✓
                    </span>

                    <div>
                        <strong>
                            Booking retrieved
                        </strong>

                        <span>
                            Flight information loaded
                        </span>
                    </div>
                </div>


                <div className="activity-item">
                    <span className="activity-icon">
                        ✓
                    </span>

                    <div>
                        <strong>
                            Policy evaluated
                        </strong>

                        <span>
                            Request checked against policy
                        </span>
                    </div>
                </div>


                {resolution && (

                    <div className="activity-item current">

                        <span className="activity-icon">
                            →
                        </span>

                        <div>
                            <strong>
                                Agent response generated
                            </strong>

                            <span>
                                Resolution returned to customer
                            </span>
                        </div>

                    </div>

                )}

            </div>

        </div>
    );
}


export default ActivityLog;