# Disk Usage Notification Script

This Python script monitors disk usage on a system and sends an email notification when disk usage reaches or exceeds 90%.

## Dependencies

This script depends on the `psutil` and `sendgrid` Python libraries. 

To install these dependencies, run:

```
pip install psutil sendgrid
```

## Environmental Variables

This script requires several environment variables to be set:

- `SENDGRID_API_KEY`: Your SendGrid API key.
- `SENDER_EMAIL`: The email address that will be used to send the notifications.
- `RECEIVER_EMAIL`: The email address that will receive the notifications.

You can set these environment variables in your shell:

```bash
export SENDGRID_API_KEY='your-sendgrid-api-key'
export SENDER_EMAIL='your-email@example.com'
export RECEIVER_EMAIL='receiver-email@example.com'
```

For a more permanent solution, add these lines to your `.bashrc` or `.bash_profile` file.

## Running the Script

To run the script manually, use the following command:

```bash
python disk_usage_script.py
```

## Scheduling the Script with Cron

To schedule the script to run every hour, you can use a cron job.

To open your crontab file, use the command:

```bash
crontab -e
```

Then add the following line to your crontab:

```bash
0 * * * * /usr/bin/env python3 /path/to/disk_usage_script.py
```

Replace `/path/to/disk_usage_script.py` with the actual path to the script.

This will schedule the script to run at the start of every hour.

---

The script will run once every hour, check the disk usage, and send an email if the disk usage is 90% or more.
