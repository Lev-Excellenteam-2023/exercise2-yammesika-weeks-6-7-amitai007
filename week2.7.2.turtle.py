# region turtle - this 2

class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False  # flag to each message to keep track of whether it has been read or not
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, n=None):
        """Read messages from user's inbox.

        :param str user: The username.
        :param n: The number of messages to read.
        :type n: int, optional
        :return: The list of messages.
        :rtype: list[dict]
        :raises KeyError: if the user does not exist.
        """
        user_box = self.boxes[user]
        if n is None:
            n = len(user_box)
        messages = []
        for message in user_box[:n]:
            message['read'] = True
            messages.append(message)
        user_box[:] = user_box[n:]
        return messages

    def search_inbox(self, user, my_query):
        """Search user's inbox for messages that contain query.

        :param str user: The username.
        :param str my_query: The search my_query.
        :return: The list of matching messages.
        :rtype: list[dict]
        :raises KeyError: if the user does not exist.
        """
        user_box = self.boxes[user]
        matching_messages = []
        for message in user_box:
            if not message['read'] and my_query in message['body']:
                matching_messages.append(message)
        return matching_messages


# endregion
