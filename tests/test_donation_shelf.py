import pytest
from src.donation_shelf import DonationShelf


def test_add_donation():
    shelf = DonationShelf()
    donation = shelf.add_donation("donor@example.com", "Sketchbook")

    assert donation.donation_id == 1
    assert donation.donor_email == "donor@example.com"
    assert donation.item_name == "Sketchbook"
    assert donation.is_available() is True


def test_empty_item_name_raises_error():
    shelf = DonationShelf()

    with pytest.raises(ValueError):
        shelf.add_donation("donor@example.com", "")


def test_empty_donor_email_raises_error():
    shelf = DonationShelf()

    with pytest.raises(ValueError):
        shelf.add_donation("", "Notebook")


def test_pick_up_item_generates_message():
    shelf = DonationShelf()
    donation = shelf.add_donation("donor@example.com", "Paintbrush set")

    message = shelf.pick_up_item(donation.donation_id, "receiver@example.com")

    assert message == "Someone welcomed your item 'Paintbrush set' into their life today."
    assert donation.is_available() is False
    assert donation.picked_up_by == "receiver@example.com"


def test_cannot_pick_up_same_item_twice():
    shelf = DonationShelf()
    donation = shelf.add_donation("donor@example.com", "Notebook")

    shelf.pick_up_item(donation.donation_id, "receiver1@example.com")

    with pytest.raises(ValueError):
        shelf.pick_up_item(donation.donation_id, "receiver2@example.com")


def test_invalid_donation_id_raises_error():
    shelf = DonationShelf()

    with pytest.raises(ValueError):
        shelf.pick_up_item(999, "receiver@example.com")
