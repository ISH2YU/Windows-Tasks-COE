# VulnServer 

We Need Two Virtual Machines Windows 10 , Kali . Download VulnServer [Here](https://thegreycorner.com/vulnserver.html)

In the Windows VM open Cmd go to `vulnserver` directory < Run `vulnserver.exe`.

In the Kali , write this command < HELP
```sh
nc -nv 192.168.242.130 9999
```
Now we have to Find a Crash we do that by Fuzzing , we write a code in `test.spk`.

