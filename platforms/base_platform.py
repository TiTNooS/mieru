# -*- coding: utf-8 -*-
"""this is a "abstract" class defining the API for platform modules
   NOTE: this is not just API, some multi-platform implementations are there too
"""

class BasePlatform:
  def __init__(self):
    pass

  def guiModuleLoaded(self):
    """notify the device module that the GUI module
    has been loaded"""
    pass

  def getName(self):
    return "unknown platform"

  def getDeviceName(self):
    return "unknown device"

  def getIDString(self):
    """
    get a unique string identifier for a platform module
    """
    return None

  def getScreenWH(self):
    return 800, 480

  def hasPagingKeys(self):
    """report if the device has has some buttons usable for paging"""
    return False

  def startChooser(self, type):
    """start a file/folder chooser dialog"""
    pass

  def handleKeyPress(self, keyName):
    """handle a key press event and return True if the key was "consumed" or
    "False" if it wasn't"""
    return False

  def notify(self, message, icon):
    """show a notification, if possible"""
    pass

  def showPagingDialogCB(self, button):
    """for showing paging dialog from button CB"""
    self.showPagingDialog()

  def showPagingDialog(self):
    pass

  def pagingDialogBeforeOpen(self):
    """do something before opening the paging dialog"""
    pass

  def showInfo(self):
    """show/witch to the options info"""
    pass

  def showOptions(self):
    """show/witch to the options window"""
    pass

  def minimize(self):
    """minimize the main window"""
    pass

  def showMinimiseButton(self):
    """
    report if a window minimise button needs to be shown somewhere in the
     application managed UI
    """
    return True

  def showQuitButton(self):
    """
    report if a quit button needs to be shown somewhere in the
     application managed UI
    """
    return True

  def getDefaultFileSelectorPath(self):
    """a fail-safe path for the file/folder selector on its first opening"""
    return '/'

  # GTK specific

  def startInFullscreen(self):
    """"should Mieru start in fullscreen on this platform ?"""
    return True

  def getSupportedGUIModuleIds(self):
    """
    supported GUI module IDs, ordered by preference from left to right
    (the most-preferred should be on the left)
    """
    return ["QML"] # as default try GTK first and then QML

#  def Button(self, label=""):
#    """return classic GTK button"""
#    return gtk.Button(label)
#
#  def CheckButton(self, label=""):
#    """return classic GTK check button"""
#    return gtk.CheckButton(label)



