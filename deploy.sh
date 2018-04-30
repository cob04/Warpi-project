#!/bin/bash

ansible-playbook ./production/deploy.yml --private-key=./ssh-keys/45.33.51.166_prod_key -K -u cobain -i ./production/hosts -vvv
