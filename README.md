# VPN Reminder

The `vpn_reminder` tool is designed to check whether a Slack user has their VPN activated. With this tool running continuously, users can ensure that they aren't accessing services from prohibited countries, thus avoiding potential access issues.

## **Pre-requisites:**

1. Ensure you have the `.env` file prepared with the following variables:
    - `SLACK_TOKEN` - Your Slack API workspace client token 
    - `SLACK_CHANNEL` - The Slack chat client token


2. It's essential to have both [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

## **Running the Service:**

1. First, clone the repository:
```bash
git clone <your_repository_link> && cd <repository_name>
```
2. Then, build the Docker image:
```bash
docker-compose up --build
```

he service should now be active and monitoring as expected. If there are any issues, please review your configuration and setup.