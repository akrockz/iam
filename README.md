## Creating Access Keys Via CLI

1) Federate into admin role in target account (e.g. nonprod-auto, etc)
2) Run `AWS_PROFILE=saml ./scripts/create_access_key.py -u automation-jenkins`
3) Copy the details into a USB key, walk over and give the key to the developer
