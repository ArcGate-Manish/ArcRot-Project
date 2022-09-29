import unittest
from app import app

# @unittest.skip("skip this file")
# def test_4_login_success(self):
#     tester = app.test_client(self)
#     response = tester.post("/loginapi")
#     statuscode = response.status_code
#     self.assertEqual(statuscode, 200)
#     self.assertIsNotNone(response)


class TestApp(unittest.TestCase):

    # -----------------club api test case-----------------------

 # @unittest.skip("skip this file")
    def test_1_individual_club_success(self):
        tester = app.test_client(self)
        response = tester.get("/club/1/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["about"])
        self.assertIsNotNone(field_value[0]["address"])
        self.assertIsNotNone(field_value[0]["assistant_governor"])
        self.assertIsNotNone(field_value[0]["chartered"])
        self.assertIsNotNone(field_value[0]["club_ids"])
        self.assertIsNotNone(field_value[0]["club_members"])
        self.assertIsNotNone(field_value[0]["club_type"])
        self.assertIsNotNone(field_value[0]["district_code"])
        self.assertIsNotNone(field_value[0]["email_id"])
        self.assertIsNotNone(field_value[0]["fax_no"])
        self.assertIsNotNone(field_value[0]["location"])
        self.assertIsNotNone(field_value[0]["mailing_address"])
        self.assertIsNotNone(field_value[0]["name"])
        self.assertIsNotNone(field_value[0]["phone_no"])
        self.assertIsNotNone(field_value[0]["rotary_langauge"])
        self.assertIsNotNone(field_value[0]["vendors"])
        self.assertIsNotNone(field_value[0]["website"])
        self.assertIsNotNone(field_value[0]["club_members"])
        for row in (field_value[0]["club_members"]):
            self.assertIsNotNone(["club_member_email"])
            self.assertIsNotNone(["club_member_id"])
            self.assertIsNotNone(["is_active"])
            self.assertIsNotNone(["member_first_name"])
            self.assertIsNotNone(["member_from"])
            self.assertIsNotNone(["member_last_name"])
            self.assertIsNotNone(["member_till"])
            self.assertIsNotNone(["profile"])
            self.assertIsNotNone(["profile_picture"])

    def test_2_list_club_success(self):
        tester = app.test_client(self)
        response = tester.get("/club/list/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["about"])
        self.assertIsNotNone(field_value[0]["address"])
        self.assertIsNotNone(field_value[0]["assistant_governor"])
        self.assertIsNotNone(field_value[0]["chartered"])
        self.assertIsNotNone(field_value[0]["club_ids"])
        self.assertIsNotNone(field_value[0]["club_members"])
        self.assertIsNotNone(field_value[0]["club_type"])
        self.assertIsNotNone(field_value[0]["district_code"])
        self.assertIsNotNone(field_value[0]["email_id"])
        self.assertIsNotNone(field_value[0]["fax_no"])
        self.assertIsNotNone(field_value[0]["location"])
        self.assertIsNotNone(field_value[0]["mailing_address"])
        self.assertIsNotNone(field_value[0]["name"])
        self.assertIsNotNone(field_value[0]["phone_no"])
        self.assertIsNotNone(field_value[0]["rotary_langauge"])
        self.assertIsNotNone(field_value[0]["vendors"])
        self.assertIsNotNone(field_value[0]["website"])
        self.assertIsNotNone(field_value[0]["club_members"])
        for row in (field_value[0]["club_members"]):
            self.assertIsNotNone(["club_member_email"])
            self.assertIsNotNone(["club_member_id"])
            self.assertIsNotNone(["is_active"])
            self.assertIsNotNone(["member_first_name"])
            self.assertIsNotNone(["member_from"])
            self.assertIsNotNone(["member_last_name"])
            self.assertIsNotNone(["member_till"])
            self.assertIsNotNone(["profile"])
            self.assertIsNot
            None(["profile_picture"])

# ------------------author api test case----------------------

    def test_3_individual_author_success(self):
        tester = app.test_client(self)
        response = tester.get("/author/1/")
        field_value = response.get_json()
        # print(field_value)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["author_id"])
        self.assertIsNotNone(field_value[0]["description"])

    def test_4_list_author_success(self):
        tester = app.test_client(self)
        response = tester.get("/author/list/")
        field_value = response.get_json()
        # print(field_value)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["author_id"])
        self.assertIsNotNone(field_value[0]["description"])

# ------------------event api test case-------------------------

    def test_5_individual_event_success(self):
        tester = app.test_client(self)
        response = tester.get("/event/1")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["title"])
        self.assertIsNotNone(field_value[0]["time"])
        self.assertIsNotNone(field_value[0]["address"])

    def test_6_list_event_success(self):
        tester = app.test_client(self)
        response = tester.get("/event/list")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["title"])
        self.assertIsNotNone(field_value[0]["time"])
        self.assertIsNotNone(field_value[0]["address"])

# ------------------post api test case---------------------------

    def test_7_individual_post_success(self):
        tester = app.test_client(self)
        response = tester.get("/post/1/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["author_id"])
        self.assertIsNotNone(field_value[0]["title"])
        self.assertIsNotNone(field_value[0]["content"])
        self.assertIsNotNone(field_value[0]["cover_image_name"])
        self.assertIsNotNone(field_value[0]["created_at"])
        for row in (field_value[0]["post_images"]):
            self.assertIsNotNone(["id"])
            self.assertIsNotNone(["post_id"])
            self.assertIsNotNone(["image_name"])
        for row in (field_value[0]["post_tags"]):
            self.assertIsNotNone(["id"])
            self.assertIsNotNone(["name"])

    def test_8_list_post_success(self):
        tester = app.test_client(self)
        response = tester.get("/post/list/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["id"])
        self.assertIsNotNone(field_value[0]["author_id"])
        self.assertIsNotNone(field_value[0]["title"])
        self.assertIsNotNone(field_value[0]["content"])
        self.assertIsNotNone(field_value[0]["cover_image_name"])
        self.assertIsNotNone(field_value[0]["created_at"])
        for row in (field_value[0]["post_images"]):
            self.assertIsNotNone(["id"])
            self.assertIsNotNone(["post_id"])
            self.assertIsNotNone(["image_name"])
        for row in (field_value[0]["post_tags"]):
            self.assertIsNotNone(["id"])
            self.assertIsNotNone(["name"])

# -------------------user api test case------------------------

    def test_9_individual_user_success(self):
        tester = app.test_client(self)
        response = tester.get("/user/1/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["user_id"])
        self.assertIsNotNone(field_value[0]["first_name"])
        if field_value is None:
            self.assertIsNone(["last_name"])
            self.assertIsNone(["city"])
            self.assertIsNone(["contact_number"])
        else:
            self.assertIsNotNone(["last_name"])
            self.assertIsNotNone(["city"])
            self.assertIsNotNone(["contact_number"])
        self.assertIsNotNone(field_value[0]["email"])

    def test_10_list_user_success(self):
        tester = app.test_client(self)
        response = tester.get("/user/list/")
        field_value = response.get_json()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIsNotNone(field_value[0]["user_id"])
        self.assertIsNotNone(field_value[0]["first_name"])
        if field_value is None:
            self.assertIsNone(["last_name"])
            self.assertIsNone(["city"])
            self.assertIsNone(["contact_number"])
        else:
            self.assertIsNotNone(["last_name"])
            self.assertIsNotNone(["city"])
            self.assertIsNotNone(["contact_number"])
        self.assertIsNotNone(field_value[0]["email"])
