from dataclasses import dataclass
from typing import Optional


@dataclass
class Donation:
    donation_id: int
    donor_email: str
    item_name: str
    picked_up_by: Optional[str] = None

    def is_available(self) -> bool:
        return self.picked_up_by is None


class DonationShelf:
    def __init__(self):
        self.donations = {}
        self.next_id = 1

    def add_donation(self, donor_email: str, item_name: str) -> Donation:
        if not donor_email.strip():
            raise ValueError("Donor email cannot be empty.")
        if not item_name.strip():
            raise ValueError("Item name cannot be empty.")

        donation = Donation(
            donation_id=self.next_id,
            donor_email=donor_email,
            item_name=item_name
        )

        self.donations[self.next_id] = donation
        self.next_id += 1
        return donation

    def pick_up_item(self, donation_id: int, receiver_email: str) -> str:
        if donation_id not in self.donations:
            raise ValueError("Donation ID does not exist.")
        if not receiver_email.strip():
            raise ValueError("Receiver email cannot be empty.")

        donation = self.donations[donation_id]

        if not donation.is_available():
            raise ValueError("This item has already been picked up.")

        donation.picked_up_by = receiver_email

        return f"Someone welcomed your item '{donation.item_name}' into their life today."
