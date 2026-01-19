import webbrowser

class Hero:
    @staticmethod
    def open(link):
        try:
            webbrowser.open(link)
            print("✅ تم فتح الرابط بنجاح")
        except Exception as e:
            print("❌ صار خطأ:", e)