import { useState } from "react";

import { customers } from "./data";
import "./App.css";
import Sidebar from "./components/Sidebar";
import CustomerProfile from "./components/CustomerProfile";
import BookingCard from "./components/BookingCard";
import ChatWindow from "./components/ChatWindow";
import ResolutionPanel from "./components/ResolutionPanel";
import ActivityLog from "./components/ActivityLog";


function App() {

    const [selectedCustomer, setSelectedCustomer] =
        useState(customers[0]);

    const [messages, setMessages] =
        useState([]);

    const [resolution, setResolution] =
        useState(null);


    function handleCustomerChange(customer) {

        setSelectedCustomer(customer);

        setMessages([]);

        setResolution(null);

    }


    return (

        <div className="app">

            <Sidebar
                selectedCustomer={selectedCustomer}
                onSelectCustomer={handleCustomerChange}
            />


            <main className="main-content">

                <header className="topbar">

                    <div>

                        <span className="eyebrow">
                            OPERATIONS
                        </span>

                        <h1>
                            Customer Resolution Agent
                        </h1>

                    </div>


                    <div className="topbar-status">

                        <span className="status-dot"></span>

                        System operational

                    </div>

                </header>


                <div className="dashboard">

                    <section className="left-column">

                        <CustomerProfile
                            customer={selectedCustomer}
                        />

                        <BookingCard
                            customer={selectedCustomer}
                        />

                    </section>


                    <section className="center-column">

                        <ChatWindow
                            customer={selectedCustomer}
                            messages={messages}
                            setMessages={setMessages}
                            setResolution={setResolution}
                        />

                    </section>


                    <section className="right-column">

                        <ResolutionPanel
                            customer={selectedCustomer}
                        />

                        <ActivityLog
                            resolution={resolution}
                        />

                    </section>

                </div>

            </main>

        </div>

    );
}


export default App;