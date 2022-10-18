#!/bin/bash
sudo systemctl start rabbitmq-server
echo "Starting rabbitmq server"
sudo systemctl status rabbitmq-server 