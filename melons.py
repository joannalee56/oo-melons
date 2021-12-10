"""Classes for melon orders."""
from random import randint
import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        """Initialize melon order attributes. """
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5, 9)
        today = datetime.now()
        if today.weekday() in range(0, 6) and today.hour():
            
        return

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()
        if self.species == 'Christmas melon':
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == 'international' and self.qty < 10:
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        self.order_type = "domestic"
        self.tax = 0.08
        super().__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        self.order_type = "international"
        self.country_code = country_code
        self.tax = 0.17
        super().__init__(species, qty)
        

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        self.tax = 0
        self.passed_inspection = False
        self.order_type = 'domestic'
        super().__init__(species, qty)


    def mark_inspection(self):
        """Record the fact than an order has been shipped."""
        self.passed_inspection = True