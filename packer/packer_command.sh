#!/bin/bash

#Just list all of the packer command here

# Validate
# packer validate -var region="us-west1" -var source_image_family="ubuntu-1604-lts" -var machine_type="n1-standard-1" -var zone="us-west1-b" -var project_id=$PROJECT_ID -var service_account_json=$SERVICE_ACCOUNT_JSON demo-packer.json

# Build
# packer build -var region="us-west1" -var source_image_family="ubuntu-1604-lts" -var machine_type="n1-standard-1" -var zone="us-west1-b" -var project_id=$PROJECT_ID -var service_account_json=$SERVICE_ACCOUNT_JSON demo-packer.json
