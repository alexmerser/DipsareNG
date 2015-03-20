#!/usr/bin/env bash

echo "Configuring"
echo "copy recipes/gc_dispareng.conf >> etc/"
cp recipes/gc_dispareng.conf etc/
echo "copy recipes/supervisord.conf >> etc/"
cp recipes/supervisord.conf etc/
echo "copy recipes/nginx.conf >> /etc/nginx/sites-available/dispareng"
cp recipes/nginx.conf /etc/nginx/sites-available/dispareng
