from client import MultiChannelConversationalSalesAgentClient

def main():
    client = MultiChannelConversationalSalesAgentClient()
    res = client.handle_message(user_message="Do you have size 10 running shoes in blue?", channel="whatsapp")
    print(f"Reply: {res['reply_text']}")
    print(f"Checkout Link: {res['one_click_checkout_url']}")

if __name__ == "__main__":
    main()
