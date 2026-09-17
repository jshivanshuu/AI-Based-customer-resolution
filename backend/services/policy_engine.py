def get_cancellation_policy():
    return {
        "free_rebooking": True,
        "rebooking_window_hours": 24,
        "full_refund": True,
        "refund_processing_days": 7,
        "refund_payment_method": "original_payment_method"
    }


def get_delay_policy(delay_hours):
    if delay_hours < 3:
        return {
            "meal_voucher": True,
            "meal_voucher_amount": 500,
            "lounge_access": False,
            "hotel": False
        }

    elif delay_hours > 3 and delay_hours <= 5:
        return {
            "meal_voucher": True,
            "meal_voucher_amount": 500,
            "lounge_access": True,
            "hotel": False
        }

    elif delay_hours > 5:
        return {
            "meal_voucher": True,
            "meal_voucher_amount": 500,
            "hotel": True,
            "hotel_scope": "delayed_hours_only"
        }

    return {
        "policy_status": "not_explicitly_defined"
    }


def check_fare_difference(amount):
    if amount > 1500:
        return {
            "allowed": False,
            "escalation_required": True,
            "reason": "Fare difference above ₹1,500 requires supervisor approval"
        }

    return {
        "allowed": True,
        "escalation_required": False
    }


def get_loyalty_policy(loyalty_tier):
    if loyalty_tier in ["Gold", "Platinum"]:
        return {
            "priority_rebooking": True,
            "additional_compensation": False
        }

    return {
        "priority_rebooking": False,
        "additional_compensation": False
    }


def resolve_policy(
    intent,
    customer,
    bookings,
    fare_difference=0
):

    # --------------------------------
    # Cancellation refund
    # --------------------------------

    if intent == "cancellation_refund":

        cancelled_booking = None

        for booking in bookings:
            if booking.get("status", "").lower() == "cancelled":
                cancelled_booking = booking
                break

        if cancelled_booking is None:
            return {
                "allowed": False,
                "reason": "Booking is not cancelled"
            }

        policy = get_cancellation_policy()

        return {
            "allowed": True,
            "action": "refund",
            "refund_amount": "full",
            "processing_time": f"{policy['refund_processing_days']} business days",
            "payment_method": policy["refund_payment_method"],
            "escalation_required": False
        }

    # --------------------------------
    # Cancellation rebooking
    # --------------------------------

    if intent == "cancellation_rebooking":

        cancelled_booking = None

        for booking in bookings:
            if booking.get("status", "").lower() == "cancelled":
                cancelled_booking = booking
                break

        if cancelled_booking is None:
            return {
                "allowed": False,
                "reason": "Booking is not cancelled"
            }

        return {
            "allowed": True,
            "action": "free_rebooking",
            "window_hours": 24,
            "escalation_required": False
        }

    # --------------------------------
    # Delay compensation
    # --------------------------------

    if intent == "delay_compensation":

        delayed_booking = None

        for booking in bookings:
            if booking.get("status", "").lower() == "delayed":
                delayed_booking = booking
                break

        if delayed_booking is None:
            return {
                "allowed": False,
                "reason": "Booking is not delayed"
            }

        delay_hours = delayed_booking["delay_hours"]

        policy = get_delay_policy(delay_hours)

        return {
            "allowed": True,
            "action": "delay_entitlements",
            "delay_hours": delay_hours,
            "policy": policy,
            "escalation_required": False
        }

    # --------------------------------
    # Higher fare rebooking
    # --------------------------------

    if intent == "higher_fare_rebooking":

        return {
            "allowed": check_fare_difference(
                fare_difference
            )["allowed"],
            "fare_difference": fare_difference,
            **check_fare_difference(fare_difference)
        }

    # --------------------------------
    # Business class upgrade
    # --------------------------------

    if intent == "business_upgrade":

        return {
            "allowed": False,
            "escalation_required": True,
            "reason": "Business-class upgrade is not covered by the supplied policy"
        }

    # --------------------------------
    # Legal complaint
    # --------------------------------

    if intent == "legal_complaint":

        return {
            "allowed": False,
            "escalation_required": True,
            "reason": "Legal action or formal complaint requires human support"
        }

    # --------------------------------
    # Unknown request
    # --------------------------------

    return {
        "allowed": False,
        "escalation_required": True,
        "reason": "Request is not covered by the supplied policy"
    }