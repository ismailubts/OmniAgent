#!/bin/bash
# This hook was installed by OmniAgent
# It calls the pre-commit script in the .omniagent directory

if [ -x ".omniagent/pre-commit.sh" ]; then
    source ".omniagent/pre-commit.sh"
    exit $?
else
    echo "Warning: .omniagent/pre-commit.sh not found or not executable"
    exit 0
fi
