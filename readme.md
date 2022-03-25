# GitHub - File Listing (IPFire)

## Contents:

<!--ts-->
   * [About](#about)
   * [Functionalities](#functionalities)
   * [Requisites](#requisites)
   * [How to Use](#how-to-use)
<!--te-->

About
============

- Script created to perform URL testing of several extension files (.cgi) of IPFire (ipfire-2.x).

Functionalities
============

- Returns the status_code of tests in the URL with all files extension (.cgi) in the directory (html/cgi-bin/). The execution output will be placed in a .txt file (url_status_code.txt) in the same directory as the Script was executed.

GitHub: https://github.com/ipfire/ipfire-2.x/tree/master/html/cgi-bin

Requisites
============

- Change the IP and port of the host that will perform the test.

Obs: (ip = 'https://ip:port/cgi-bin/') in the main method.

How To Use
============

- After changing IP and port, run the script and the result will be generated in the .txt file.
