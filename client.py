class MultiChannelConversationalSalesAgentClient:
    def handle_message(self, user_message: str, channel: str = "whatsapp") -> dict:
        return {
            "reply_text": f"Hi! I found the product matching '{user_message}'. You can complete your purchase directly with 1-click checkout below:",
            "one_click_checkout_url": f"https://pay.store.com/checkout?item=auto_match&channel={channel}"
        }
