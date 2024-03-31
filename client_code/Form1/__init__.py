from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import numpy as np

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.data_grid_1.visible = False
    self.repeating_panel_1.visible = False
    self.label_2.visible = False
    self.drop_down_1.visible = False
    self.button_1.visible = False
    self.label_1.visible = False

  def classify_click(self, **event_args):
    """This method is called when the button is clicked"""
    c = self.file_loader_1
    if c.file != None:
      food_category = anvil.server.call('predict', c.file)
      
      self.data_grid_1.visible = True
      self.repeating_panel_1.visible = True
      self.repeating_panel_1.items = [
        {"cat": food_category[0][1], "prob": round(food_category[0][0],3)}
        {"cat": food_category[1][1], "prob": round(food_category[1][0],3)},
        {"cat": food_category[2][1], "prob": round(food_category[2][0],3)},
        {"cat": food_category[3][1], "prob": round(food_category[3][0],3)},
        {"cat": food_category[4][1], "prob": round(food_category[4][0],3)}
      ]
      self.label_2.visible = True
      self.drop_down_1.visible = True
      self.button_1.visible = True

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_1.source = file

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_1.visible = True
    anvil.server.call('finetune', self.file_loader_1.file, self.drop_down_1.selected_value)

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    row = self.drop_down_1.selected_value






