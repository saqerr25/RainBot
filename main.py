import sys
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def run_bot():
    print("جاري تشغيل محرك الأتمتة...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # تطبيق التمويه لمنع الحظر
        stealth_sync(page)
        
        print("جاري زيارة الموقع...")
        page.goto("https://www.youtube.com/")
        print(f"عنوان الصفحة: {page.title()}")
        
        browser.close()
        print("تمت المهمة بنجاح.")

if __name__ == "__main__":
    run_bot()
  
