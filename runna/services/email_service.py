import os
import base64
import resend
from typing import List
import logging

logger = logging.getLogger(__name__)

# Set the Resend API key
resend.api_key = os.getenv("RESEND_API_KEY")

def prepare_attachment(file_obj) -> dict:
    """
    Accepts a file-like object (e.g., TemporaryUploadedFile) or a file path,
    reads its content, encodes it in base64, and returns a dict with filename and content.
    """
    # If the object is a TemporaryUploadedFile or any file-like object:
    if hasattr(file_obj, 'read'):
        file_content = file_obj.read()
        # Reset pointer if needed:
        if hasattr(file_obj, 'seek'):
            file_obj.seek(0)
        filename = file_obj.name
    else:
        # Otherwise, assume it's a file path.
        with open(file_obj, "rb") as f:
            file_content = f.read()
        filename = os.path.basename(file_obj)
    
    encoded_content = base64.b64encode(file_content).decode("utf-8")
    return {"filename": filename, "content": encoded_content}


class EmailService:
    """Service for sending emails using Resend."""

    @staticmethod
    def send_email(
        to: List[str],
        subject: str,
        html_content: str,
        sender: str = "Acme <onboarding@resend.dev>",
        bcc: List[str] = None,
        cc: List[str] = None,
        attachments: List[str] = None
    ) -> dict:
        """
        Sends an email using the Resend API.
        """
        # Process attachments if provided
        prepared_attachments = None
        if attachments:
            prepared_attachments = [prepare_attachment(path) for path in attachments]

        params: resend.Emails.SendParams = {
            "from": sender,
            "to": to,
            "bcc": bcc,  # Correctly using bcc here
            "cc": cc,
            "attachments": prepared_attachments,
            "subject": subject,
            "html": html_content,
        }
        
        print("resend.api_key: ", resend.api_key)
        # print("params: ", params)

        try:
            email_response = resend.Emails.send(params)
            return {
                "email_status": "201",
                "email_details": "Email sent successfully",
                "error": None
            }
        except Exception as e:
            print(f"Failed to send email: {e}")
            logger.error(f"Failed to send email: {e}")
            raise e

# Example usage
# cc = ["santiagocarranzazinny@gmail.com"]
# bcc = ["facundoolivam@gmail.com"]
# to = ["facundoolivam@gmail.com"]
# attachments_paths = ["C:\\Users\\facun\\Downloads\\Fisica2-FacundoOlivaMarchetto-2406097.pdf"]
# subject = "Demanda ID 1 ha sido desactivada"
# html_content = """
#     <strong>Estimados,</strong><br>
#     La demanda ID 1 ha sido desactivada.<br>
#     <strong>Details:</strong><br>
#     Zona: ads <br>
#     Comentarios: asds<br>
#     Saludos,<br>
#     Nuevo RUNNA
# """

# email_response = EmailService.send_email(to, subject, html_content, bcc=bcc, cc=cc, attachments=attachments_paths)
# print(f"Email response: {email_response}")
