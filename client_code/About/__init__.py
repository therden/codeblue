from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    markdown_text = anvil.server.call(get_misc_table_data, 'about.md', 'media')
    anvil.server.
    self.rich_text_1.data = markdown_text
