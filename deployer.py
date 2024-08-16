import logging

def deploy_app(environment):
    logging.info(f"Starting deployment in {environment} environment.")

    # Simulate deployment process
    if environment == 'dev':
        logging.info("Deploying to development environment...")
        # Add deployment logic for dev environment here
    elif environment == 'prod':
        logging.info("Deploying to production environment...")
        # Add deployment logic for prod environment here
    else:
        logging.error("Unknown environment!")

    logging.info(f"Deployment to {environment} environment completed successfully.")
