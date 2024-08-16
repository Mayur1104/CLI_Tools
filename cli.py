import argparse
from tasks import formatter, deployer

def main():
    parser = argparse.ArgumentParser(description='Custom CLI Tool for development tasks')
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand for code formatting
    parser_format = subparsers.add_parser('format', help='Format code files')
    parser_format.add_argument('path', help='Path to the code file or directory')

    # Subcommand for deployment
    parser_deploy = subparsers.add_parser('deploy', help='Deploy the application')
    parser_deploy.add_argument('--env', choices=['dev', 'prod'], required=True, help='Deployment environment')

    args = parser.parse_args()

    if args.command == 'format':
        formatter.format_code(args.path)
    elif args.command == 'deploy':
        deployer.deploy_app(args.env)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
