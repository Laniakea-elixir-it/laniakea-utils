#!/bin/bash
##install openstack cli
### download the openstackv2 file and assign the $OPESTACK_CREDENTIALS variable
#Variable to fill
OPESTACK_CREDENTIALS="<openstack v2 credential file>"
IMAGE="<galaxy image to use>"
INSTANCE="<name of the Virtual machine>"

python3 -m venv openstack_cli_flavour
. openstack_cli_flavour/bin/activate
pip3 install --upgrade pip
pip3 install python-openstackclient
 
set +x $OPENSTACK_CREDENTIALS
.  $OPESTACK_CREDENTIALS
openstack server create --flavor large --image $IMAGE --key-name laniakea-robot  --network public_net --security-group default  --security-group ssh --security-group http $INSTANCE --wait
export VM_IP=$(openstack server list --name $INSTANCE -f json | grep -Eo \'[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\' )
echo $VM_IP
