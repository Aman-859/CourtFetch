from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def fetch_case_data(case_type, case_number, filing_year):
    try:
        
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

       
        driver.get("https://delhihighcourt.nic.in/app/case-number")

        
        captcha_text = driver.find_element(By.ID, "captcha-code").text

        
        driver.find_element(By.ID, "case_type").send_keys(case_type)
        driver.find_element(By.ID, "case_number").send_keys(case_number)
        driver.find_element(By.ID, "year").send_keys(filing_year)
        driver.find_element(By.ID, "captchaInput").send_keys(captcha_text)

        
        search_btn = driver.find_element(By.ID, "search")
        driver.execute_script("arguments[0].click();", search_btn)

        time.sleep(3)   

        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find("table", {"id": "s_judgeTable"})

        if not table:
            return {"status": "failed", "error": "No results table found"}

        rows = table.find("tbody").find_all("tr")
        result_data = []

        for row in rows:
            cols = row.find_all("td")
            row_data = []

            for col in cols:
                # Check for PDF link
                link_tag = col.find("a")
                if link_tag and ".pdf" in link_tag.get("href", ""):
                    text = col.get_text(strip=True)
                    pdf_url = link_tag["href"]
                    row_data.append({"text": text, "pdf_url": pdf_url})
                else:
                    row_data.append({"text": col.get_text(strip=True), "pdf_url": None})

            result_data.append(row_data)

        return {
            "status": "success",
            "case_type": case_type,
            "case_number": case_number,
            "filing_year": filing_year,
            "records": result_data
        }

    except Exception as e:
        return {"status": "failed", "error": str(e)}

    finally:
        try:
            driver.quit()
        except:
            pass
