#!/usr/bin/env python3
"""netsetup_oswrapper.py
=========================
This module is a wrapper class that
implements os-specific commands for
use by the netsetup script.
"""

class OSWrapper():
  """OS wrapper class. Binds commands
  into functions based on the OS
  provided to __init__.
  ====
  Required Arguments:
   - os - specify OS to use
  ====
  Returns: object access to functions
  that define specific OS commands.
  ====
  Functions:
    Function definitions are mostly
    self-explanatory. They are also
    documented within themselves.

   - get_hostname
   - set_hostname

   - get_hwaddress
   - set_hwaddress

   - get_ipaddress
   - add_ipaddress
   - del_ipaddress

   - get_gateway
   - set_gateway
   - del_gateway

   - get_netmask
   - set_netmask

   - get_dns
   - add_dns
   - del_dns

   - get_ntp
   - set_ntp

   - set_trusted
   - set_targets
   - set_exclude

   - get_fw_rule
   - set_fw_rule
   - del_fw_rule
   - set_fw_profile
  """
  def __init__(self, os=None):
  """__init__ method, initializes
  class.  Returns error if os is
  not defined; sets self.os if it is.
  """

    self.os = os

    if ( self.os == None ):
      raise AssertionError

  def get_hostname(self):
  """Returns the current hostname.
  Commands:
  - Windows - hostname
  - Linux   - hostname
  """
    #code here
    pass

  def set_hostname(self, hostname="mip"):
  """Sets the hostname.
  Commands:
  - Windows - wmic computersystem where name=OLDNAME call rename name={}
  - Linux   - hostnamectl set-hostname {}
  ====
  Returns:
  - 0 - successful
  - 1 - unsuccessful
  ====
  Windows: sets restart flag
  """
    # set default hostname based on OS
    if ( hostname =="mip" ):
      if   ( self.os == "Windows" ):
        hostname = "win-mip"
      elif ( self.os == "Linux" ):
        hostname = "nix-mip"

    #code here
    pass

  def get_hwaddress(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 