import asyncio
from pyppeteer import launch

async def html_to_pdf():
    browser = await launch(headless=True)
    page = await browser.newPage()
    
    # Load the local HTML file
    await page.goto(f'file:///Users/mollydepew/graph-spectral-theory/blog_deploy/article.html', waitUntil='networkidle0')
    
    # Generate PDF
    await page.pdf({
        'path': 'article.pdf',
        'format': 'A4',
        'printBackground': True,
        'margin': {
            'top': '20mm',
            'bottom': '20mm',
            'left': '15mm',
            'right': '15mm'
        }
    })
    
    await browser.close()
    print("PDF created: article.pdf")

asyncio.get_event_loop().run_until_complete(html_to_pdf())
