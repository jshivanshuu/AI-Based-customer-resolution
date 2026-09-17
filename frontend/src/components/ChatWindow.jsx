import { useState } from "react";
import { sendMessage } from "../api";


function ChatWindow({
    customer,
    messages,
    setMessages,
    setResolution
}) {

    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);


    async function handleSend() {

        if (!input.trim() || loading) {
            return;
        }


        const userMessage = input.trim();

        setInput("");


        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: userMessage
            }
        ]);


        setLoading(true);


        try {

            const data = await sendMessage(
                userMessage,
                customer.pnr
            );


            setMessages(prev => [
                ...prev,
                {
                    role: "agent",
                    content: data.response
                }
            ]);


            setResolution({
                type: "agent_response",
                response: data.response
            });


        } catch (error) {

            console.error(error);


            setMessages(prev => [
                ...prev,
                {
                    role: "agent",
                    content:
                        "Unable to connect to the resolution service."
                }
            ]);

        } finally {

            setLoading(false);

        }

    }


    function handleKeyDown(event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            handleSend();

        }

    }


    return (

        <div className="chat-container">

            <div className="chat-header">

                <div>

                    <span className="eyebrow">
                        CUSTOMER CONVERSATION
                    </span>

                    <h2>
                        {customer.name}
                    </h2>

                </div>


                <span className="chat-pnr">
                    {customer.pnr}
                </span>

            </div>


            <div className="messages">

                {messages.length === 0 && (

                    <div className="empty-chat">

                        <div className="empty-icon">
                            ✦
                        </div>

                        <h3>
                            How can I help?
                        </h3>

                        <p>
                            Ask the resolution agent about
                            this customer's flight disruption.
                        </p>

                    </div>

                )}


                {messages.map((message, index) => (

                    <div
                        key={index}
                        className={
                            message.role === "user"
                                ? "message-row user-row"
                                : "message-row"
                        }
                    >

                        {message.role === "agent" && (

                            <div className="message-avatar">
                                AI
                            </div>

                        )}


                        <div
                            className={
                                message.role === "user"
                                    ? "message user-message"
                                    : "message agent-message"
                            }
                        >

                            {message.content}

                        </div>

                    </div>

                ))}


                {loading && (

                    <div className="message-row">

                        <div className="message-avatar">
                            AI
                        </div>

                        <div className="message agent-message typing">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>

                    </div>

                )}

            </div>


            <div className="composer">

                <textarea
                    value={input}
                    onChange={(e) =>
                        setInput(e.target.value)
                    }
                    onKeyDown={handleKeyDown}
                    placeholder="Ask about the disruption, refund, rebooking..."
                    rows="1"
                />

                <button
                    className="send-button"
                    onClick={handleSend}
                    disabled={loading || !input.trim()}
                >
                    ↑
                </button>

            </div>

            <div className="composer-hint">
                AI responses are based only on verified booking
                and policy information.
            </div>

        </div>

    );
}


export default ChatWindow;