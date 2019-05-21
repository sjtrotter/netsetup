#!/usr/bin/env python3
"""netsetup_oswrapper.py
=========================
This module is a wrapper class that implements os-specific commands
for use by the netsetup script.
"""
import sys, subprocess

class OSWrapper():
  """OS wrapper class. Binds commands into functions based on the
  OS provided to __init__.
  ====
  Required Arguments:
   - os - specify OS to use
  ====
  Returns: object access to functions that define specific OS
  commands.
  ====
  Functions:
    Function definitions are mostly self-explanatory. They are also
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

   - get_trusted
   - set_trusted
   - del_trusted
   
   - get_targets
   - set_targets
   - del_targets
   
   - get_exclude
   - set_exclude
   - del_exclude

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
    
    # Add input checking to ensure either Windows or Linux was set.

    #possibly... add directory definitions here, based on OS.

  def _die(self, message=""):
    print("{}: cannot stat: {}".format(__file__, \
      message), file=sys.stderr)
    exit()


  def _run_cmd(self, cmd=None, stdin=None):
    """Runs shell command given.
    ====
    Arguments:
    - cmd - command to run
    ====
    Returns:
    Tuple with stdout, stderr, and exit code
    """
    if ( cmd != None ):
      out = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE, \
                                  stderr=subprocess.PIPE)
      if ( stdin != None ):
        stdin = bytes(stdin, 'utf-8')
      stdout, stderr = out.communicate(input=stdin)
      exit_code = out.returncode
      stdout = str(stdout, 'utf-8').strip()
      stderr = str(stderr, 'utf-8').strip()
      output = [ stdout, stderr, exit_code ]

      return output
    else:
      return 1

  def get_hostname(self):
    """Returns the current hostname.
    Commands:
    - Windows - hostname
    - Linux   - hostname
    """
    #code here
    cmd = "hostname"
    stdout, stderr, exit = self._run_cmd(cmd)
    if ( exit == 0 ):
      return stdout
    else:
      die("{} returned an error".format(cmd))


  def set_hostname(self, hostname="mip"):
    """Sets the hostname.
    Commands:
    - Windows - wmic computersystem where name=OLDNAME call rename name={}
    - Linux   - hostnamectl set-hostname {}
    ====
    Arguments:
    - hostname - the hostname to set
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
        mac = self.get_hwaddress().split('-')
        mac_l4 = mac[-2] + mac[-1]
        hostname = "win-" + mac_l4
      elif ( self.os == "Linux" ):
        mac = self.get_hwaddress().split(':')
        mac_l4 = mac[-2] + mac[-1]
        hostname = "nix-" + mac_l4

    #code here
    return hostname

  def get_hwaddress(self, iface="enp2s0"):
    """Returns current hardware address.
    Commands:
    - Windows - ...ipconfig?
    - Linux   - Maybe .. run an arp on 127.0.0.1?
    """
    #code here
    if ( self.os == "Linux" ):
      cmd = [ "ip", "a", "sho", "dev", iface ]
      stdout, stderr, exit_code = self._run_cmd(cmd) 
      cmd = [ "grep", "ether" ]
      stdout, stderr, exit_code = self._run_cmd(cmd, stdin=stdout)
      if ( exit_code == 0 ):
        stdout = stdout.split(' ')[1]
        return stdout
      else:
        self._die("{} returned an error".format(cmd))

    elif ( self.os == "Windows" ):
      cmd = [ "powershell", "-c", "ipconfig /all | findstr Physical | %{ $_.Split(':')[1]; }" ]
      stdout, stderr, exit_code = self._run_cmd(cmd)
      if ( exit_code == 0 ):
        return stdout
      else:
        self._die("{} returned an errer".format(cmd))
 
  def set_hwaddress(self, hwaddress=""):
    """Sets the hardware address.
    Commands:
    - Windows - 
    - Linux   - 
    ====
    Arguments:
    - hwaddress - the MAC address to set
    ====
    Returns:
    - 0 - successful
    - 1 - unsuccessful
    """
    #code here
    pass
  
  def get_ipaddress(self):
    """Returns current IP address(es).
    Commands:
    - Windows - 
    - Linux   - 
    """
    #code here
    pass
  
  def add_ipaddress(self, ipaddress=""):
    """Adds IP address.
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

  # Unit Test: die if no OS provided
  #netset = OSWrapper()

  # Unit Test: die if OS provided is not Linux or Windows
  #netset = OSWrapper(os="Darwin")

  # Unit Test: Set OS. Comment out one of these to test the other.
  # - also... only test on that actual OS.
  netset = OSWrapper(os="Linux")
  #netset = OSWrapper(os="Windows")

  # Unit Test: get_hostname
  #print("hostname: {}".format(netset.get_hostname()))

  # Unit Test: set_hostname (default)
  print("hostname: {}".format(netset.set_hostname()))

  # Unit test: get_hwaddress
  #print("hwaddress: {}".format(netset.get_hwaddress()))
  

if ( __name__ == "__main__" ):
  main()
