![CI](https://github.com/rw687-dev/donation-shelf-system_5493/actions/workflows/ci.yml/badge.svg)

# Donation Shelf System

## Project Overview

The Donation Shelf System is a small Python project that models a student donation shelf. The system allows a donor to register an item, stores the donation information, and lets a receiver pick up the item later. When an item is picked up, the system generates a message for the donor: “Someone welcomed your item into their life today.”

This project was inspired by a physical donation shelf concept using RFID tags, buttons, and email notifications. The Python version focuses on the core software logic behind that system: storing donations, checking item availability, preventing duplicate pickups, and generating notification messages.

## Features

- Add a new donation with donor email and item name
- Store each donation with a unique donation ID
- Check whether an item is still available
- Mark an item as picked up by a receiver
- Prevent the same item from being picked up twice
- Generate a donor notification message
- Raise clear errors for invalid or empty inputs

## Project Structure

```text
donation-shelf-system_5493/
├── src/
│   ├── __init__.py
│   └── donation_shelf.py
├── tests/
│   └── test_donation_shelf.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
