# VPN Reminder

The `vpn_reminder` tool is designed to check whether a Slack user has their VPN activated. With this tool running continuously, users can ensure that they aren't accessing services from prohibited countries, thus avoiding potential access issues.

## **Pre-requisites:**

1. Ensure you have the `.env` file prepared with the following variables:
    - `SLACK_TOKEN=<token>` - Your Slack API workspace client token 
    - `SLACK_CHANNEL=<token>` - The Slack chat client token

2. It's essential to have [Docker](https://docs.docker.com/get-docker/) installed on your machine.

## **Running the Service:**

1. First, clone the repository:
```bash
git clone https://github.com/stickandstone/vpn_reminder.git && cd vpn_reminder
```
2. Next, create the `.env` inside in the repo folder file with the variables mentioned above.

3. Then, build the Docker image:
```bash
docker build -t vpn_reminder . 
```
4.Finally, run the Docker container:
```bash
docker run -d --env-file .env --name vpn_reminder vpn_reminder
```

The service should now be active and monitoring as expected. If there are any issues, please review your configuration and setup.
And don't hesitate to contact me if you have any questions.