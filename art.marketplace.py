class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '{}. "{}". {}, {}. {}, {}.'.format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location) 
  


class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
# List of Marketplaces
veneer = Marketplace()



class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      veneer.add_listing(Listing(artwork, price, self))
      
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        art_listing = None
        if listing.art == artwork:
          art_listing = listing
          artwork.owner = self
        veneer.remove_listing(art_listing)
          
          
    
# List of Clients
edytta = Client("Edytta Halpirt", "Private Collection", False)

moma = Client("The MOMA", "New York", True)


# List of artwork
girl_with_mandolin = Art("Picasso, Pablo", "Girl with Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)



class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
    
  def __repr__(self):
    return "Title: {}, Price: {}".format(self.art.title, self.price)
  

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
veneer.show_listings()

