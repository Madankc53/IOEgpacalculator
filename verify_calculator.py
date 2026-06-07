import asyncio
from playwright.async_api import async_playwright
import os
import subprocess
import time

async def test_calculator():
    # Start a local server
    server_process = subprocess.Popen(['python3', '-m', 'http.server', '8000'])
    time.sleep(2)  # Wait for server to start

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto("http://localhost:8000/index.html")

            # Scenario 1: Max Score
            await page.fill("#mathCorrect", "50")
            await page.fill("#phyCorrect", "45")
            await page.fill("#chemCorrect", "25")
            await page.fill("#engCorrect", "22")
            await page.fill("#aptCorrect", "18")
            await page.click("button[type='submit']")

            await page.wait_for_function('document.getElementById("result").classList.contains("hidden") === false')
            final_score = await page.inner_text("#finalScore")
            positive_marks = await page.inner_text("#positiveMarks")
            print(f"Max Score Test: Final Score = {final_score}, Positive Marks = {positive_marks}")
            assert final_score == "228.00"
            assert positive_marks == "228"

            # Reset
            await page.click("#resetBtn")
            await page.wait_for_function('document.getElementById("result").classList.contains("hidden") === true')

            # Scenario 2: Penalty Calculation
            await page.fill("#mathIncorrect", "10")
            await page.click("button[type='submit']")

            await page.wait_for_function('document.getElementById("result").classList.contains("hidden") === false')
            final_score = await page.inner_text("#finalScore")
            negative_marks = await page.inner_text("#negativeMarks")
            print(f"Penalty Test: Final Score = {final_score}, Negative Marks = {negative_marks}")
            assert final_score == "-2.00"
            assert negative_marks == "2.00"

            # Scenario 3: Validation (Sum check)
            await page.click("#resetBtn")
            await page.fill("#mathCorrect", "40")
            await page.fill("#mathIncorrect", "11") # Total 51 > 50
            await page.click("button[type='submit']")

            await page.wait_for_function('document.getElementById("error").classList.contains("hidden") === false')
            error_message = await page.inner_text("#errorMessage")
            print(f"Validation Test (Sum): Error Message = '{error_message}'")
            assert "Error: The sum of correct and incorrect answers cannot exceed the total questions for a subject." in error_message

            await browser.close()
            print("All tests passed!")

    finally:
        server_process.terminate()

if __name__ == "__main__":
    asyncio.run(test_calculator())
