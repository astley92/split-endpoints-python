from SplitTester import Split_API_Request
import datetime

# Set token
token = "add_token_here"

# Create request object
req = Split_API_Request(token)

# # LIST ALL CONTACTS
# req.execute("/contacts")
# req.show_response()

# # CREATE ANYTONE CONTACT
# payload = {
#   "name": "Hunter Thompson",
#   "email": "hunter@batcountry.com",
#   "branch_code": "123456",
#   "account_number": "13048322",
#   "metadata": {
#     "custom_key": "Custom string",
#     "another_custom_key": "Maybe a URL"
#   }
# }
# req.execute("/contacts/anyone", payload=payload, method="POST")
# req.show_response()

# # GET A CONTACT BY ID
# id = "contact_id_here"
# req.execute("/contacts/{}".format(id))
# req.show_response()

# # REMOVE A CONTACT BY ID
# id = "contact_id_here"
# req.execute("/contacts/{}".format(id), method="DELETE")
# req.show_response()

# # UPDATE CONTACT BANK CONNECTION
# id = "contact_id_here"
# req.execute("/contacts/{}/refresh_balance".format(id), method="POST")
# req.show_response()

# # GET ALL BANK ACCOUNTS
# req.execute("/bank_accounts")
# req.show_response()

# # GET ALL BANK CONNECTIONS
# req.execute("/bank_connections")
# req.show_response()

# # GET BANK CONNECTION BY ID
# id = "enter_bank_connection_id_here"
# req.execute("/bank_connections/{}".format(id))
# req.show_response()

# # REMOVE A BANK CONNECTION BY ID
# id = "enter_bank_connection_id_here"
# req.execute("/bank_connections/{}".format(id), method="DELETE")
# req.show_response()

# # CREATE AN OPEN AGREEMENT
# payload = {
#   "title": "Test",
#   "terms": {
#     "per_payout": {
#       "min_amount": None,
#       "max_amount": None
#     },
#     "per_frequency": {
#       "days": None,
#       "max_amount": None
#     }
#   }
# }
# req.execute("/open_agreements", payload=payload, method="POST")
# req.show_response()

# # LIST ALL OPEN AGREEMENTS
# req.execute("/open_agreements")
# req.show_response()
#
# # ACTIVATE CLOSED OPEN AGREEMENT
# agreement_ref = "agreement_ref_here"
# req.execute("/open_agreements/{}/activate".format(agreement_ref), method="POST")
# req.show_response()
#
# # CLOSE ACTIVE OPEN AGREEMENT
# agreement_ref = "agreement_ref_here"
# req.execute("/open_agreements/{}/close".format(agreement_ref), method="POST")
# req.show_response()

# # REQUEST PAYMENT
# payload = {
#   "description": "Visible to both initiator and authoriser",
#   "matures_at": str(datetime.datetime.utcnow()),
#   "amount": 100,
#   "authoriser_contact_id": "5148d73b-7bb8-4f95-87b8-6a5e62ffab04",
#   "precheck_funds": "false",
#   "metadata": {
#     "custom_key": "Custom string",
#     "another_custom_key": "Maybe a URL"
#   }
# }
# req.execute("/payment_requests", payload=payload, method="POST")
# req.show_response()

# # APPROVE PAYMENT REQUEST
# payment_request_id = "payment_request_reference_here"
# req.execute("/payment_requests/{}/approve".format(payment_request_id), method="POST")
# req.show_response()

# # APPROVE PAYMENT REQUEST
# payment_request_id = "payment_request_reference_here"
# req.execute("/payment_requests/{}/decline".format(payment_request_id), method="POST")
# req.show_response()

# # GET PAYMENT REQUEST
# payment_request_id = "payment_request_reference_here"
# req.execute("/payment_requests/{}".format(payment_request_id))
# req.show_response()

# # CANCEL PAYMENT REQUEST
# payment_request_id = "PR.chq"
# req.execute("/payment_requests/{}".format(payment_request_id), method="DELETE")
# req.show_response()

# # LIST ALL INCOMING PAYMENT REQUESTS
# req.execute("/payment_requests/incoming")
# req.show_response()

# # LIST ALL OUTGOING PAYMENT REQUESTS
# req.execute("/payment_requests/outgoing")
# req.show_response()

# # GET A PAYMENT REQUESTS HISTORY
# payment_request_id = "PR.chq"
# req.execute("/payment_requests/{}/history".format(payment_request_id))
# req.show_response()

# # MAKE A PAYMENT
# recipient_contact_id ="contact_id_here"
# payload = {
#   "description": "Test payment",
#   "matures_at": str(datetime.datetime.utcnow()),
#   "payouts": [
#     {
#       "amount": 200,
#       "description": "Test payout",
#       "recipient_contact_id": "{}".format(recipient_contact_id),
#     },
#     {
#       "amount": 400,
#       "description": "Test payout",
#       "recipient_contact_id": "{}".format(recipient_contact_id),
#     }
#   ]
# }
# req.execute("/payments", payload=payload, method="POST")
# req.show_response()

# # LIST ALL PAYMENTS
# req.execute("/payments")
# req.show_response()

# # GET A PAYMENT
# payment_batch_ref = "payment_ref_here"
# req.execute("/payments/{}".format(payment_batch_ref))
# req.show_response()

# # RETRY A CREDIT/DEBIT PAYOUT
# payout_ref = "payout_ref_here"
# req.execute("/payouts/{}/retry".format(payout_ref), method="POST")
# req.show_response()

# # RETRY A CREDIT/DEBIT PAYOUT
# payout_ref = "payout_ref_here"
# req.execute("/payouts/{}".format(payout_ref), method="DELETE")
# req.show_response()

# # ISSUE A REFUND
# credit_ref = "credit_ref_here"
# payload = {
#   "amount": 1,
#   "reason": "Because reason",
#   "metadata": {
#     "custom_key": "Custom string",
#     "another_custom_key": "Maybe a URL"
#   }
# }
# req.execute("/credits/{}/refunds".format(credit_ref), payload=payload,  method="POST")
# req.show_response()

# # LIST INCOMING REFUNDS
# req.execute("/refunds/incoming")
# req.show_response()

# # LIST OUTGOING REFUNDS
# req.execute("/refunds/outgoing")
# req.show_response()

# # RETRIEVE A REFUND REFUNDS
# refund_ref = "refund_ref_here"
# req.execute("/refunds/{}".format(refund_ref))
# req.show_response()

# # LIST ALL TRANSACTIONS
# req.execute("/transactions")
# req.show_response()

# # PROPOSE AN UNASSIGNED AGREEMENT
# payload = {
#   "expiry_in_seconds": 60,
#   "terms": {
#     "per_payout": {
#       "min_amount": None,
#       "max_amount": None
#     },
#     "per_frequency": {
#       "days": None,
#       "max_amount": None
#     }
#   }
# }
# req.execute("/unassigned_agreements", payload=payload, method="POST")
# req.show_response()

# # LIST ALL UNASSIGNED AGREEMENTS
# req.execute("/unassigned_agreements")
# req.show_response()

# # GET AN UNASSIGNED AGREEMENT
# unassigned_agreement_ref = "agreement_ref_here"
# req.execute("/unassigned_agreements/{}".format(unassigned_agreement_ref))
# req.show_response()

# # DELETE AN UNASSIGNED AGREEMENT
# unassigned_agreement_ref = "agreement_ref_here"
# req.execute("/unassigned_agreements/{}".format(unassigned_agreement_ref), method="DELETE")
# req.show_response()

# # GET USER DETAILS
# req.execute("/user")
# req.show_response()
