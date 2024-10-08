from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class User(UserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.location_dd.items = [(r['name'], r) for r in app_tables.locations.search(tables.order_by('name'))]
    self.carrier_dd.items = [(r['carrier'], r) for r in app_tables.carriers.search(tables.order_by('carrier'))]
    user = anvil.server.call('get_user')
    if user:
      self.user_copy = dict(user)
      self.item = self.user_copy
      self.headline.text = "View/Edit User: " + self.item['email']
    else:
      self.user_copy = dict()
    self.toggle_text_components()


  def toggle_text_components(self):
    self=self
    by_text_components = [self.carrier_dd, 
                          self.cellphone_box, 
                          self.label_2, 
                          self.label_3, 
                          self.test_text_btn, 
                          self.test_text_spacer]
    for each in by_text_components:
      each.visible = self.notify_by_text_checkbox.checked

  def notify_by_text_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.toggle_text_components()