from abc import ABC, abstractmethod


class NotificationSender(ABC):
    """
        # Interface
        Define a regra de construção.
        Essa interface, por exemplo, estrutura como deve ser um classe para notificações.
    """
    @abstractmethod
    def send_notification(self, message: str) ->  None:
        print(f"Interface {message}")

class EmailNotificationSender(NotificationSender):
    def send_notification(self, message) -> None:
        super().send_notification(message)
        print(f"Classe Email {message}")

class SMSNotificationSender(NotificationSender):
    def send_notification(self, message):
        super().send_notification(message)
        print(f"Classe SMS {message}")

# email = EmailNotificationSender()
# email.send_notification("Ola")

# sms = SMSNotificationSender()
# sms.send_notification("Ola")

class Notificator:
    def __init__(self, notificator_sender: NotificationSender) -> None:
        self.__notificator_sender = notificator_sender

    def send(self, message: str) -> None:
        self.__notificator_sender.send_notification(message)
        
        
obj = Notificator(EmailNotificationSender())

obj.send("Hello World")
