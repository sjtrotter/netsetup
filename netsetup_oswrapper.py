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
  """__init__ method, initializes class. Returns error if os is
  not defined; sets self.os if it is.  Also sets directory
  variables based on OS.
  """

    self.os = os
    
    if ( self.os == None ):
      self._die("no OS has been defined.")
    
    #possibly... add directory definitions here, based on OS.

  def _die(self, message=""):
    print("{}: cannot stat: {}".format(__file__, message), file=sys.stderr)
    exit()
    
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
  """
    #code here
    pass
  
  def set_hwaddress(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_ipaddress(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def add_ipaddress(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def del_ipaddress(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_gateway(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_gateway(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def del_gateway(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_netmask(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_netmask(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_dns(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def add_dns(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def del_dns(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_ntp(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_ntp(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_trusted(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_targets(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_exclude(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def get_fw_rule(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_fw_rule(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def del_fw_rule(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
  
  def set_fw_profile(self):
  """Returns current hardware address.
  Commands:
  - Windows - 
  - Linux   - 
  """
    #code here
    pass
   
def main():
  """main function, only runs if name==main.
  Will input unit tests here.
  """
  #code here
  pass

if ( __name__ == "__main__" ):
  main()
