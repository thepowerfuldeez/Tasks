import vk_api
import time


class Post:
    def __init__(self, public_id_to_propose, post_text_to_propose):
        self.public_id_to_propose = public_id_to_propose
        self.post_text_to_propose = post_text_to_propose
        session = vk_api.VkApi(
            token="53138abc9e626b01f2076352feab1321df0d2147cebe96a8e293417f4e1b5650c5e1d99f6cf3646479f35")
        try:
            session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
        self.session = session

    def post(self):
        self.session.method("wall.post", {
            "owner_id": -self.public_id_to_propose,
            "message": self.post_text_to_propose
        })


class Story:
    def __init__(self, public_id, post_id, comments):
        self.public_id = public_id
        self.post_id = post_id
        self.comments = comments
        session = vk_api.VkApi(token="53138abc9e626b01f2076352feab1321df0d2147cebe96a8e293417f4e1b5650c5e1d99f6cf3646479f35")
        try:
            session.authorization()
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
        self.session = session

    def get_last_comment_from_user_with_that_msg(self, last_msg):
        # TODO: return last of Authorized User's comment
        all_comments = self.session.method("wall.getComments", {
            "owner_id": -self.public_id,
            "post_id": self.post_id
        }).get('items')
        for comment in all_comments[::-1]:
            author_id = comment.get('from_id')
            if comment.get('text') == last_msg:
                return author_id

    comment_id_to_reply = 0

    def post_comment(self, msg):
        self.session.method("wall.createComment", {
            "owner_id": -self.public_id,
            "post_id": self.post_id,
            "message": msg,
            "reply_to_comment": self.comment_id_to_reply
        })
        # update comment_id_to_reply
        self.comment_id_to_reply = self.get_last_comment_from_user_with_that_msg(msg)
        time.sleep(1)

    def start(self):
        for msg in self.comments:
            self.post_comment(msg)

# p = Post(131805658, "Initial post")
# p.post()

# post_id = get_from_eventloop()

s = Story(131805658, 21, ["1", "2", "3"])
s.start()


