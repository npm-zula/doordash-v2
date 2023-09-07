from enum import Enum


class status_options(Enum):
    ORDERED = 'Ordered'
    PAID = 'Paid'
    CANCELLED = 'Cancelled'
    COMPLETED = 'Completed'
