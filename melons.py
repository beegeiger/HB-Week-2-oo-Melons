"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, country_code=None):

        self.shipped = False
        self.qty = qty
        self.country_code = country_code
        self.species = species

 
    def get_total(self):
        """Calculate price, including tax."""
        #If the species is Christmas melon the base price is multiplied by 1.5
        Christ_mas = 1
        if self.species == "Christmas melon":
            Christ_mas = 1.5
        qty_charge = 0
        #For internation orders if there is less than 10 melons, there is a 3 dollar charge
        if self.qty < 10 and self.order_type == "international":
            qty_charge = 3
        
        base_price = 5 * Christ_mas
        total = (1 + self.tax) * self.qty * base_price + qty_charge

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    # def qty_charge(self):
    #     if self.qty < 10:
    #         total = get_total(self) + 3
