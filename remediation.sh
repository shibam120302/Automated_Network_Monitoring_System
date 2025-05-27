#!/bin/bash
# remediation.sh
# Shell-based fallback for restarting network services on Linux

echo "Restarting network service..."
sudo systemctl restart NetworkManager.service
echo "Done."
