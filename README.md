# OpenVPN Server with Zero Trust Cloudflare Tunnel and Connection Monitoring

This project demonstrates the setup of an OpenVPN server on Oracle Cloud, integration with Cloudflare's Zero Trust tunnels, and real-time connection monitoring using Python.

## Features
- Secure VPN access using OpenVPN on Oracle Cloud.
- Zero trust tunnel, cloudflare.
- Python monitoring script for tracking VPN connections.

## Requirements
- Oracle Cloud Infrastructure account.
- OpenVPN server (Marketplace image).
- Cloudflare account for Zero Trust setup.
- Python 3.x for the monitoring script.

## Usage
- Docker-compose file for running the zero trust tunnel in cloudflare.

## DNS Configuration
1. Created an `A` record for `vpn.example.com` pointing to the server's public IP.
2. Enabled Cloudflare proxy for `vpn.example.com` to route traffic through the Zero Trust Tunnel.
3. Verified SSL settings to ensure secure traffic between the client and server.


