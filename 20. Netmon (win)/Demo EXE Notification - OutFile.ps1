# Demo 'Powershell' Notification for Paessler Network Monitor
# Writes current Date/Time into a File
# 
# How to use it:
# 
# Create a exe-notification on PRTG, select 'Demo Exe Notifcation - OutFile.ps1' as program,
# The Parametersection consists of one parameter:
# 
# - Filename
# 
# e.g.
# 
#         "C:\temp\test.txt"
# 
# Note that the directory specified must exist.
# Adapt Errorhandling to your needs.
# This script comes without warranty or support.


if ($Args.Count -eq 0) {

  #No Arguments. Filename must be specified.

  exit 1;
 }elseif ($Args.Count -eq 1){


  $Path = split-path $Args[0];
  
  if (Test-Path $Path)    
  {
    $Text = Get-Date;
    $Text | out-File $Args[0];
    exit 0;
  
  }else
  {
    # Directory does not exist.
    exit 2;
  }
}
