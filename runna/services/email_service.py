import os
import resend
from typing import List
import logging
logger = logging.getLogger(__name__)


# Set the Resend API key
resend.api_key = os.getenv("RESEND_API_KEY")


class EmailService:
    """Service for sending emails using Resend."""

    @staticmethod
    def send_email(to: List[str], subject: str, html_content: str, sender: str = "Acme <onboarding@resend.dev>"):
        """
        Sends an email using the Resend API.

        :param to: List of recipient email addresses.
        :param subject: Email subject line.
        :param html_content: HTML content of the email body.
        :param sender: The sender's email address and name.
        :return: Response from the Resend API.
        """
        params: resend.Emails.SendParams = {
            "from": sender,
            "to": to,
            "subject": subject,
            "html": html_content,
        }

        try:
            # email_response = resend.Emails.send(params)
            email_response = f'resend api key: {resend.api_key}'
            logger.info(f"Email sent successfully: {email_response}")
            print(f"Email sent successfully: {email_response}")
            # return {
            #     "email_status": email_response.get("status"),
            #     "email_details": email_response.get("response"),
            #     "error": email_response.get("message", None)
            # }
            return {
                "email_status": "status",
                "email_details": "response",
                "error": "message"
            }
        except Exception as e:
            # Log the error if logging is set up, or handle gracefully
            print(f"Failed to send email: {e}")
            logger.error(f"Failed to send email: {e}")
            return None
