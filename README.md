# Phishing Examples

## Epic Games
This contains a web page with some scripts that send an AJAX get request to my personal server http://ngetty.me:8089.

On my website I run a node http server with cors enabled making it much easier to test.

```sh
npm install http-server

getty@getty:~$ http-server -p 8089 --cors='*' --no-dotfiles -r  -i
Starting up http-server, serving ./
Available on:
  http://127.0.0.1:8089
  http://159.203.5.243:8089
  http://10.20.0.5:8089
Hit CTRL-C to stop the server

```

Move the html file to an apache server or something like that, and click the login page and you should post the creds to the ajax script destination, check the logs on the node http server to see if it works or not. Also use the web dev console to see more deets.

