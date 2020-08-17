#!/usr/bin/env bash
#Install nginx
sudo apt-get -y update
sudo apt-get install -y nginx
sudo service nginx start

sudo mkdir -p "/data/"
sudo mkdir -p "/data/web_static/"
sudo mkdir -p "/data/web_static/releases/"
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"
sudo echo "some simple data" > "/data/web_static/releases/test/index.html"

link_file="/data/web_static/current"
destination="/data/web_static/releases/test/"
sudo ln -sf "$destination" "$link_file"
sudo chown -R ubuntu:ubuntu /data/
config="/etc/nginx/sites-enabled/default"
sudo sed -i "38i \\\\tlocation /hbnb_static/ {\n\t\talias $link_file/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart
