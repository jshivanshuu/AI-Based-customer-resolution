import { customers } from "../data";


function Sidebar({ selectedCustomer, onSelectCustomer }) {

    return (
        <aside className="sidebar">

            <div className="brand">
                <div className="brand-icon">✈</div>

                <div>
                    <h2>AEROLINE</h2>
                    <span>Resolution Desk</span>
                </div>
            </div>


            <div className="sidebar-section">

                <div className="section-title">
                    CUSTOMERS
                </div>


                <div className="customer-list">

                    {customers.map((customer) => (

                        <button
                            key={customer.pnr}
                            className={
                                selectedCustomer.pnr === customer.pnr
                                    ? "customer-item active"
                                    : "customer-item"
                            }
                            onClick={() =>
                                onSelectCustomer(customer)
                            }
                        >

                            <div className="avatar">
                                {customer.name
                                    .split(" ")
                                    .map(word => word[0])
                                    .join("")
                                }
                            </div>


                            <div className="customer-item-info">

                                <strong>
                                    {customer.name}
                                </strong>

                                <span>
                                    {customer.tier} · {customer.pnr}
                                </span>

                            </div>

                        </button>

                    ))}

                </div>

            </div>


            <div className="sidebar-footer">

                <div className="agent-status">
                    <span className="status-dot"></span>

                    <div>
                        <strong>AI Agent Online</strong>
                        <span>Ready to assist</span>
                    </div>
                </div>

            </div>

        </aside>
    );
}


export default Sidebar;