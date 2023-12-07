#!/usr/bin/env bash
# The script sets up the webservers for deployment of web static
# Install nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create the folder /data
sudo mkdir -p /data

# Create the folder /data/web_static/
sudo mkdir /data/web_static

# Create the folder /data/web_static/releases/ and /data/web_static/shared/
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases

# Create the folder 
sudo mkdir /data/web_static/releases/test/

# Create a html file with simple content
sudo touch /data/web_static/releases/test/index.html
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# Create a sym link /data/web_static/current linked to/data/web_static/releases/test folder
target="/data/web_static/releases/test/"
symlink="/data/web_static/current"
# Delete the symlink if it exists
if [ -L "$symlink" ]; then
    sudo rm -f "$symlink"
fi
# Create the new symlinl
sudo ln -s "$target" "$symlink"

# Give ownership of the /data folder to the user ubuntu as well as the group
sudo chown -R ubuntu:ubuntu /data/

# Update the nginx config file to serve the content of /data/web_static/current/ to hbnb_static
nginxconf="/etc/nginx/nginx.conf"
# Backup the original configuration file
scp "$nginxconf" "$nginxconf.bak"
# Modify the location block with alias
sudo bash -c 'cat <<EOF >>'"$nginxconf"'
server {
    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}
EOF'

# Restart nginx
sudo service nginx restart