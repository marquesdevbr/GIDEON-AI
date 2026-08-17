class ConfirmationManager:

    def __init__(self):

        self.pending_action = None

    def request_confirmation(
        self,
        action,
        description,
        data=None
    ):

        self.pending_action = {
            "action": action,
            "description": description,
            "data": data
        }

        return (
            f"CONFIRMAÇÃO NECESSÁRIA: "
            f"{description}"
        )

    def has_pending_action(self):

        return self.pending_action is not None

    def get_pending_action(self):

        return self.pending_action

    def confirm(self):

        if not self.pending_action:

            return None

        action = self.pending_action

        self.pending_action = None

        return action

    def cancel(self):

        self.pending_action = None

        return (
            "Ação cancelada."
        )