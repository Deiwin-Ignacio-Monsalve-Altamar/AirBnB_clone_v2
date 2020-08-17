#!/usr/bin/env bash
#Install nginx
sudo apt-get -y update
sudo apt-get install -y nginx 

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "Content false" | sudo tee /data/web_static/releases/test/index.html

file_likend="/data/web_static/current"
destination="/data/web_static/releases/test/"

sudo ln -sf "$file_linked" "$destination"
data="/data/"
sudo chown -R ubuntu:ubuntu "$data"
config="/etc/nginx/sites-enabled/default"
sudo sed -i "41i \\\\tlocation /hbnb_static/ {\n\t\talias $file_likend/;\n\t\tautoindex off;\n\t}\n" "$config"
sudo service nginx restart
