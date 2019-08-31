#!/usr/bin/python3

import argparse
import boto3


def _get_args():
    parser = argparse.ArgumentParser(
        description='Component Compiler for the Action Runner',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-u', '--user-name', help='IAM UserName', required=True)
    args = parser.parse_args()
    return args


def run(args):
    client = boto3.client('iam')
    print('Creating access key for {}...'.format(args.user_name))
    response = client.create_access_key(UserName=args.user_name)
    print('UserName={}, AccessKeyId={}, SecretAccessKey={}'.format(response['AccessKey']['UserName'], response['AccessKey']['AccessKeyId'], response['AccessKey']['SecretAccessKey']))


if __name__ == '__main__':
    run(_get_args())
