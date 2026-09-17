export const customers = [
    {
        name: "Priya Nair",
        tier: "Gold",
        pnr: "SK4821X",
        email: "priya.nair@example.com",
        phone: "+91-98xxxxxxx1",
        flights: 6,
        complaints: 1
    },
    {
        name: "Arvind Kulkarni",
        tier: "Silver",
        pnr: "TR1190B",
        email: "arvind.kulkarni@example.com",
        phone: "+91-98xxxxxxx2",
        flights: 3,
        complaints: 0
    },
    {
        name: "Meher Kaur",
        tier: "Platinum",
        pnr: "WL7742",
        email: "meher.kaur@example.com",
        phone: "+91-98xxxxxxx3",
        flights: 10,
        complaints: 1
    }
];


export const bookings = {
    SK4821X: [
        {
            flight: "SK-204",
            route: "Delhi → Goa",
            date: "23 Sep 2026",
            departure: "18:40",
            status: "Cancelled",
            reason: "Operational reasons"
        },
        {
            flight: "Return",
            route: "Goa → Delhi",
            date: "25 Sep 2026",
            departure: "16:20",
            status: "Unaffected"
        }
    ],

    TR1190B: [
        {
            flight: "SK-118",
            route: "Mumbai → Bengaluru",
            date: "23 Sep 2026",
            departure: "07:10",
            newDeparture: "11:10",
            status: "Delayed",
            delay: "4h"
        }
    ],

    WL7742: [
        {
            flight: "SK-305",
            route: "Delhi → Hyderabad",
            date: "23 Sep 2026",
            departure: "14:00",
            newDeparture: "20:00",
            status: "Delayed",
            delay: "6h"
        }
    ]
};